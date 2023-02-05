import logging
from logging.config import dictConfig

FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

logger = logging.getLogger("[PROFUL HUNT]")