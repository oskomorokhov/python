# just urllib.parse ffs...


def url_decode(s: str = '') -> str:
    #
    result = ''
    i = 0
    while i < len(s):
        print(i)
        if s[i] != '%':
            result += s[i]
            i += 1
        else:
            tmp = bytes.fromhex(s[i+1:i+3])
            print(tmp)
            print(tmp.decode())
            result += tmp.decode()
            i += 3
    return result


if __name__ == "__main__":
    url = 'magnet:?xt=urn:btih:332CA60380EE574BD913F1FB86CA48D61C077D62&tr=http%3A%2F%2Fbt3.t-ru.org%2Fann%3Fmagnet&dn=%D0%A7%D0%B5%D1%80%D0%BD%D0%BE%D0%B1%D1%8B%D0%BB%D1%8C%20%2F%20Chernobyl%20%2F%20%D0%A1%D0%B5%D0%B7%D0%BE%D0%BD%3A%201%20%2F%20%D0%A1%D0%B5%D1%80%D0%B8%D0%B8%3A%201-5%20%D0%B8%D0%B7%205%20(%D0%99%D0%BE%D1%85%D0%B0%D0%BD%20%D0%A0%D0%B5%D0%BD%D0%BA)%20%5B2019%2C%20%D0%92%D0%B5%D0%BB%D0%B8%D0%BA%D0%BE%D0%B1%D1%80%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D1%8F%2C%20%D0%A1%D0%A8%D0%90%2C%20%D0%B4%D1%80%D0%B0%D0%BC%D0%B0%2C%20%D0%B8%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F%2C%20WEB-DL%201080p%5D%20MVO%20(Amedia)%20%2B%20Original%20%2B%20Su'
    print(url_decode(url))
