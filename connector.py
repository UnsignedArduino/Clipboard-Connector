import logging

from create_logger import create_logger
import networkzero as nw0


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


class ClipboardClient:
    def __init__(self, name: str, log_level: int = logging.INFO):
        """
        Create a clipboard client.

        :param name: The name to connect to.
        :param log_level: The logging level. Defaults to info level.
        """
        self.logger = create_logger(name=__name__, level=log_level)
        self.name = name
        self.logger.debug(f"Target: {self.name}")

    def run(self):
        """
        Kick everything into action!
        """
        self.logger.info("Starting client")
