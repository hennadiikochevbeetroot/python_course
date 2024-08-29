import logging
from contextlib import contextmanager

# Logging has levels of severity:
# From Low to High:
# DEBUG - INFO - WARNING - ERROR - CRITICAL
#
# When log level is WARNING,
# only WARNING and higher severity logs would be printed
# logger = logging.getLogger()
# logger.debug('Debug message')
# logger.info('Info message')
# logger.error('Error message')
# logging.DEBUG


@contextmanager
def log_level(level):
    logger = logging.getLogger()
    old_level = logger.level
    logger.setLevel(level)

    try:
        yield
    finally:
        logger.setLevel(old_level)


# Configure logging:
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
logging.debug("This debug message is outside and won't be shown")

with log_level(logging.DEBUG):
    logging.debug("This is a debug message inside debug-level context")

logging.debug("This debug message is outside and won't be shown")
