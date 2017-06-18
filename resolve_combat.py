import argparse
import yaml
import json
import sys

"""
Parses rules from yaml files and runs those
"""
def config_parser():
    parser = argparse.ArgumentParser(description="Loads combat resolution rules")
    parser.add_argument('rules')
    parser.add_argument('-c', '--config', nargs=1)
    parser.add_argument('database', nargs=argparse.REMAINDER, required=False)

if __name__ == "__main__":
    parser = config_parser()
    parser.parse_args()




