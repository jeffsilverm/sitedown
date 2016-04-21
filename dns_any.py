#! /usr/bin/python3
#
#
from dns.resolver import dns
name_server = '8.8.8.8' #Google's DNS server
ADDITIONAL_RDCLASS = 65535
# http://www.dnspython.org/docs/1.10.0/html/toc-dns.rdatatype-module.html
request = dns.message.make_query('google.com', dns.rdatatype.ANY)
request.flags |= dns.flags.AD
print(request)
request.find_rrset(request.additional, dns.name.root, ADDITIONAL_RDCLASS,
                       dns.rdatatype.OPT, create=True, force_unique=True)       
print(request)
response = dns.query.udp(request, name_server)
print(response)
