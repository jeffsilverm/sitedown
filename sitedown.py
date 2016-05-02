#! /usr/bin/env python3
#
# This is the top level module for sitedown
#
import json
import argparse
import pprint
from collections import OrderedDict



pp = pprint.PrettyPrinter( indent=2  )

class Test ( object ) :
    """Methods to test anything"""

    self.INFORMATIONAL=0
    self.WARNING=1
    self.ERROR=2
    self.FATAL=3

    def __init__ ( self, query_method, severity=self.WARNING ):

        self.query_method = query_method
        self.severify = severity

    def test ( self, query, expected_result, severity=None)
        actual_result = self.query_method ( query )
        if type(actual_result) == type([]) :
            actual_result.sort()
            expected_result.sort()
# There are more error syndromes than this.  Suppose the number of actual results
# is not the same as the number of expected results?
            for l in actual_result :
                if l not 
        
    

class Dns ( object ):
    """Methods to check out name servers"""

    def __init__( self, dns ):
        """dns is an ordered dictionary which has a list of the predicted nameservers,
the answers that the nameservers are supposed to provide for both IPv4 and IPv6"""
        assert type(dns) == type(OrderedDict()), "internal software error, dns is not an OrderedDict"
        assert 'NS' in dns, """Error in configuration file: there should be an 'NS' which has the
IP addresses of the name servers for the domains we care about"""
        assert 'A' in dns, """Error in configuration file: there should be an 'A' key which has the
IPv4 addresses of the servers we care about"""
        assert 'AAAA' in dns, """Error in configuration file: there should be an 'AAAA' key which has
IPv6 addresses of the servers we care about.  If there are no IPv6 addresses, then the value
for this key should be empty"""
        self.nameservers = dns['NS']
        self.ipv4_addresses = dns['A']
        self.ipv6.addresses = dns['AAAA']
# A future improvement would be to add support for other datatypes

    

def get_args ( ):
    """Parse the command line arguments"""

    parser = argparse.ArgumentParser()
# Optional arguments go here (from
# http://stackoverflow.com/questions/24180527/argparse-required-arguments-listed-under-optional-arguments
    parser.add_argument('-o', '--output', help='Output file name', default='stdout')
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-C', '--configuration', action='store',
                               required=True,
                               help='Configuration file name')
# https://docs.python.org/3/library/argparse.html#required  
#    parser.parse_args(['-h'])
    args = parser.parse_args()
    print(args.configuration)
    return args

def parse_config_file ( config_file ):
    """This subroutine parses a configuration file"""

# I want to maintain the order of elements in the imported dictionar, so use an ordered
# dictionary
# From http://stackoverflow.com/questions/6921699/can-i-get-json-to-load-into-an-ordereddict-in-python
    with open(config_file, "r") as json_data:
        configuration = json.load(json_data, object_pairs_hook=OrderedDict)
        assert type(configuration) == type(OrderedDict() )
    return configuration

if __name__ == "__main__" :
    args = get_args()
    config = parse_config_file ( args.configuration )
    pp.pprint( config )
    dns = Dns( config['dns'] )
    ipv4 = Ipv4 ( config['ipv4'] )
    ipv6 = Ipv6 ( config['ipv6'] )
    
