# Two types of modules in python:
# - BUilt in Modules
# - External Modules
# List of all the built in Modules: https://docs.python.org/3/py-modindex.html

import math
import os
import mymodule
import requests        

os.abort
print(math.sqrt(16))
mymodule.hello()
r = requests.get("https://www.google.com")
print(r.text)