#! /usr/bin/env python3
#
# This is the top level module for sitedown
#
import json
import 

args = get_args()

config = get_config( config_file )









def get_get_args ( ):
    """Parse the command line arguments"""

    import argparse
    parser = argparse.ArgumentParser()
# Optional arguments go here (from
# http://stackoverflow.com/questions/24180527/argparse-required-arguments-listed-under-optional-arguments
    parser.add_argument('-o', '--output', help='Output file name', default='stdout')
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-C', '--configuration', help='Configuration file name',\
                               required=True)
 # https://docs.python.org/3/library/argparse.html#required  
    parser.parse_args(['-h'])
    args = parser.parse_args()
    print(args.config_file)
    
