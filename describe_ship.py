import pyyaml
import argparse

def config_parser():
    parser = argparse.ArgumentParser(description="Describe a ship")
    parser.add_argument('Ship File')
    parser.add_argument('Ship Parts Database')

    return parser

if __name__ == "__main__":
    parser = config_parser()

