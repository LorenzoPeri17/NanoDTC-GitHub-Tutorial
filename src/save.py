from typing import Dict


def save_message(my_message: Dict[str, str]) -> None:

    with open("messages.txt", "a") as f:
        f.write(f'{my_message["name"]} says {my_message["message"]}\n')
