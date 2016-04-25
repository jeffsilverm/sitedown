!# /usr/bin/python3
#
#
#

import dnspython


class DNS ( object ) :
    """This class has methods and records results from name servers"""

    def __init__ ( self, domain ) :
        """The DNS object starts with a domain.  Within the domain are
name servers.  Within the name servers are NS records and A records and AAAA records
(there are other things, too, but that comes later)."""
        self.domain = domain
        self.nameservers = query_dns ( domain, "NS" )



    def query_dns ( self, name_server="8.8.8.8", name ="f5.com", rdata_type = dns.rdatatype.ANY ):
        """Query a specific nameserver for a specific label with a specific type"""
        request = dns.message.make_query(name_server, dns.rdatatype.ANY)
        make_query(qname, rdtype, rdclass=1


# From http://stackoverflow.com/questions/13842116/how-do-we-get-txt-cname-and-soa-records-from-dnspython
from dns.resolver import dns
name_server = '8.8.8.8' #Google's DNS server
ADDITIONAL_RDCLASS = 65535
request = dns.message.make_query('google.com', dns.rdatatype.ANY)
request.flags |= dns.flags.AD
request.find_rrset(request.additional, dns.name.root, ADDITIONAL_RDCLASS,
                       dns.rdatatype.OPT, create=True, force_unique=True)       
response = dns.query.udp(request, name_server)
