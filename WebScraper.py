from bs4 import BeautifulSoup
import requests
import logging
from yurl import URL
from requests.exceptions import InvalidURL
from urllib3.exceptions import NewConnectionError


class WebScraper:
    def __init__(self, url):
        headers = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25"
        _headers = {'User-Agent': headers}

        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d %H:%M',
                            filename='event.log',
                            filemode='w')

        # define a Handler which writes INFO messages or higher to the sys.stderr
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        # set a format which is simpler for console use
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        # tell the handler to use this format
        console.setFormatter(formatter)
        # add the handler to the root logger
        logging.getLogger('').addHandler(console)

        req = requests.get(url, _headers)
        soup = BeautifulSoup(req.text, "html.parser")
        urls_set = set()

        for link in soup.find_all('a'):
            new_url = URL(build_valid_url(url, link))
            process_url(urls_set, url, new_url)

        write_url_list_to_file(urls_set, url)


def build_valid_url(base_url, link):
    _scheme = ""
    _host   = ""
    _port   = ""
    _sep    = "//"
    new_url = ""

    if not link.scheme:
        _scheme = "https://"

    if not link.host:
        _host = base_url.host

    if not link.port:
        _port = "443"

    new_url = _scheme + _host + str(link.get('href'))

    return new_url


def get_context_as_text(req):
    return req.text


def process_url(urls_set, url, test_url):

    if not test_url.full_path.__contains__('void('):
        if test_url.host == url.host and not str(test_url) == str(url) and not test_url.path.endswith("/"):
            try:
                logging.debug(str(test_url))
                req = requests.get(test_url)
                if req.status_code >= 400:
                    error_file = open("errors.txt", 'a')
                    err_msg = (test_url + ", " + str(req.status_code) + "\r\n")
                    error_file.write(err_msg)
                    logging.critical("ERROR Validating Link: " + str(test_url) + " Response Code: " + str(req.status_code))
                else:
                    urls_set.add(str(test_url))
                    logging.info("Validating Link: " + str(test_url) + " Response Code: " + str(req.status_code))
            except Exception as e:
                logging.critical(e)
                pass


def get_file_name(url):
    file_name = str(url.host + url.path)
    if file_name.endswith("/"):
        file_name = file_name.rstrip("/")

    file_name = file_name.replace("www.","")
    file_name = file_name.replace(".com","")
    file_name = file_name.replace("https://", "")
    file_name = file_name.replace("/", ".")

    return file_name


def write_url_list_to_file(urls_set, url):
    try:
        file_name = get_file_name(url)
        f = open(file_name, "a")

        for url_item in urls_set:
            f.write("{0}\r\n".format(url_item))
    except Exception as e:
        logging.critical("Filename too long")
        pass


def process_urls_from_file(url):
    file_name = get_file_name(url)
    f = open(file_name, "r")
    for line in f:
        line = line.rstrip('\n')
        line = line.rstrip("/")

        WebScraper(URL(line))


def_url = URL("https://www.cnn.com").setdefault(host="www.cnn.com", scheme="https")

WebScraper(def_url)
process_urls_from_file(def_url)
