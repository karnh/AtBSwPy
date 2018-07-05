#! python3
# downloadXkcd.py - Download all comic from xkcd.com

import requests, os, bs4

url = 'https://xkcd.com'           # Starting URL
os.makedirs('xkcd', exist_ok=True)      # Store comin in ./xkcd

while not url.endswith('#'):
    # Download the page
    print('Downloading page {} ...'.format(url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Find URL of comic image
    comicElem = soup.select('#comic img')

    if comicElem == []:
        print('Could not fine comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # Download the image
        print('Downloading image {} ...'.format(comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save image to ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get Prev page button's URL
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('done')