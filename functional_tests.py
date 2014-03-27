#! /usr/bin/python3

from selenium import webdriver
import os

chromedriver = "/media/storage/TDD/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

browser = webdriver.Chrome(chromedriver)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
