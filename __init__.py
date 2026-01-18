from .logger import logger as _logger

info = _logger.info
debug = _logger.debug
warning = _logger.warning
error = _logger.error
critical = _logger.critical
ok = _logger.ok
__all__ = ["info", "debug", "warning", "error", "critical", "ok"]
