import logging

# message formatting
formatting = {
    "brief": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "verbose": "%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s - %(funcName)s - %(lineno)d",
}


def setup_logger(
    name: str = __name__, formatter: str = "brief", level: int = logging.INFO
) -> logging.Logger:
    """
    Sets up logger with specified formatter and severity level.
    """
    assert formatter in formatting, f"formatter must be one of {formatting.keys()}"

    # Formatting handler
    handler = logging.StreamHandler()
    formatter = logging.Formatter(formatting[formatter])
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
