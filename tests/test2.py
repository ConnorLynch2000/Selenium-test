from selenium import webdriver
from selenium.webdriver.common.by import By

TEST_DESCRIPTION = "Test #2\nThis test case checks first page element.\n\n"
DELIMITER = "-----------------------------------------------------\n\n"
PASSED = "Passed.\n\n"
FAILED = "Failed.\n\n"


def test2(driver):
    elem = driver.find_element(By.XPATH, "/html/body/div/nav/div/ul/li[1]/a")
    try:
        assert "صفحه اصلی" in elem.text
        with open("OutLog.txt", 'at') as out_file:
            out_file.write(TEST_DESCRIPTION)
            out_file.write(PASSED)
            out_file.write(DELIMITER)
    except AssertionError as e:
        with open("OutLog.txt", 'at') as out_file:
            out_file.write(TEST_DESCRIPTION)
            out_file.write(FAILED)
            out_file.write(DELIMITER)