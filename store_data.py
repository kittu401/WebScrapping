import os
import requests
import random
import requests
import shutil
import urllib.request
from lxml import html
from bs4 import BeautifulSoup

'''
A Gift to Remember (2017) [WEBRip] [1080p] English

A Gift to Remember (2017)

IMDB...............: https://www.imdb.com/title/tt7006938/
FORMAT.............: MP4
CODEC..............: X264 
GENRE..............: Drama / Romance
FILE SIZE..........: 1.48 GB
RESOLUTION.........: 1920*1072
FRAME RATE.........: 23.976 fps
AUDIO..............: AAC 2CH
LANGUAGE...........: English 
RUNTIME............: 1hr 30 min
'''

URL = "https://yts.lt/rss/0/all/all/0"
PATH = 'movies/'
HEADERS = ['IMDB...............:', 'FORMAT.............:',
           'CODEC..............:', 'GENRE..............:', 'FILE SIZE..........:',
           'RESOLUTION.........:', 'FRAME RATE.........:', 'AUDIO..............:',
           'LANGUAGE...........:', 'RUNTIME............:']


def get_links(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'xml')

    movie_links = set()

    for link in soup.find_all('link'):
        movie_links.add(link.text)

    links = []
    for link in movie_links:
        links.append(link)

    return links


def file_exists(path):
    return os.path.exists(path) is not True


def xpath_to_string(tree, xpath):
    data = tree.xpath(xpath)
    data_string = ''.join(data)
    return data_string.strip()


