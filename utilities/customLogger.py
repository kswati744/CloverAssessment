import logging
import os
class LogGen:
    @staticmethod
    def loggen():
        log_path = os.path.join(os.path.dirname(__file__), '..', 'Logs', 'automation.log')
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        log_format = ('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s')
        logging.basicConfig(filename=log_path,
                            level=logging.INFO,
                            format=log_format,
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        return logger
