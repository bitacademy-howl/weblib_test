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
    # 페이지 접근 #######################################################################################
    url = 'www.google.co.kr'
    conn = HTTPConnection(url)

    # 정상응답 200 OK
    conn.request('GET', '/')
    response = conn.getresponse()
    print(response, type(response))

    charset = response.headers.get_content_charset()
    data = response.read().decode(charset)
    ######################################################################################################
    # 이미지 url 구하기 ##################################################################################
    # 이미지 파서 생성 및 데이터 추출 ####################################################################
    # HTMLParser 사용의 3단계
    # 1. 메서드를 재정의 하여 클래스로 지정
    # 2. data(html문서) 를 feeding 하여 결과를 얻어옴.
    # 3. 내부에서 처리하여 객체에 결과값을 저장하도록한다.!
    # 위 3단계 및 HTML parser는 웹 크롤링에 유용하게 사용될 수 있을 것 같으니 많이 사용해볼것!!!
    parser = ImageParser()

    parser.feed(data)                        # 파서는 데이터를 주고 파싱된 결과를 얻어온다.

    # HTMLParser를 상속받아 result 라는 새로운 변수를 지정하고 handle_starttag() 함수로 데이터를 파싱한다.
    # handle_starttag(), 혹은 endtag등 pass 매서드들을 오버라이딩 하여 원하는 결과를 얻어낼 수 있다.
    # 이와 같은 방법으로 웹 크롤링 시 링크를 계속 타고 파싱하여 데이터를 수집하는 등 활용할 수 있겠다.


    # 아래는 파서가 가진 결과물을 따로 저장하는 것인데....
    dataset = set(x for x in parser.result)
    # 아래와 같이 써도 객체가 값을 항상 가지고 있으므로 따로 저장해 놓을 필요는 없겠다.
    # 비교  -------
    print(dataset, type(dataset))
    print(parser.result, type(parser.result))


    # 아래는 데이터 파서가 추출한 result set (sub url : 디렉토리 및 파일명)을 이용하여 해당 이미지를
    # HTTP 로 요청하고, 그 결과를 받아와 파일에 저장하는 단계이다.

    for i in dataset:
        print(i, type(i))
        # 데이터 read 는 위의 방식과 동일하게 요청
        # 읽어온 데이터는 어차피 바이트스트림이므로 그대로 파일에 저장하면 그림파일로 저장될 것!
        conn = HTTPConnection(url)
        conn.request('GET', i)
        response = conn.getresponse()
        data = response.read()

        # 파일이름은 해당 URL의 것을 그대로 사용하도록 한다.
        filename = i.split('/')[len(i.split('/')) - 1]

        # 파일 만들고 write byte 모드로 열어 쓰기.
        with open(RESULT_PATH + '/' + filename, 'wb') as localFile:
            localFile.write(data)

if __name__ == '__main__':
    # 그림 파일을 폴더가 없으면 생성할 것!
    if not os.path.exists(RESULT_PATH):
        os.makedirs(RESULT_PATH)

    main()