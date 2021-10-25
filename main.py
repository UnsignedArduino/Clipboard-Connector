import logging
from argparse import ArgumentParser

from connector import ClipboardHost, ClipboardClient
from create_logger import create_logger

parser = ArgumentParser(description="Sync text in the clipboard across "
                                    "multiple computers.")
parser.add_argument("--host", help="Run the program as a host. ",
                    action="store_true")
parser.add_argument("name", help="As a host, the name to advertise. "
                                 "As a client, the name to connect to. ")
parser.add_argument("--verbose", help="Show debug messages. ",
                    action="store_true")
args = parser.parse_args()

level = logging.DEBUG if args.verbose else logging.INFO
logger = create_logger(name=__name__, level=level)

if args.host:
    conn = ClipboardHost(name=args.name, log_level=level)
else:
    conn = ClipboardClient(name=args.name, log_level=level)

try:
    conn.run()
except KeyboardInterrupt:
    logger.warning("Exiting")
