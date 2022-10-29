import logging
import sys

log_format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(stream=sys.stdout,
                    format=log_format,
                    level=logging.INFO)

logger = logging.getLogger()
