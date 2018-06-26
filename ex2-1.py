#url parser

from urllib.parse import urlparse, urlsplit, urljoin, parse_qs, parse_qsl

url = 'http://www.python.org:80/guido/python.html;philosophy?overall=3#here'
result_urlparse = urlparse(url)
print(result_urlparse, type(result_urlparse))

result_urlsplit = urlsplit(url)
print(result_urlsplit, type(result_urlsplit))

# parse_qs 함수코드 - .html 이후의 것을 = 을 기준으로 딕셔너리의 형태로 저장하는 듯
result_parse_qs = parse_qs(url)
print(result_parse_qs, type(result_parse_qs))

base = 'www.google.com'
url = '/search?q=fragment&oq=fragment&aqs=chrome..69i57j0l5.1165j0j7&sourceid=chrome&ie=UTF-8'

# 라고 한다면 해당 유알엘을 그냥 조인 하여 사용 할 수 있으려나.
result_urljoin = urljoin(base = base, url = url)
print(result_urljoin, type(result_urljoin))

'''
def parse_qs(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace'):
    
    parsed_result = {}
    
    pairs = parse_qsl(qs, keep_blank_values, strict_parsing,
                      encoding=encoding, errors=errors)
    for name, value in pairs:
        if name in parsed_result:
            parsed_result[name].append(value)
        else:
            parsed_result[name] = [value]
    return parsed_result
    '''
# 위의 parse_qs 는 내부에서 아래의 함수를 호출....

'''
def parse_qsl(qs, keep_blank_values=False, strict_parsing=False,
              encoding='utf-8', errors='replace'):
    qs, _coerce_result = _coerce_args(qs)
    pairs = [s2 for s1 in qs.split('&') for s2 in s1.split(';')]
    r = []
    for name_value in pairs:
        if not name_value and not strict_parsing:
            continue
        nv = name_value.split('=', 1)
        if len(nv) != 2:
            if strict_parsing:
                raise ValueError("bad query field: %r" % (name_value,))
            # Handle case of a control-name with no equal sign
            if keep_blank_values:
                nv.append('')
            else:
                continue
        if len(nv[1]) or keep_blank_values:
            name = nv[0].replace('+', ' ')
            name = unquote(name, encoding=encoding, errors=errors)
            name = _coerce_result(name)
            value = nv[1].replace('+', ' ')
            value = unquote(value, encoding=encoding, errors=errors)
            value = _coerce_result(value)
            r.append((name, value))
    return r
'''
''' 끝이 없다....코드로 봐선 노답인거 같으니...
    그냥 설명을 읽자
'''

# parse 쿼리의 설명
# 요약하자면 문자열로 명시된 아규먼트에 대한 응답을 가져온다.
# qs : 퍼센트-인코디드 쿼리스트링 (가져와야 할 요청)
# keep_blank_value : 공백값을 그대로 유지할 것인지에 대한 옵션, 파라미터의 값은 boolean
# strict_parsing : 파싱에러 처리에 관한 옵션,
#                  true 이면 에러 발생 시 ValueError 반환
#                  false 이면 에러 발생 시 무시
# encoding : 파싱될 데이터의 인코딩 값 명시, errors 는 지난번 사용해 보았던 'replace' 옵션 디폴트

"""Parse a query given as a string argument.

        Arguments:

        qs: percent-encoded query string to be parsed

        keep_blank_values: flag indicating whether blank values in
            percent-encoded queries should be treated as blank strings.
            A true value indicates that blanks should be retained as
            blank strings.  The default false value indicates that
            blank values are to be ignored and treated as if they were
            not included.

        strict_parsing: flag indicating what to do with parsing errors.
            If false (the default), errors are silently ignored.
            If true, errors raise a ValueError exception.

        encoding and errors: specify how to decode percent-encoded sequences
            into Unicode characters, as accepted by the bytes.decode() method.

        Returns a dictionary.
"""

# urljoin 함수
'''
def urljoin(base, url, allow_fragments=True):
    """Join a base URL and a possibly relative URL to form an absolute
    interpretation of the latter."""
    if not base:
        return url
    if not url:
        return base

    base, url, _coerce_result = _coerce_args(base, url)
    bscheme, bnetloc, bpath, bparams, bquery, bfragment = \
            urlparse(base, '', allow_fragments)
    scheme, netloc, path, params, query, fragment = \
            urlparse(url, bscheme, allow_fragments)

    if scheme != bscheme or scheme not in uses_relative:
        return _coerce_result(url)
    if scheme in uses_netloc:
        if netloc:
            return _coerce_result(urlunparse((scheme, netloc, path,
                                              params, query, fragment)))
        netloc = bnetloc

    if not path and not params:
        path = bpath
        params = bparams
        if not query:
            query = bquery
        return _coerce_result(urlunparse((scheme, netloc, path,
                                          params, query, fragment)))

    base_parts = bpath.split('/')
    if base_parts[-1] != '':
        # the last item is not a directory, so will not be taken into account
        # in resolving the relative path
        del base_parts[-1]

    # for rfc3986, ignore all base path should the first character be root.
    if path[:1] == '/':
        segments = path.split('/')
    else:
        segments = base_parts + path.split('/')
        # filter out elements that would cause redundant slashes on re-joining
        # the resolved_path
        segments[1:-1] = filter(None, segments[1:-1])

    resolved_path = []

    for seg in segments:
        if seg == '..':
            try:
                resolved_path.pop()
            except IndexError:
                # ignore any .. segments that would otherwise cause an IndexError
                # when popped from resolved_path if resolving for rfc3986
                pass
        elif seg == '.':
            continue
        else:
            resolved_path.append(seg)

    if segments[-1] in ('.', '..'):
        # do some post-processing here. if the last segment was a relative dir,
        # then we need to append the trailing '/'
        resolved_path.append('')

    return _coerce_result(urlunparse((scheme, netloc, '/'.join(
        resolved_path) or '/', params, query, fragment)))
        '''
