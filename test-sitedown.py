#! /usr/bin/env python3
#

import nose2
import sitedown


def test_Any_test () :
    """This method is designed to test this class"""

    def test_list_query_1 ( n ) :
        return list( "X" * n )

    def test_list_query_2 ( n ) :
        return list( "Y" * n )

    c = class any_test ( query_method=test_list_query_1 )
    expected = test_list_query_1( 4)
    result, explanation = c.test ( query=4 )
    if ( result != c.OKAY ):
        print ( "There was a problem: %s ", explanation )
    else :
        print ("Passed")

    expected = test_list_query_1( 4)
    result, explanation = c.test ( query=4 )
    if ( result != c.OKAY ):
        print ( "There was a problem: %s ", explanation )
    else :
        print ("Passed")

