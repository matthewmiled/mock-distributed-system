import os
import sys

from webserver.app import setup
from common.logging import setup_loggers
from common.settings import *

setup_loggers()
app = setup()

if __name__ == '__main__':
    app.run('0.0.0.0', PORT)

