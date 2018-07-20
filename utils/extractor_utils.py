"""

"""

import urllib.request
import json


def url_text_reader(url):
    """

    :param url:
    :return:
    """
    response = urllib.request.urlopen(url)
    data = response.read()  # a `bytes` object
    text = data.decode('utf-8')  # string
    return text


def writer(text, filename):
    """

    :param text:
    :return:
    """
    with open(filename, "w") as f:
        for line in text:
            f.write(line)
    f.close()
    return True


def read_json(file_path):
    """

    :param file_path:
    :return:
    """
    with open(file_path) as data_file:
        data = json.load(data_file)
    return data
