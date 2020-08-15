# A module is basically a file conatining a set of functions to include in your application. There 
# are core pythons, modules that you can install using pip package manager ( eg Dgango), custom modules

# Core modules

import datetime
from datetime import date
import time
from time import time

today = datetime.date.today()
print(today)

timestamp = time()
print(timestamp)

# Pip module
pip install Django

#import custom module

import validator
from validator import validate_email