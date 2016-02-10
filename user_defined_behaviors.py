from selenium.webdriver.common import keys
from selenium.webdriver import ActionChains
import time

def web_actions(webdriver):
	try:
		elem_1 = webdriver.find_element_by_id("form_input_List - 1")
		elem_2 = webdriver.find_element_by_id("form_input_List - 2")
		elem_3 = webdriver.find_element_by_id("form_input_List - 3")
		elem_4 = webdriver.find_element_by_id("form_input_List - 4")
		elem_5 = webdriver.find_element_by_id("form_input_List - 5")
		elem_6 = webdriver.find_element_by_id("form_input_List - 6")
		elem_7 = webdriver.find_element_by_id("form_input_List - 7")

		for i in range(10):
			elem_1.send_keys("Panda_"+str(i))
			elem_2.send_keys("Gorilla_"+str(i))
			elem_3.send_keys("Rat_"+str(i))
			elem_4.send_keys("Snake_"+str(i))
			elem_5.send_keys("Pig_"+str(i))
			elem_6.send_keys("Penguin_"+str(i))
			elem_7.send_keys("Eagle_"+str(i))

			elem_1.send_keys(keys.Keys.RETURN)
			elem_2.send_keys(keys.Keys.RETURN)
			elem_3.send_keys(keys.Keys.RETURN)
			elem_4.send_keys(keys.Keys.RETURN)
			elem_5.send_keys(keys.Keys.RETURN)
			elem_6.send_keys(keys.Keys.RETURN)
			elem_7.send_keys(keys.Keys.RETURN)

		actionChains = ActionChains(webdriver)
		actionChains.send_keys(keys.Keys.ARROW_DOWN).perform()
		time.sleep(0.5)
		x = 0
		t = 0
		while t < 6:
			t += 1
			if x == 0:
				webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				time.sleep(0.2)
				x += 1
			else:
				webdriver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
				time.sleep(0.2)
				x -= 1

		remover_1 = webdriver.find_element_by_xpath('//*[@id="List - 1"]/li[1]/div/a')
		remover_2 = webdriver.find_element_by_xpath('//*[@id="List - 2"]/li[1]/div/a')
		remover_3 = webdriver.find_element_by_xpath('//*[@id="List - 3"]/li[1]/div/a')
		remover_4 = webdriver.find_element_by_xpath('//*[@id="List - 4"]/li[1]/div/a')
		remover_5 = webdriver.find_element_by_xpath('//*[@id="List - 5"]/li[1]/div/a')
		remover_6 = webdriver.find_element_by_xpath('//*[@id="List - 6"]/li[1]/div/a')
		remover_7 = webdriver.find_element_by_xpath('//*[@id="List - 7"]/li[1]/div/a')

		for i in range(8):
			remover_1.click()
			remover_2.click()
			remover_3.click()
			remover_4.click()
			remover_5.click()
			remover_6.click()
			remover_7.click()

		time.sleep(1)
	finally:
		print "finished!"