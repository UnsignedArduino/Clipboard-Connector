import logging
from argparse import ArgumentParser

from create_logger import create_logger

parser = ArgumentParser(description="Sync text in the clipboard across "
                                    "multiple computers.")
parser.add_argument("--verbose", help="Show debug messages",
                    action="store_true")
args = parser.parse_args()

level = logging.DEBUG if args.verbose else logging.INFO
logger = create_logger(name=__name__, level=level)
