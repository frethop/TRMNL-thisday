# TRMNL On This Day

On This Day in History plugin for TRMNL

<kbd>![on-this-day-plugin](https://github.com/frethop/TRMNL-thisday/blob/main/onthisday.png)></kbd>

## Intro
This plugin displays the latest entries from the onthisday.com Web page.  The Python code contained here needs to scrape the page and is used to generate plugin data.

## Setup
0. Start at usetrmnl.com/plugins
1. Find "Private Plugin" and click.
2. Click on "Add New".
3. Give it a name, select the refresh rate (once a day is sufficient) and select "Webhook" for the strategy. Click "Save" at the top right.
4. Note the Plugin UUID.
5. Download the ``onthisdayinhistory.py`` code from this repo and change the line below to have the plugin UUID noted above.
```
PLUGIN_UUID = "<YOUR PLUGIN UUID>"
```
4. Copy HTML from the ".html" files in this repo and paste the contents in for the four views.
5. Run ``onthisdayinhistory.py`` and it should push data to the TRML plugin.  Force a refresh to see if the data populates.

Set up the ``onthisdayinhistory.py`` Python program to run once a day to push new data to TRMNL.
