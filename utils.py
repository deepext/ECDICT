import logging

def setupLogging(level=None):
    logging.root.setLevel(level or logging.INFO)
