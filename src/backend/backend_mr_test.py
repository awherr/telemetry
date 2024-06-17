# Copyright (C) 2018-2024 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import os
import unittest
import uuid
from tempfile import TemporaryDirectory
from unittest.mock import MagicMock

from .backend import BackendRegistry
from ..utils.opt_in_checker import OptInChecker
from ..utils.message import Message, MessageType

class MRTest(unittest.TestCase):
    def init_backend(self):
        self.backend = BackendRegistry.get_backend('mr')("test_backend", "NONE")

    def test_send(self):
        """
        Set a generic message
        """
        data = {
            't': 'event',
            'ec': "event_category",
            'ea': "event_action",
            'el': "event_label",
            'ev': "event_value",
            'number': 1
        }

        self.init_backend()
        self.backend.send(Message(MessageType.EVENT, data))


    def test_build_event_message(self):
        """
        Set a event message
        """
        self.init_backend()
        msg = self.backend.build_event_message("category_build_event_message", "event", "label", 1)
        self.backend.send(msg)

    def test_build_error_message(self):
        """
        Set an error message
        """
        self.init_backend()
        msg = self.backend.build_error_message("category_build_error_message", "error_message")
        self.backend.send(msg)

    def test_build_session_start_message(self):
        """
        Set a start message
        """
        self.init_backend()
        msg = self.backend.build_session_start_message("category_build_session_start_message")
        self.backend.send(msg)

    def test_build_session_end_message(self):
        """
        Set an end trace message
        """
        self.init_backend()
        msg = self.backend.build_session_end_message("category_build_session_end_message")
        self.backend.send(msg)

