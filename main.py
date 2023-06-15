import logging
import pathlib
from logging.handlers import TimedRotatingFileHandler

from client import DynamiClient
from dotenv import load_dotenv
from os import getenv
from utils.ext import load_extensions


def main():
    client = DynamiClient("/")
    load_extensions(client)
    client.run(TOKEN)


if __name__ == '__main__':
    load_dotenv()
    TOKEN = getenv("TOKEN")

    file_path = pathlib.Path(f'utils/logs/Dynamichannel.log')
    file_path.touch(exist_ok=True)
    logger = logging.getLogger('dynamichannel')
    logger.setLevel(logging.INFO)
    log_handler = TimedRotatingFileHandler(file_path, when='midnight')
    logger.addHandler(log_handler)
    main()
