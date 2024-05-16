# DuckDuckGo HTML URL extractor

This Python script extracts URLs from a DuckDuckGo search HTML source code file and decodes them before saving them to a text file.

## How to use
For this script to work you should make your search on the html version of DuckDuckGo go and copy the source code of the page. Each search page will have roughly 20-25 results. 


1. **Perform Your Search:**
   - Use the HTML version of DuckDuckGo to perform your search at [DuckDuckGo HTML](https://html.duckduckgo.com/html/).
   - Using google dorks terms such as "intext", "site", "inurl" will give a better results

2. **Copy the Source Code:**
   - Open the source code of the search results page. You can do this by:
     - Adding `view-source:` at the beginning of the URL, or
     - Pressing `Ctrl+U` (in Chrome and Firefox).

3. **Save the Source Code:**
   - Copy the entire source code and save it into a `.txt` file.
   - You can add more than one page

4. **Run the Script:**
   - Execute the script to extract and decode the URLs.


## Requirements

- Python 3.x
- `tkinter` (usually included with Python standard library)
- `beautifulsoup4` lib
- `urllib.parse` lib
- web browser
 
## Installation

Before running the script, ensure you have the necessary libraries installed. You can install `beautifulsoup4` and `urllib` using pip:

```
pip install beautifulsoup4 urllib.parse
```

Duckduckgo html URL extractor by Pedro Webber

