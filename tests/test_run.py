import os
import sys
from glob import glob

import pytest

sys.path.append("src")

all_messages = pytest.mark.parametrize("filename", glob("src/**message*.py"))


@all_messages
def test_eagreness(filename):

    filename, _ = os.path.splitext(os.path.basename(filename))

    module = __import__(filename)

    with open("messages.txt", "r") as f:
        lines = f.readlines()

    expected_line = f'{module.my_message["name"]} says {module.my_message["message"]}\n'

    assert expected_line in lines
