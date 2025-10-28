"""Structured logging configuration."""
import logging
import sys
from datetime import datetime

def setup_logging(log_level: str = "INFO"):
    """Configure structured logging with JSON output."""
    # Create custom JSON formatter
    class JSONFormatter(logging.Formatter):
        def format(self, record):
            log_data = {
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "level": record.levelname,
                "module": record.module,
                "function": record.funcName,
                "message": record.getMessage(),
            }
            return str(log_data)
    
    # Configure root logger
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(message)s',
        handlers=[logging.StreamHandler(sys.stdout)]
    )
    
    # Set formatter
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JSONFormatter())
    root_logger = logging.getLogger()
    root_logger.handlers = [handler]
    root_logger.setLevel(getattr(logging, log_level.upper()))
    
    return root_logger

