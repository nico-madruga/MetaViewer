import argparse
from core import inputHandler

def main():

    handler = inputHandler.inputHandler()

    parser = argparse.ArgumentParser(description="Saudação pela linha de comando.")
    parser.add_argument("nome", help="Nome da pessoa a cumprimentar")
    parser.add_argument(
        "-f", "--file", type=str, help="Path of file to scan"
    )
    parser.add_argument(
    "-v", "--version", action="version", version="MetaViewer 1.0"
    )

    args = parser.parse_args()

    file = args.file

    handler.handle(file)
    

if __name__ == "__main__":
    main()