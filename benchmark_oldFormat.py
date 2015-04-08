from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import datetime
import os
import imp

options = ChromeOptions()
# options.binary_location = "/Volumes/Google Chrome/Google Chrome.app/Contents/MacOS/Google Chrome" #poin to what version of Chrome you want to use
options.add_argument("--enable-profiling")
options.add_argument("--enable-benchmarking")
options.add_argument("--enable-net-benchmarking")
options.add_argument("--enable-extension-timeline-api")
options.add_argument("--profiling-at-start")
options.add_argument("--memory-profile")

capabilities = DesiredCapabilities.CHROME
capabilities['loggingPrefs'] = {'performance':'INFO'}
capabilities.update(options.to_capabilities())

# if user specified ChromeDriver path, use the ChromeDriver
chromedriver_path = os.environ["chromedriver_path"]
if(chromedriver_path):
	driver = webdriver.Chrome(
		executable_path=chromedriver_path, # if chromedriver is not in the path of python, need to specify here.
	    desired_capabilities=capabilities)
else:
	driver = webdriver.Chrome(desired_capabilities=capabilities)
	 
driver.command_executor._commands.update({'getLog': ('POST', '/session/$sessionId/log')})

# import pre-defined web actions from the user
driver.get(os.environ["benchmark_url"])
actions = imp.load_source('selenium_scripts', os.environ['benchmark_actions'])
actions.web_actions(driver)

# gather the tracing logs for chrome devtools' timeline
timeline_log = driver.execute('getLog', {'type': 'performance'})['value']

# parse and save the timeline logs to disk
now = datetime.datetime.now()
date = str(now)[:10] +':'+ str(now.hour) +'_'+ str(now.minute) +'_'+ str(now.second)
f = open('benchmarkLog_oldFormat' + date + '.json', 'w')
f.write("[")

for dic in timeline_log:
	if 'Timeline.eventRecorded' in dic['message']:
		mydct = json.loads(dic['message'])
		data = mydct['message']['params']['record']
		json.dump(data, f)
		f.write(',')

f.seek(-1, os.SEEK_END)
f.truncate()
f.write(']')
f.close()

driver.quit()