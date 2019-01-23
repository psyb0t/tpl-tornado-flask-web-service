#!/usr/bin/env python
import argparse

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from main import app

parser = argparse.ArgumentParser()

parser.add_argument('--debug', nargs='?', const=1, type=int, default=0)
parser.add_argument('--address', nargs='?', const=1, type=str, default='127.0.0.1')
parser.add_argument('--port', nargs='?', const=1, type=int, default=8080)

args = parser.parse_args()


if __name__ == '__main__':
    if args.debug:
        app.run(host=args.address, port=args.port, debug=True)
        exit(0)

    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(args.port, address=args.address)
    IOLoop.instance().start()
