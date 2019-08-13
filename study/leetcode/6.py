def convert(s: str, numRows: int) -> str:

    l = []
    c, i, j = 0, 0, numRows

    while len(s[i:j+1]) >= numRows:

        i = c*numRows-c
        j = (c+1)*numRows-c
        l.append(s[i:j])
        c += 1

    print(l)


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    n = 3
    convert(s, 5)
