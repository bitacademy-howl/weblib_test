# http.client 모듈의 HttpConnection 을 사용한 GET 방식 요청

from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')
# 404 에러
conn.request('GET', '/board')
result = conn.getresponse()
print(result, type(result))


# HTTP 커넥션은 요청에 대한 응답이 이루어지면 바로 끊어지므로 다시 커넥션 부터 시작하여야하낟.
conn = HTTPConnection('www.example.com')
# 정상응답 200 OK
conn.request('GET', '/')
result = conn.getresponse()
print(result, type(result))

print(result.status, type(result.status), result.reason, type(result.reason))
data = result.read().decode("utf-8")
print(data, type(data))



