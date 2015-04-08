from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import datetime
import os
import imp

capabilities = DesiredCapabilities.CHROME
capabilities['loggingPrefs'] = {'performance':'ALL'}
# enable traceCategories of your choice for the new devtools format, which automatically disable timeline log
# for a complete list of traceCategories, open Chrome with this url: chrome://tracing/json/categories
capabilities['chromeOptions'] = {'perfLoggingPrefs': {'traceCategories':'blink.console,disabled-by-default-devtools.timeline'}, 'extensions': [], 'args': []}
# capabilities['perfLoggingPrefs'] = {'enableTimeline':'True'} #enable timeline log

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

# parse and save the tracing logs to disk
now = datetime.datetime.now()
date = str(now)[:10] +':'+ str(now.hour) +'_'+ str(now.minute) +'_'+ str(now.second)
f = open('benchmarkLog' + date + '.json', 'w')
f.write("[")

for dic in timeline_log:
	if 'Tracing.dataCollected' in dic['message']:
		mydct = json.loads(dic['message'])
		data = mydct['message']['params']
		json.dump(data, f)
		f.write(',')

f.seek(-1, os.SEEK_END)
f.truncate()
f.write(']')
f.close()

driver.quit()