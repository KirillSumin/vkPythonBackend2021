import time
import json


def app(environ, start_response):
    response_body = bytes(json.dumps({'data': str(time.ctime()),
                 'url': str(environ['RAW_URI'])}), 'utf-8')
    start_response(
        '200 OK',
        [('Content-Type','application/json; charset=utf-8'),
        ('Content-Length', str(len(response_body)))])
    return iter([response_body])
