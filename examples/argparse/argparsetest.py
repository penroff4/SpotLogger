import argparse

# set up arg parser
parser = argparse.ArgumentParser(description='Log Spotify data...')
# set up db-commit argument
# parser.add_argument('--db-commit', metavar='C', type=int, help='1 to commit, 0 to not', default=0)
parser.add_argument('--db-commit', type=int, help='1 to commit, 0 to not', default=0)

arguments=parser.parse_args()

print(arguments)
# arguments.db-commit=0
