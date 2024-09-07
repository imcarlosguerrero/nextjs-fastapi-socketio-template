import logging

def setup_logger(logger_name: str):
    logger = logging.getLogger(logger_name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(f"%(levelname)s:     [{logger_name}] - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger