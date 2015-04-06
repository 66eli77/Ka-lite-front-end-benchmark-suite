from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common import keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import time
import os
import datetime

capabilities = DesiredCapabilities.CHROME
capabilities['loggingPrefs'] = {'performance':'ALL'}
capabilities['chromeOptions'] = {'perfLoggingPrefs': {'traceCategories':'blink.console,disabled-by-default-devtools.timeline'}, 'extensions': [], 'args': []}
# capabilities['perfLoggingPrefs'] = {'traceCategories':'AccountTrackerService,CRLSet,CRLSetFetcher,ETW Trace Event,FileSystem,IndexedDB,RLZ,ServiceWorker,ValueStoreFrontend::Backend,WebCore,audio,base,benchmark,blink,blink,benchmark,blink_gc,browser,browser,navigation,cc,cc,benchmark,cc,disabled-by-default-devtools.timeline,disabled-by-default-blink.debug.layout,disabled-by-default-blink.graphics_context_annotations,disabled-by-default-blink.invalidation,disabled-by-default-cb_command,disabled-by-default-cc.debug,disabled-by-default-cc.debug,disabled-by-default-cc.debug.quads,disabled-by-default-devtools.timeline.layers,disabled-by-default-cc.debug,disabled-by-default-devtools.timeline.layers,disabled-by-default-cc.debug.picture,disabled-by-default-cc.debug.picture,disabled-by-default-devtools.timeline.picture,disabled-by-default-cc.debug.quads,disabled-by-default-cc.debug.scheduler,disabled-by-default-cc.debug.scheduler.now,disabled-by-default-devtools.timeline,disabled-by-default-devtools.timeline.frame,disabled-by-default-devtools.timeline.invalidationTracking,disabled-by-default-gpu.debug,disabled-by-default-gpu.device,disabled-by-default-gpu.service,disabled-by-default-gpu_decoder,disabled-by-default-ipc.flow,disabled-by-default-netlog,disabled-by-default-renderer.scheduler,disabled-by-default-skia,disabled-by-default-system_stats,disabled-by-default-toplevel.flow,disabled-by-default-v8_cpu_profile,event,gpu,identity,input,ipc,ipc,toplevel,leveldb,loader,media,navigation,net,renderer,renderer_host,renderer_host,navigation,skia,startup,sync,sync_lock_contention,test_fps,test_gpu,trace_event_overhead,ui,v8,webkit,webrtc'}

driver = webdriver.Chrome(
	# chrome_options = options,
    executable_path='/Users/Eli/Downloads/chromedriver', #path to the latest version chromedriver 
    desired_capabilities=capabilities)
 
driver.command_executor._commands.update({'getLog': ('POST', '/session/$sessionId/log')})

driver.get('http://news.google.com')
timeline_log = driver.execute('getLog', {'type': 'performance'})['value']

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