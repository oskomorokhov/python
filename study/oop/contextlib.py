from contextlib import ContextDecorator
from contextlib import contextmanager


@contextmanager
def open_file(path, mode):
    the_file = open(path, mode)
    yield the_file
    the_file.close()


files = []

for x in range(100000):
    with open_file('foo.txt', 'w') as infile:
        files.append(infile)

for f in files:
    if not f.closed:
        print('not closed')


class makeparagraph(ContextDecorator):
    def __enter__(self):
        print('<p>')
        return self

    def __exit__(self, *exc):
        print('</p>')
        return False


@makeparagraph()
def emit_html():
    print('Here is some non-HTML')


emit_html()
