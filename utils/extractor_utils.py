"""

"""

import urllib.request


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
