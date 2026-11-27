import sys
from pathlib import Path

class inputHandler:

    def __init__(self):
        self.history = []

    def handle(self, user_input : str):

        self.history.append(user_input)

        if Path(user_input).is_file():
            print("nice bro it exists")
        else:
            sys.exit(f"that shi dont exist bro: {user_input}")

