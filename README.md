# TRMNL On This Day

On This Day in History plugin for TRMNL

<img src="https://media.discordapp.net/attachments/1284987869546549268/1308128200777273485/device-2024-11-18T12-43-4801-00.png?ex=673cd0d2&is=673b7f52&hm=a55369c169a51eecb4598f39653c23a7f9b9ae70dba9a186626fdccfb542557c&=&format=webp&quality=lossless" alt="On This Day" width="50%">

## Intro
This plugin displays the latest entries from the onthisday.com Web page.  The Python code contained here needs to scrape the page and is used to generate plugin data.

## Setup
0. Start at usetrmnl.com/plugins
1. Find "Private Plugin" and click.
2. Click on "Add New".
3. Give it a name, select the refresh rate (once a day is sufficient) and select "Webhook" for the strategy. Click "Save" at the top right.
4. Note the Plugin UUID.
5. Download the "onthisdayinhistory.py" code from this repo and change the line below to have the plugin UUID noted above.
```
PLUGIN_UUID = "<YOUR PLUGIN UUID>"
```
4. Copy HTML from the ".html" files in this repo and paste the contents in for the four views.
5. Run ``onthisdayinhistory.py`` and it should push data to the TRML plugin.  Force a refresh to see if the data populates.

Set up the "onthisdayinhistory.py" Python program to run once a day to push new data to TRMNL.
