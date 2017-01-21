import yaml
import argparse

ship_database = {}

def config_parser():
    parser = argparse.ArgumentParser(description="Describe a ship")
    parser.add_argument('ship')
    parser.add_argument('-c', '--config', nargs=1)
    parser.add_argument('database', nargs=argparse.REMAINDER, required=False)

    return parser

def load_config(config):
    if not config:
        return

def load_ship_database(database):
    file = open(database, 'r')
    data = yaml.load(file)

def construct_ship(ship):
    file = open(ship, 'w')

if __name__ == "__main__":
    parser = config_parser()
    parser.parse_args()

    load_config(parser.config)

    if not isinstance(parser.database, list):
        load_ship_database(parser.database)
    else:
        for database in parser.database:
            load_ship_database(database)

    construct_ship(parser.ship)



