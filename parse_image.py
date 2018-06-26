from html.parser import HTMLParser
from urllib.request import urlopen

class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        print(tag, attrs)
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)
                print(value)

def parseImage(data):
    pass


def main():
    url = 'http://www.google.co.kr'
    response = urlopen(url)
    charset = response.headers.get_content_charset()
    # print(charset)

    data = response.read().decode(charset)
    response.close()

    # print(data)

    print('\n>>>>>>>>>>> Fetch Image From', url)

    parser = ImageParser()
    parser.feed(data)
    dataset = set(x for x in parser.result)

    print('\n'.join(sorted(dataset)))

if __name__ == '__main__':
    main()