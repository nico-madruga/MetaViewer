import argparse

parser = argparse.ArgumentParser(description="Saudação pela linha de comando.")
parser.add_argument("nome", help="Nome da pessoa a cumprimentar")
parser.add_argument(
    "-n", "--vezes", type=int, default=1, help="Número de repetições"
)

args = parser.parse_args()

for _ in range(args.vezes):
  print(f"Olá, {args.nome}!")