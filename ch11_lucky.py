#! python3
# lucky.py - Open several google search results

import requests, sys, webbrowser, bs4

print('Googling ...') # Display text while downloading google page
res = requests.get('https://google.com/search?q={}'.format(' '.join(sys.argv[1:])))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    url = 'http://google.com' + linkElems[i].get('href')
    print('Opening URL: {}'.format(url))
    webbrowser.open(url)