from html.parser import HTMLParser
from http.client import HTTPConnection
import os

RESULT_PATH = '__result__'

class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return

        if not hasattr(self, 'result'):
            self.result = []

        # print(tag, attrs)
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)
                # print(value)

def parseImage(data):
    pass


def main():
    url = 'www.google.co.kr'
    conn = HTTPConnection(url)

    # 정상응답 200 OK
    conn.request('GET', '/')
    response = conn.getresponse()
    print(response, type(response))

    charset = response.headers.get_content_charset()
    data = response.read().decode(charset)

    # 이미지 url 구하기
    print('\n>>>>>>>>>>> Fetch Image From', url)

    # 이미지 파서 생성 및 데이터 추출
    parser = ImageParser()
    parser.feed(data)
    dataset = set(x for x in parser.result)

    for i in dataset:
        conn = HTTPConnection(url)
        conn.request('GET', i)
        response = conn.getresponse()
        data = response.read()

        print(i, type(i))
        filename = i.split('/')[len(i.split('/')) - 1]

        with open(RESULT_PATH + '/' + filename, 'wb') as localFile:
            localFile.write(data)

if __name__ == '__main__':
    if not os.path.exists(RESULT_PATH):
        os.makedirs(RESULT_PATH)
    main()