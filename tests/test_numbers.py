from glob import glob


def test_consistency():

    source_messages: int = len(glob("src/*message*.py"))

    with open("messages.txt", "r") as f:
        lines = f.readlines()

    ran_messages: int = len(lines)

    assert source_messages == ran_messages
