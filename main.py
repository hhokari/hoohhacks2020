from main_funcs import *
import logging
from logging.config import fileConfig

fileConfig("logging_config.ini")

logger = logging.getLogger("main")

logger.info("Application started")

word = input("Name of event: ")
recipient = input("To whom is this photo for? ")
res = main_func(word, recipient)
