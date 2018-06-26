# http.client 모듈의 HttpConnection 을 사용한 GET 방식 요청

from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')

# 정상응답 200 OK
conn.request('HEAD', '/')
result = conn.getresponse()
print(result, type(result))


print(result.status, type(result.status), result.reason, type(result.reason))

data = result.read()

print(data, type(data))



