from bs4 import BeautifulSoup
import requests
from collections import OrderedDict


def get_string_contents_from_url(url):
    # Before we do anything, we need to recognize that a lot of sites have precautions in place to fend off scrapers
    # from accessing their data. The first thing we can do to get around this is spoofing the headers we send along
    # with our requests to make it look like we're a legitimate browser
    # Set headers
    headers = requests.utils.default_headers()
    headers.update(
        {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    scraped_text = {}

    for header in soup.find_all(['h1', 'h2', 'h3']):
        header.get_text()

        p_all_text = []

        for elem in header.next_siblings:
            if elem.name and elem.name.startswith('h'):
                break
            if elem.name == 'p':
                p_text = elem.get_text()
                p_all_text.append(p_text)

        all_p_combined_in_string = " ".join(p_all_text)

        scraped_text[header.get_text()] = all_p_combined_in_string

    return scraped_text
