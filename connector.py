import logging
from time import sleep

import networkzero as nw0

from create_logger import create_logger

NW0_NEWS_TOPIC = "clipboard_connector"


class ClipboardHost:
    def __init__(self, name: str, log_level: int = logging.INFO):
        """
        Create a clipboard host.

        :param name: The name to advertise.
        :param log_level: The logging level. Defaults to info level.
        """
        self.logger = create_logger(name=__name__, level=log_level)
        self.name = name

    def run(self):
        """
        Kick everything into action!
        """
        self.logger.info(f"Starting host under name \"{self.name}\"")
        self.logger.debug("Starting event loop")
        while True:
            self.service()
            sleep(1)

    def service(self):
        """
        Service everything.
        """


class ClipboardClient:
    def __init__(self, name: str, log_level: int = logging.INFO):
        """
        Create a clipboard client.

        :param name: The name to connect to.
        :param log_level: The logging level. Defaults to info level.
        """
        self.logger = create_logger(name=__name__, level=log_level)
        self.name = name

    def run(self):
        """
        Kick everything into action!
        """
        self.logger.info("Starting client")
        self.logger.debug("Starting event loop")
        while True:
            self.service()
            sleep(1)

    def service(self):
        """
        Service everything.
        """
