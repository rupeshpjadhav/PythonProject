# logging module
# The logging module records messages about what a program is doing.
# It is a better choice than print() for real programs because you can:
#   - filter messages by severity (only show errors, for example)
#   - send messages to the console, a file, or both
#   - add timestamps and other details automatically
# Log levels, from least to most severe:
#   DEBUG < INFO < WARNING < ERROR < CRITICAL

import logging
import os
import tempfile

# Basic configuration
# basicConfig() sets up the root logger once, at the start of the program.
# level=logging.DEBUG means every message from DEBUG and above is shown.
# format controls how each line looks: time, level name, and the message.
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(message)s",   # -8s pads the level name so the columns line up
)

# Writing messages at each level
logging.debug("Debug: detailed information for diagnosing problems")
logging.info("Info: normal progress updates")
logging.warning("Warning: something unexpected, but the program keeps running")
logging.error("Error: a task failed")
logging.critical("Critical: the program may not be able to continue")

# Logging an exception with its traceback
# exception() logs at ERROR level and automatically includes the traceback of the current exception.
# It must be called from inside an except block.
try:
    result = 10 / 0
except ZeroDivisionError:
    logging.exception("Could not divide the numbers")

# Creating a named logger
# getLogger(name) returns a logger for one part of your program. Using __name__ is a common convention.
# Named loggers let you control the level for each part of a large program separately.
logger = logging.getLogger("modules_demo")
logger.setLevel(logging.INFO)     # this logger ignores DEBUG messages
logger.info("Message from a named logger")
logger.debug("This debug message will NOT appear, because the level is INFO")

# Logging to a file
# FileHandler sends log messages to a file. mode="a" appends to the file instead of overwriting it.
# The file goes in a temporary folder so your project stays clean.
log_path = os.path.join(tempfile.mkdtemp(), "modules_demo.log")
file_handler = logging.FileHandler(log_path, mode="a", encoding="utf-8")
file_handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
logger.addHandler(file_handler)
logger.warning("This line is written to the console and the log file")

# Cleaning up the file handler
# close() releases the file so it is not left open. Removing it from the logger stops further writes.
logger.removeHandler(file_handler)
file_handler.close()
print("Log file written to:", log_path)
os.remove(log_path)                # delete the demo log file so nothing is left behind
os.rmdir(os.path.dirname(log_path))
