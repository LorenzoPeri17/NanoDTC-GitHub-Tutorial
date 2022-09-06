import os
import sys
from glob import glob

import pytest

sys.path.append("src")


@pytest.mark.parametrize("filename", glob("src/*message*.py"))
def test_eagreness(filename):

    filename, _ = os.path.splitext(os.path.basename(filename))

    module = __import__(filename)

    assert "name" in module.my_message.keys()
    assert "message" in module.my_message.keys()

    assert len(module.my_message.keys()) == 2
