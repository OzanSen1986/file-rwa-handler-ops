from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()


with open_file("data.txt", "w") as f:
    f.write('Brutality leads to extreme violance.')

print(f.closed)



