#!/usr/bin/env python
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
import argparse

from ret2retro_bot.handlers import start, photo


CONSOLE_LOG_FORMAT = '%(asctime)-10s : %(levelname)-8s : %(message)s'

logger = logging.getLogger('ret2retro_bot')


BOT_TOKEN = '856173416:AAG6qSSBxzSgZjAxd1g286y1I0rigW30ayI'

PROXY_SETTINGS = {
    'proxy_url': 'socks5://proxy.ruc.tf:52817',
    'urllib3_proxy_kwargs': {
        'username': 'ructf2019',
        'password': 'KeSrKxdVQuhBw1xTIZG2',
    }
}


def main():
    parser = argparse.ArgumentParser(description='Ret2Retro bot')
    args = parser.parse_args()

    setup_logger()

    updater = Updater(BOT_TOKEN, request_kwargs=PROXY_SETTINGS)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.photo, photo))

    logger.info('Bot start polling')

    updater.start_polling()
    updater.idle()


def setup_logger():
    formatter = logging.Formatter(CONSOLE_LOG_FORMAT)

    # logging.basicConfig(level=logging.DEBUG,
    #                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console = logging.StreamHandler()
    console.setFormatter(formatter)
    for logger_name in ['ret2retro_bot']:
        logger = logging.getLogger(logger_name)
        logger.addHandler(console)
        logger.setLevel(logging.INFO)


if __name__ == '__main__':
    main()
