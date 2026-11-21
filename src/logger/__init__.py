"""
MIT License

Copyright (c) 2026 tjf1

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

tjf1's logger setup!
feel free to use, modify however you want
"""

import datetime
import logging
from pathlib import Path
from typing import Any, cast

from ansik import ansik

# configuration

LEVEL = logging.DEBUG
FILE_LOGGING = False
LOG_PATH = "logs"
FILENAME_DATE_STR = "%Y-%m-%d_%H-%M-%S"

DATE_FORMAT = "%d/%m/%Y %H:%M:%S"
DEFAULT_FORMAT = "%(asctime)s [ %(levelname)s ] %(message)s (%(funcName)s)"

OK_LEVEL = 25
logging.addLevelName(OK_LEVEL, "OK")


COLORS = {
    "DEBUG": ansik.F.BRIGHT_BLACK,
    "INFO": ansik.F.BRIGHT_CYAN,
    "WARNING": ansik.F.YELLOW,
    "ERROR": ansik.F.RED,
    "CRITICAL": ansik.F.MAGENTA,
    "OK": ansik.F.BRIGHT_GREEN,
}


class ColorFormatter(logging.Formatter):
    """Logging formatter that adds ANSI colors to console output."""

    def format(self, record: logging.LogRecord) -> str:
        """Format a log record with colors based on its severity."""

        log_color = COLORS.get(record.levelname, ansik.F.WHITE)

        timestamp = self.formatTime(record, self.datefmt)
        levelname = f"{log_color}{record.levelname}{ansik.RESET}"
        message = f"{log_color}{record.getMessage()}{ansik.RESET}"
        function = f"{ansik.F.BRIGHT_BLACK}({record.funcName}){ansik.RESET}"

        return f"{timestamp} [ {levelname} ] {message} {function}"


class tjLogger(logging.Logger):
    def ok(self, message: object, *args: object, **kwargs: Any) -> None:
        if self.isEnabledFor(OK_LEVEL):
            self._log(OK_LEVEL, message, args, stacklevel=2, **kwargs)


def make_formatter(color: bool = False) -> logging.Formatter:
    formatter = ColorFormatter if color else logging.Formatter

    return formatter(
        DEFAULT_FORMAT,
        datefmt=DATE_FORMAT,
    )


def setup_logger() -> tjLogger:
    logging.setLoggerClass(tjLogger)

    logger = cast(tjLogger, logging.getLogger(__name__))
    logger.handlers.clear()
    logger.setLevel(LEVEL)
    logger.propagate = False

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(make_formatter(color=True))
    logger.addHandler(console_handler)

    if FILE_LOGGING:
        Path(LOG_PATH).mkdir(parents=True, exist_ok=True)

        timestamp = datetime.datetime.now().astimezone().strftime(FILENAME_DATE_STR)

        file_handlers = [
            (Path(LOG_PATH) / "latest.log", "w"),
            (Path(LOG_PATH) / f"{timestamp}.log", "a"),
        ]

        for path, mode in file_handlers:
            handler = logging.FileHandler(path, mode=mode, encoding="utf-8")
            handler.setFormatter(make_formatter())
            logger.addHandler(handler)

    return logger


logger = setup_logger()


info = logger.info
debug = logger.debug
warning = logger.warning
error = logger.error
critical = logger.critical
ok = logger.ok


__all__ = [
    "COLORS",
    "FILENAME_DATE_STR",
    "FILE_LOGGING",
    "LEVEL",
    "LOG_PATH",
    "ColorFormatter",
    "critical",
    "debug",
    "error",
    "info",
    "logger",
    "ok",
    "warning",
]


def main() -> None:
    logger.critical("CRITICAL")
    logger.error("ERROR")
    logger.warning("WARNING")
    logger.ok("OK")
    logger.info("INFO")
    logger.debug("DEBUG")


if __name__ == "__main__":
    main()
