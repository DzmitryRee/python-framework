from selenium import webdriver

capabilities = {
	'browsername': 'chrome'
}

driver = webdriver.Remote(
	command_executor='http://localhost:9515',
	desired_capabilities=capabilities
)
driver.quit()
