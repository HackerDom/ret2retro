#!/usr/bin/env python
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
import argparse

from ret2retro_bot.config import BOT_TOKEN, PROXY_SETTINGS
from ret2retro_bot.handlers import start, photo


CONSOLE_LOG_FORMAT = '%(asctime)-10s : %(levelname)-8s : %(message)s'

logger = logging.getLogger('ret2retro_bot')


def main():
    parser = argparse.ArgumentParser(description='Ret2Retro bot')
    args = parser.parse_args()

    setup_logger()

    updater = Updater(BOT_TOKEN, request_kwargs=PROXY_SETTINGS)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('hello', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.photo, photo))

    logger.info('Bot start polling')

    updater.start_polling()
    updater.idle()


def setup_logger():
    formatter = logging.Formatter(CONSOLE_LOG_FORMAT)
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    for logger_name in ['ret2retro_bot']:
        logger = logging.getLogger(logger_name)
        logger.addHandler(console)
        logger.setLevel(logging.INFO)


if __name__ == '__main__':
    main()
