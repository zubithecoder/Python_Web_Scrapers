# Get HTML of webpage

import requests as req 

response = req.get("https://google.com")
html = response.text

print(html) 
