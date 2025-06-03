import os
import sys
import logging 

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# %(asctime)s	The date and time when the log message was created.ßßß
# %(levelname)s	The severity level of the log message (e.g., DEBUG, INFO, WARNING).
# %(module)s	The name of the Python module (script) where the logging call occurred.
# %(message)s	The actual log message provided by the user.



log_dir = "logs"

log_filepath = os.path.join(log_dir,"running_logs.log")

os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")