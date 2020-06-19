import sys
from lxml import html
import requests
import random
import webbrowser


class DataFetch:
    def __init__(self, id_num):
        self.id_num = id_num
        page = requests.get(f'https://nhentai.net/g/{self.id_num}/')
        tree = html.fromstring(page.content)
        title = str(tree.xpath(
            '//div[@id="info"]/h1/span[@class="pretty"]/text()')[0])
        # J Title
        j_title = ''
        try:
            j_title = str(tree.xpath(
                '//div[@id="info"]/h2/span[@class="pretty"]/text()')[0])
        except:
            pass
        tags = str(tree.xpath('//span[@class="name"]/text()')[:-1])
        uploaded = str(tree.xpath('//time[@class="nobold"]/text()')[0])
        self._title = title
        self._o_title = j_title
        self._tags = tags
        self._pages = int(
            len(tree.xpath('//div[@class="thumb-container"]')))
        self._uploaded = uploaded
        return

    @property
    def title(self):
        return self._title

    @property
    def o_title(self):
        return self._o_title

    @property
    def tags(self):
        return self._tags

    @property
    def pages(self):
        return self._pages

    @property
    def uploaded(self):
        return self._uploaded


def show_help():
    print('Print help here')


# Find random based on search queues
search_items = (sys.argv)[1:]

# Check for flags
browser_flag = False
all_flag = False
if '--help' in search_items:
    show_help()
    sys.exit()
if '--browser' in search_items:
    browser_flag = True
    search_items.remove('--browser')
if '--all' in search_items:
    all_flag = True
    search_items.remove('--all')

random_doujin = 0

if len(search_items) > 0:

    # Generate search queue
    search_queue = 'https://nhentai.net/search/?q='
    for index, tag in enumerate(search_items):
        temp = tag
        if ':' in temp:
            temp = tag.replace(':', '%3A')
        search_queue += temp
        if index != len(search_items) - 1:
            search_queue += '+'

    # Debug print
    # print(f'Search URL: {search_queue}\nFlags [Browser: {browser_flag}], [All: {all_flag}]')

    # Verify at least one result
    page = requests.get(search_queue)
    tree = html.fromstring(page.content)
    try:
        result = tree.xpath('//div[@class="gallery"]')
    except:
        print('Unexpected Error.')
        sys.exit()
    if len(result) == 0:
        print('No results.')
        sys.exit()

    # Obtain number of pages
    last_link = tree.xpath('//a[@class="last"]/@href')[0]
    num_pos = last_link.find('&page=') + 6
    pages = int(last_link[num_pos:])

    # Generate random page
    random_page = random.randrange(pages) + 1
    random_url = search_queue + '&page=' + str(random_page)
    # random_url = search_queue + '&page=' + str(pages) # DEBUG

    # Geth thumbnail results
    page = requests.get(random_url)
    tree = html.fromstring(page.content)
    thumbs = tree.xpath('//a[@class="cover"]/@href')
    thumb_count = len(thumbs)

    # Get random doujin
    random_thumb = random.randrange(thumb_count)
    random_doujin = thumbs[random_thumb][3:-1]
else:
    # Find completely random
    page = requests.get('https://nhentai.net/random/')
    tree = html.fromstring(page.content)
    random_doujin = str(tree.xpath('//h3[@id="gallery_id"]/text()')[0])

if browser_flag:
    print(f'Opening Doujin in browser...')
    webbrowser.open(f'https://nhentai.net/g/{random_doujin}/')
if all_flag:
    doujin_info = DataFetch(random_doujin)
    print(f'Title:    {doujin_info.title}')
    print(f'          {doujin_info.o_title}')
    print(f'Tags:     {doujin_info.tags}')
    print(f'Pages:    {doujin_info.pages}')
    print(f'Uploaded: {doujin_info.uploaded}')
print(f'Doujin ID: {random_doujin}')
