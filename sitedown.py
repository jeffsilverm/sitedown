#! /usr/bin/env python3
#
# This is the top level module for sitedown
#
import json
import argparse
import pprint
from collections import OrderedDict



pp = pprint.PrettyPrinter( indent=2  )

class Any_test ( object ) :
    """Methods to test anything"""

    self.OKAY = 0
    self.INFORMATIONAL=1
    self.WARNING=2
    self.ERROR=3
    self.FATAL=4
    self.ACTUAL_RESULT_MISSING_VALUES=100
    self.ACTUAL_RESULT_TOO_MANY_VALUES=101
    self.ACTUAL_RESULT_WRONG_VALUE=102
    self.ACTUAL_RESULT_WRONG_TYPE=103
    
    

    def __init__ ( self, query_method, severity=self.WARNING ):

        self.query_method = query_method
        self.severify = severity

    def do_test ( self, query, expected_result, severity=None):
        actual_result = self.query_method ( query )
        if type(actual_result) == type([]) :
            if not cmp(actual_result, epected_result) :
                return 0, "Okay"
            else :
                result, explanation = compare_list( actual_result, expected_result )
            return result, explanation
        else :
# Surely there are other types that can be tested.            
            if actual_result != expected_result :
                explanation = "Actual result is %s expected result was %s" % \
                    ( str(actual_result), str(expected_result) )
                return self.ACTUAL_RESULT_WRONG_TYPE, explanation
            

    def compare_list ( actual_result, expected_result ):
        """This is a more subtle and informative test than merely testing
for equality"""
        len_actual = len(actual_result)
        len_expected = len(expected_result)
        if len_actual > len_expected :
            explanation = "There are %d elements in the actual list but only %d \
 were expected" % ( len_actual, len_expected)
# A future version will give more detail about the differences
            return self.ACTUAL_RESULT_TOO_MANY_VALUES, explanation
        elif len_actual < len_expected :
            explanation = "There are only %d elements in the actual list but %d \
 were expected" % ( len_actual, len_expected)
            return self.ACTUAL_RESULT_MISSING_VALUES, explanation
        else :
            actual_result.sort()
            expected_result.sort()
            explanation = ""
            for i in actual_result :
                if actual_result[i] != expected_result[i] :
                    explanation += "At %d, the actual was %s but the expected was %s" % \
                    ( i, str(actual_result[i]), str(expected_result[i] ) )
            return self.ACTUAL_RESULT_WRONG_VALUE, explanation
        raise AssertionError("Reached an impossible spot in compare_list()")
    
        
    

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
    """Parse the command line arguments""" sitedown_01.json

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

# I want to maintain the order of elements in the imported dictionar, so use an
# ordered dictionary
# From http://stackoverflow.com/questions/6921699/can-i-get-json-to-load-into-an-ordereddict-in-python
    with open(config_file, "r") as json_data:
        configuration = json.load(json_data, object_pairs_hook=OrderedDict)
        assert type(configuration) == type(OrderedDict() )
    return configuration

if __name__ == "__main__" :
    args = get_args()
    if args['self-test'] :
        test = Test()
        test.unit_test()
    config = parse_config_file ( args.configuration )
    pp.pprint( config )
    dns = Dns( config['dns'] )
    ipv4 = Ipv4 ( config['ipv4'] )
    ipv6 = Ipv6 ( config['ipv6'] )

    
    
