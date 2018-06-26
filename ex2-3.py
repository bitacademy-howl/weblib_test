from urllib.request import urlopen, Request
from urllib.parse import urlencode

data = urlencode({ 'a': 'Whatdoesthefoxsay', 'b': 'lingdingdingdingdingdiding이희웅' })
print(data)

#
data = data.encode('UTF-8')
request = Request('http://www.example.com', data)

# Request 객체를 사용한 request 헤더 변경
request.add_header('Content-Type', 'text/html')

response = urlopen(request)
print(response.read())
