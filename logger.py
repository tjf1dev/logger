import logging
import datetime
from pathlib import Path
from typing import cast

# tjf1's logger setup!
# feel free to use, modify however you want

FILE_LOGGING = True
LOG_DIR = "logs"
FILENAME_DATE_STR = "%Y-%m-%d_%H-%M-%S"
LEVEL = logging.DEBUG


class Colors:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    LIGHTBLACK = "\033[90m"
    RESET = "\033[0m"


class ColorFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": Colors.LIGHTBLACK,
        "INFO": Colors.BLUE,
        "WARNING": Colors.YELLOW,
        "ERROR": Colors.RED,
        "CRITICAL": Colors.MAGENTA,
        "OK": Colors.GREEN,
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, Colors.WHITE)
        levelname = f"{log_color}{record.levelname}{Colors.RESET}"
        message = f"{log_color}{record.getMessage()}{Colors.RESET}"
        formatted = f"{self.formatTime(record, self.datefmt)} [ {levelname} ] {message} ({record.funcName})"
        return formatted


default_format = "%(asctime)s [ %(levelname)s ] %(message)s (%(funcName)s)"


def make_formatter(color: bool = False):
    fmt = default_format
    datefmt = "%d/%m/%Y %H:%M:%S"
    return (
        ColorFormatter(fmt, datefmt=datefmt)
        if color
        else logging.Formatter(fmt, datefmt=datefmt)
    )


file_formatter = make_formatter(color=False)
console_formatter = make_formatter(color=True)


class tjf1Logger(logging.Logger):
    def ok(self, message, *args, **kwargs):
        if self.isEnabledFor(OK_LEVEL):
            self._log(OK_LEVEL, message, args, stacklevel=2, **kwargs)


OK_LEVEL = 25
logging.addLevelName(OK_LEVEL, "OK")

logging.setLoggerClass(tjf1Logger)
logger = cast(tjf1Logger, logging.getLogger(__name__))

if logger.hasHandlers():
    logger.handlers.clear()

logger.setLevel(LEVEL)
logger.propagate = False

handler = logging.StreamHandler()
handler.setFormatter(console_formatter)
logger.addHandler(handler)


if FILE_LOGGING:
    Path(LOG_DIR).mkdir(exist_ok=True)
    handlers = [
        (f"{LOG_DIR}/latest.log", "w"),
        (f"{LOG_DIR}/{datetime.datetime.now().strftime(FILENAME_DATE_STR)}.log", "a"),
    ]
    for path, mode in handlers:
        fh = logging.FileHandler(path, mode=mode)
        fh.setFormatter(file_formatter)
        logger.addHandler(fh)


if __name__ == "__main__":
    logger.error(
        "this file isn't meant to be run directly. refer to the readme for more info"
    )

VERSION = 11
