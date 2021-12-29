from bs4 import BeautifulSoup
from pprint import pprint
import os
import requests

URL_FILE = "./urls.txt"
OUTPUT_DIRECTORY = "./output"


def download(src, dest):
    """Download a URL to a file.

    Args:
        src (str): Source URL to download.
        dest (str): Destination file path.
    """
    r = requests.get(src)
    with open(dest, "wb") as f:
        f.write(r.content)


def NookpediaToDodoAC(url):
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, "html.parser")
    try:
        src = soup.find("div", {"id": "file"}).a.img["src"]
    except AttributeError:
        print("No image found for {}".format(url))
        src = ""
    return str(src)


def main():
    with open(URL_FILE, "r", encoding="utf-8") as f:
        urls = f.readlines()
    for url in urls:
        src = NookpediaToDodoAC(url)
        dest = os.path.join(OUTPUT_DIRECTORY, src.split("/")[-1])
        download(src, dest)
        print("Downloaded {}".format(src))

    # # Also determine closest arrangement for downloaded pictures to 16x9
    # # First count all PNGs in output directory.
    # pngs = [f for f in os.listdir(OUTPUT_DIRECTORY) if f.endswith(".png")]
    # # Then determine the closest arrangement.
    # ideal = 16 / 9
    # out = []
    # for val in range(1, len(pngs) + 1):
    #     x = val
    #     y = len(pngs) / val
    #     out.append((x, y, x / y))
    # out = sorted(out, key=lambda pair: abs(pair[2] - ideal))
    # pprint(out[:10])


if __name__ == "__main__":
    main()
