#! /usr/bin/python3
#
# This file does a DNS test

import dns.resolver

answers = dns.resolver.query('dnspython.org', 'MX')
for rdata in answers:
    print ('Host', rdata.exchange, 'has preference', rdata.preference )
    
answers = dns.resolver.query('f5.com', 'NS')
for rdata in answers :
    print (rdata)
    print (type(rdata))
    print (dir(rdata))
    print (rdata.rdclass)
    

    
