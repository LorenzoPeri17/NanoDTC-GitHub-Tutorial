import os
import sys
from glob import glob

import pytest

sys.path.append("src")

all_messages = pytest.mark.parametrize("filename", glob("src/*message*.py"))


@all_messages
def test_present(filename):

    filename, _ = os.path.splitext(os.path.basename(filename))

    module = __import__(filename)

    assert module.my_message


@all_messages
def test_keys(filename):

    filename, _ = os.path.splitext(os.path.basename(filename))

    module = __import__(filename)

    assert "name" in module.my_message.keys()
    assert "message" in module.my_message.keys()
