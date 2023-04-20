import logging

def setup_loggers():
    logger = logging.getLogger()
    logHandler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(funcName)s:%(levelname)s: %(message)s')

    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
    logger.setLevel(logging.INFO)