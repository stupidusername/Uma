"""
Logging utilities.
"""

import logging as base_logging

class StartsWithFilter(base_logging.Filter):
    """
    Log filter that filters out log messages that do not start with a specific
    prefix.

    :param str prefix:
    """

    def __init__(self, prefix):
        self.prefix = prefix
        super().__init__()

    def filter(self, record):
        """
        See parent doc.
        """
        return record.getMessage().startswith(self.prefix)
