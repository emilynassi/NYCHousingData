#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata
import json
import requests as req

#Connecting to API

app_token = "X2gMakh5B2retT4oRxgQy2A9R"
#secret_token = "ta9nc5qJ9OCx3bj3JlXW2BYSEMWbrrtwYwhH"

#url = "https://data.seattle.gov/resource/3k2p-39jp.json?$$app_token=app_token"

#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
url = ("https://data.cityofnewyork.us/resource/7x9x-zpz6.json?$$app_token=" + app_token)
# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.cityofnewyork.us,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = req.get(url).json()

print(results)

# Convert to pandas DataFrame
#results_df = pd.DataFrame(results)