from random import randint

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    print(environ)
    yield bytes(f'Hello, World! Number: {randint(0, 100)}\n', "utf-8")
    