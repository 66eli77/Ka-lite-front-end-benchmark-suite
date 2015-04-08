from selenium.webdriver.common import keys
from selenium.webdriver import ActionChains
import time

def web_actions(webdriver):
	try:
		actionChains = ActionChains(webdriver)
		actionChains.send_keys(keys.Keys.ARROW_DOWN).perform()
		time.sleep(1)
		x = 0
		t = 0
		while t < 6:
			t += 1
			if x == 0:
				webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				time.sleep(1)
				x += 1
			else:
				webdriver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
				time.sleep(1)
				x -= 1
	finally:
		print "finished!"