import logging
from logging import Logger

class PoSync:

    file_path: str = None
    folder_path: str = None

    yes: bool = False
    verbose: bool = False
    dry_run: bool = False
    logger: Logger = None

    def __init__(self, file_path: str, folder_path: str = None, dry_run: bool = False, verbose: bool = False, yes: bool = False) -> None:
        self.yes = yes
        self.verbose = verbose
        self.dry_run = dry_run
        self.file_path = file_path
        self.folder_path = folder_path

        self.init_logger()
        self.logger.setLevel(logging.DEBUG)

    def init_logger(self):
        class CustomFormatter(logging.Formatter):
            grey = "\x1b[38;20m"
            blue = "\x1b[36m"
            yellow = "\x1b[33;20m"
            red = "\x1b[31;20m"
            bold_red = "\x1b[31;1m"
            reset = "\x1b[0m"
            format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

            FORMATS = {
                logging.DEBUG: grey + format + reset,
                logging.INFO: blue + format + reset,
                logging.WARNING: yellow + format + reset,
                logging.ERROR: red + format + reset,
                logging.CRITICAL: bold_red + format + reset
            }

            def format(self, record):
                log_fmt = self.FORMATS.get(record.levelno)
                custom_formatter = logging.Formatter(log_fmt)
                return custom_formatter.format(record)

        self.logger = logging.getLogger('po-sync')
        self.logger.setLevel("DEBUG" if self.verbose else "WARNING")

        console_handler = logging.StreamHandler()
        console_handler.setLevel("DEBUG")
        console_handler.setFormatter(CustomFormatter())

        self.logger.addHandler(console_handler)

    def run(self):
        pass
