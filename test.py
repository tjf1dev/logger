from logger import logger


def showcase():
    logger.info("hi this is a preview of tjf1's logger!")
    logger.info("it uses the default levels and an additional OK level")
    print()
    logger.critical("critical message")
    logger.error("error message")
    logger.warning("warning message")
    logger.ok("ok message")
    logger.info("info message")
    logger.debug("debug message")


showcase()
