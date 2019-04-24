#!/usr/bin/env python
import logging
import argparse
import asyncio
import uvloop
import jinja2
from ret2retro.config import TEMPLATES_PATH

import aiohttp_jinja2
from aiohttp import web

from ret2retro.handlers import index

CONSOLE_LOG_FORMAT = '%(asctime)-10s : %(levelname)-8s : %(message)s'

def main():
    parser = argparse.ArgumentParser(description='Ret2Retro web')
    parser.add_argument('--host', dest='host', type=str, default='0.0.0.0')
    parser.add_argument('-p', '--port', dest='port', type=int, default=80)
    args = parser.parse_args()

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    app = web.Application()
    print(TEMPLATES_PATH)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(TEMPLATES_PATH))
    app.add_routes([
        web.get('/', index)
    ])
    setup_logger()
    web.run_app(app, host=args.host, port=args.port)


def setup_logger():
    formatter = logging.Formatter(CONSOLE_LOG_FORMAT)

    console = logging.StreamHandler()
    console.setFormatter(formatter)
    for logger_name in ['aiohttp']:
        logger = logging.getLogger(logger_name)
        logger.addHandler(console)
        logger.setLevel(logging.INFO)

if __name__ == '__main__':
    main()
