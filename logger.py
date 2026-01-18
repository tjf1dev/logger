import logging
import datetime
from pathlib import Path
from typing import cast

# tjf1's logger setup!
# feel free to use, modify however you want

FILE_LOGGING = False


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
        record.levelname = f"{log_color}{record.levelname}{Colors.RESET}"
        record.msg = f"{log_color}{record.msg}{Colors.RESET}"
        return super().format(record)


OK_LEVEL = 25
logging.addLevelName(OK_LEVEL, "OK")


class ExtLogger(logging.Logger):
    def ok(self, message, *args, **kwargs):
        if self.isEnabledFor(OK_LEVEL):
            self._log(OK_LEVEL, message, args, stacklevel=2, **kwargs)


logging.setLoggerClass(ExtLogger)

logger = cast(ExtLogger, logging.getLogger(__name__))

if logger.hasHandlers():
    logger.handlers.clear()

handler = logging.StreamHandler()

logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logger.propagate = False
handler.setFormatter(
    ColorFormatter(
        "%(asctime)s [ %(levelname)s ] %(message)s (%(funcName)s)",
        datefmt="%d/%m/%Y %H:%M:%S",
    )
)

file_formatter = logging.Formatter(
    "%(asctime)s [ %(levelname)s ] %(message)s: (%(funcName)s)",
    datefmt="%d/%m/%Y %H:%M:%S",
)

colorless_formatter = "%(asctime)s [ %(levelname)s ] %(funcName)s: %(message)s"

log_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")


if FILE_LOGGING:
    Path("logs").mkdir(exist_ok=True)

    latest_handler = logging.FileHandler("logs/latest.log", mode="w")
    latest_handler.setFormatter(file_formatter)

    file_handler = logging.FileHandler(f"logs/{log_filename}")
    file_handler.setFormatter(file_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(latest_handler)


if __name__ == "__main__":
    logger.error(
        "this file isn't meant to be run directly. refer to the readme for more info"
    )

VERSION = 10
