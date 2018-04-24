import logging

logging.basicConfig()
logger = logging.getLogger()  # pylint: disable=C0103
logger.setLevel(logging.INFO)

__all__ = ['logger']
