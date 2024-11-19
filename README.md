# TRMNL On This Day

On This Day in History plugin for TRMNL

<img src="https://media.discordapp.net/attachments/1284987869546549268/1308128200777273485/device-2024-11-18T12-43-4801-00.png?ex=673cd0d2&is=673b7f52&hm=a55369c169a51eecb4598f39653c23a7f9b9ae70dba9a186626fdccfb542557c&=&format=webp&quality=lossless" alt="On This Day" width="50%">

## Intro
This plugin displays the latest entries from the onthisday.com Web page.  The Python code contained here needs to scrape the page and is used to generate plugin data.

## Setup
0. Start at usetrmnl.com/plugins
1. Find "Private Plugin" and click.
2. Click on "Add New".
3. Give it a name, and select "Webhook" for the Strategy. Click "Save".
4. Collect the Plugin UUID as well as your TRMNL API key.
5. Download the code and in the same folder as it, create a ``.env`` file, and populate like so:
```
TRMNL_API_KEY="<your api key>"
TODOIST_API="<your api key>"
TRMNL_PLUGIN_ID="<your plugin UUID>"
```
4. Take the code in ``template.html.j2`` and add it as the markup for your TRMNL plugin
5. Run ``main.py`` and if it successfully posts to TRMNL you should be set. You can force a refresh in TRMNL to see if the data populates.

From there, you can schedule the code to run at regular intervals to post to TRMNL based on your desired frequency.