def download_torrent(file_url, filepath):
    if file_exists(filepath):
        r = requests.get(file_url, stream=True)
        with open(filepath, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


def get_data(links):
    for link in links:
        try:
            page = requests.get(link)
            tree = html.fromstring(page.content)
            title = xpath_to_string(
                tree, '//*[@id="mobile-movie-info"]/h1/text()')

            if len(title) is not 0:
                format_movie = 'MP4'
                codec = 'X264'
                audio = 'AAC 2CH'
                movie_path = PATH + title
                if file_exists(movie_path):
                    os.mkdir(movie_path)

                imdb_link = xpath_to_string(
                    tree, '//*[@id="movie-info"]/div[2]/div[2]/a/@href')
                genre = xpath_to_string(
                    tree, '//*[@id = "mobile-movie-info"]/h2[2]/text()')
                year = xpath_to_string(
                    tree, '//*[@id = "movie-info"]/div[1]/h2[1]/text()')

                # 720p DATA
                movie_type_720 = xpath_to_string(
                    tree, '//*[@id="movie-info"]/p/a[1]/text()')
                file_size_720 = xpath_to_string(
                    tree, '//*[@id = "movie-tech-specs"]/div[1]/div[1]/div[1]/text()')
                resolution_720 = xpath_to_string(
                    tree, '//*[@id="movie-tech-specs"]/div[1]/div[1]/div[2]/text()')
                frame_rate_720 = xpath_to_string(
                    tree, '//*[@id="movie-tech-specs"]/div[1]/div[2]/div[2]/text()')
                language_720 = xpath_to_string(
                    tree, '//*[@id="movie-tech-specs"]/div[1]/div[1]/div[3]/text()')
                runtime_720 = xpath_to_string(
                    tree, '//*[@id="movie-tech-specs"]/div[1]/div[2]/div[3]/text()')

                data_720p = (imdb_link, format_movie, codec, genre, file_size_720,
                             resolution_720, frame_rate_720, audio, language_720, runtime_720)

                torrent_link_720p = xpath_to_string(
                    tree, '// *[@id="movie-info"]/p/a[1]/@href')

                try:

                    types_720 = movie_type_720.split('.')
                    if types_720[1] == "WEB":
                        types_720[1] = "WEBRip"

                    main_heading_720 = title + \
                        ' (' + year + ') [' + types_720[1] + \
                        '] [' + types_720[0] + '] ' + language_720

                    sub_heading_720 = title + ' (' + year + ')'

                    torrent_heading_720 = title + \
                        ' (' + year + ') [' + types_720[1] + \
                        '] [' + types_720[0] + '] [YTS.LT]'

                    torrent_path_720p = movie_path + '/' + torrent_heading_720 + '.torrent'

                    if file_exists(torrent_path_720p):
                        download_torrent(torrent_link_720p, torrent_path_720p)

                    zipped_720p = zip(HEADERS, data_720p)
                    file_path_720 = movie_path + "/" + title + "_720p.txt"
                    if file_exists(file_path_720):
                        with open(file_path_720, 'w') as fp:
                            fp.write(main_heading_720 + "\n\n")
                            fp.write(sub_heading_720 + "\n\n")
                            fp.write(''.join('%s %s\n' % x for x in zipped_720p))

                except:
                    print(
                        "Couldn't download 720p torrent and it's other details: : ", title)

                # 1080p DATA
                movie_type_1080 = xpath_to_string(
                    tree, '//*[@id="movie-info"]/p/a[2]/text()')
                file_size_1080 = xpath_to_string(
                    tree, '//*[@id = "movie-tech-specs"]/div[2]/div[1]/div[1]/text()')
                resolution_1080 = xpath_to_string(
                    tree, '//*[@id="movie-tech-specs"]/div[2]/div[1]/div[2]/text()')
                frame_rate_1080 = xpath_to_string(
                    tree, '//*[@id="movie-tech-specs"]/div[2]/div[2]/div[2]/text()')
                language_1080 = xpath_to_string(
                    tree, '//*[@id="movie-tech-specs"]/div[2]/div[1]/div[3]/text()')
                runtime_1080 = xpath_to_string(
                    tree, '//*[@id="movie-tech-specs"]/div[2]/div[2]/div[3]/text()')

                data_1080p = (imdb_link, format_movie, codec, genre, file_size_1080,
                              resolution_1080, frame_rate_1080, audio, language_1080, runtime_1080)

                torrent_link_1080p = xpath_to_string(
                    tree, '//*[@id="movie-info"]/p/a[2]/@href')

                try:
                    types_1080 = movie_type_1080.split('.')
                    if types_1080[1] == "WEB":
                        types_1080[1] = "WEBRip"

                    main_heading_1080 = title + \
                        ' (' + year + ') [' + types_1080[1] + \
                        '] [' + types_1080[0] + '] ' + language_720

                    sub_heading_1080 = title + ' (' + year + ')'
                
                    torrent_heading_1080 = title + \
                        ' (' + year + ') [' + types_1080[1] + \
                        '] [' + types_1080[0] + '] [YTS.LT]'

                    torrent_path_1080p = movie_path + '/' + torrent_heading_1080 + '.torrent'

                    if file_exists(torrent_path_1080p):
                        download_torrent(torrent_link_1080p,
                                         torrent_path_1080p)

                    zipped_1080p = zip(HEADERS, data_1080p)
                    file_path_1080 = movie_path + "/" + title + "_1080p.txt"
                    if file_exists(file_path_1080):
                        with open(file_path_1080, 'w') as fp:
                            fp.write(main_heading_1080 + "\n\n")
                            fp.write(sub_heading_1080 + "\n\n")
                            fp.write(''.join('%s %s\n' % x for x in zipped_1080p))

                except:
                    print(
                        "Couldn't download 1080p torrent and it's other details: ", title)

                img_file_count = len([f for f in os.listdir(movie_path)
                     if f.endswith('.jpg') and os.path.isfile(os.path.join(movie_path, f))])

                if img_file_count != 3:
                    # Image Download
                    image_urls = [
                        # xpath_to_string(tree, '//*[@id = "movie-poster"]/img/@src'),
                        xpath_to_string(
                            tree, '// *[@id = "screenshots"]/div[1]/a[2]/img/@src'),
                        xpath_to_string(
                            tree, '//*[@id="screenshots"]/div[2]/a/img/@src'),
                        xpath_to_string(tree, '//*[@id="screenshots"]/div[3]/a/img/@src')]

                    for index, image in enumerate(image_urls):
                        image = image.replace('medium', 'large')
                        num = random.randrange(10**14, 10**15 - 1, 3)
                        image_path = movie_path + "/" + str(num) + ".jpg"
                        try:
                            if file_exists(image_path):
                                urllib.request.urlretrieve(image, image_path)
                        except:
                            print("Couldn't download image: ", index)

        except Exception as e:
            print(e)
            print("Couldn't download :", link)


LINKS = get_links(URL)
get_data(LINKS)
