import logging
import os
from datetime import datetime

LOG_FILE_NAME=datetime.now().strftime("%m_%d_%Y_%H_%M_%S")+".log"
log_file_path=os.path.join(os.getcwd(),"logs")
os.makedirs(log_file_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(log_file_path,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging started...")