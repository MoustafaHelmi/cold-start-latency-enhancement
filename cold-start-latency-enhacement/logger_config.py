"""
logger_config.py: Configures the logging format and level for all modules.
"""
import logging

def setup_logging():
    """
    Setup the root logger with a standard format and INFO level.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
    )

# Initialize logging configuration
setup_logging()
logger = logging.getLogger(__name__)

