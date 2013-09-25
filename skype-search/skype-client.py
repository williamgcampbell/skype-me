#!/usr/bin/python

import sys
import argparse
    
def usage():
    print 'skype-client.py -i <inputfile> -o <outputfile>'   
    
def config(args):
    print 4
    
def main(argv):
    # top-level parser
    parser = argparse.ArgumentParser(description='Performs lookup operations on a local Skype message store')
    subparsers = parser.add_subparsers(title='Skype client options',
                                       help='Eligible commands')
    
    # config parser
    config_parser = subparsers.add_parser('config', help='Get, add, or update Skype client configuration')
    group = config_parser.add_argument_group('Actions')
    group.add_argument('-l', '--list', help="list all")
    config_parser.add_argument('-u', '--username', help="Username of the Skype account to query against")
    config_parser.add_argument('-db', '--database', help="Path to the database file")
    config_parser.set_defaults(func=config)
    
    # find parser
    find_parser = subparsers.add_parser('find',
                                        help='Print lines matching a pattern')
    group = find_parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-a', '--author', action='store_true', help="Author's Skype username")
    group.add_argument('-c', '--conversation', action='store_false', help="Conversation id for the skype conversation")
    find_parser.add_argument('pattern', help="Message pattern to search for")
    args = parser.parse_args(argv)
    
if __name__ == '__main__':
    main(sys.argv[1:])