from urllib.request import urlopen

# f = urlopen('http://www.naver.com')
f = urlopen('192.168.1.7:8080')
print(f.read())

