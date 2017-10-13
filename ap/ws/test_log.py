import logging
from logging.handlers import SysLogHandler
# import logging.handlers

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# handler = logging.handlers.SysLogHandler(address='/dev/log')
handler = SysLogHandler(address='/dev/log')

my_logger.addHandler(handler)

my_logger.debug('Test: This is debug')
my_logger.critical('Test: This is critical')
