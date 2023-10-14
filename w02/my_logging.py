import logging
logging.basicConfig(level = logging.DEBUG)

logging.debug('hello')
logger = logging.getLogger(__name__)
logger.debug('hello')