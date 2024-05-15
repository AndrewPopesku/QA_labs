import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

GROUP = "302-А"

def test_group_selection_and_schedule_display():
    driver = webdriver.Chrome()

    driver.get("http://fmi-schedule.chnu.edu.ua/")

    time.sleep(1)

    autocomplete_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/section/div[1]/form/div[2]/div/div/div/div/button[2]"))
    )
    autocomplete_dropdown.click()

    group_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".MuiAutocomplete-option"))
    )
    my_group = next((elem for elem in group_elements if elem.text == GROUP), None)

    assert my_group, "Specified group not found in the list."
    my_group.click()
    
    submitButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/section/div[1]/form/button"))
    )
    submitButton.click()

    scheduleTitle = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/h1[contains(text(), '" + GROUP + "')]"))
    )
    assert GROUP in scheduleTitle.text, "Schedule title does not contain the group."


test_group_selection_and_schedule_display()