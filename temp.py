from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np 
import time
import datetime

real_text = "Siddharth institute (More Jobs) Well well"

text_inital = real_text.find('(')
text_last = real_text.find(')')


text=real_text[:text_inital]
# print(text)

texta = real_text[text_last+1:]
print(texta)

print('\n '+ text + texta)