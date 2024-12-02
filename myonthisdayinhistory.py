#--------------------------------------------------------------------------
#
#  onthisday.py -- Scrape the onthisday.com page and push the most recent 
#  entries as variables to a TRMNL plugin.

import requests
from bs4 import BeautifulSoup
from datetime import datetime

PLUGIN_UUID = "9242f452-2a86-48e3-9449-cfd4bf172f3d"

# Start by fetching onthisday page
URL = "https://www.onthisday.com/"
page = requests.get(URL)

# Parse the page with BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")
lines = soup.find_all("li", class_="event")

# Split out the lines containing "on this day" entries and take the
# last 8
linelist = []
for line in lines:
    linetext = line.text
    if linetext[0] <= '9':
        pos = linetext.find(" ")
        if pos < 4:
            linetext = "0"+linetext
        linelist.append(linetext)
linelist = sorted(linelist)
linelist = linelist[-8:]

# Generate the HTML versions of the 8 entries in 4 parts, to be used
# by different views in a TRMNL plugin configuration
htmlCols = [""] * 4
count = 0
index = int(count / 2)
for item in linelist:
    html = ""
    if len(item) > 0:
        html += '<div class="item">'
        html +=     '<div class="meta">'
        html +=         '<span class="index">&nbsp;</span>'
        html +=     '</div>'
        html +=     '<div class="content">'
        item = item.replace(" ", ":", 1)
        pieces = item.split(":")
        html +=         '<span class="title">'+pieces[0]+'</span>'
        html +=         '<span class="description clamp--2">'+pieces[1]+'</span>'
        html +=     '</div>'
        html += '</div>'
    htmlCols[index] += html
    count += 1
    index = int(count / 2)

# Send the date + 4 views in to TRMNL
todaystr = datetime.now().strftime("%m/%d/%Y")
url = "https://usetrmnl.com/api/custom_plugins/" + PLUGIN_UUID
variables = {"merge_variables": {"date": todaystr, 
                                 "itemsColOne": htmlCols[0], "itemsColTwo": htmlCols[1],
                                 "itemsColThree": htmlCols[2], "itemsColFour": htmlCols[3],  }}
result = requests.post(url, json=variables)
if result.status_code != 200:
    print(result.text)
