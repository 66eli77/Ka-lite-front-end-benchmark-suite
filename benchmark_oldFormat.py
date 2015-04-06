from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common import keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import time
import datetime
import os

options = ChromeOptions()
options.binary_location = "/Volumes/Google Chrome/Google Chrome.app/Contents/MacOS/Google Chrome"
options.add_argument("--enable-profiling")
options.add_argument("--enable-benchmarking")
options.add_argument("--enable-net-benchmarking")
options.add_argument("--enable-extension-timeline-api")
options.add_argument("--profiling-at-start")
options.add_argument("--memory-profile")

capabilities = DesiredCapabilities.CHROME
capabilities['loggingPrefs'] = {'performance':'INFO'}
# capabilities['perfLoggingPrefs'] = {'enableTimeline':'True'}
capabilities['perfLoggingPrefs'] = {'tracingCategories':'disabled-by-default-devtools.timeline', 'enableTimeline':'True'}
capabilities.update(options.to_capabilities())

driver = webdriver.Chrome(
    # executable_path="chromedriver2_server", #if chromedriver is not in the path of python, need to specify here.
    desired_capabilities=capabilities)
 
driver.command_executor._commands.update({
    'getAvailableLogTypes': ('GET', '/session/$sessionId/log/types'),
    'getLog': ('POST', '/session/$sessionId/log')})

driver.get('http://news.google.com')
timeline_log = driver.execute('getLog', {'type': 'performance'})['value']

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