import sys
from pathlib import Path

class InputHandler:
    
    def __init__(self):
        self.history = []

    def handle(self, user_input : str):
        self.history.append(user_input)

        if Path(user_input).is_file():
            print("ye bru ts a file")
        else:
            sys.exit(f"The file {user_input} doesn't exist.")