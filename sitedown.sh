#! /bin/bash
#
# Check all of my web sites.
# Every website should work with both IPv4 and IPv6
# Every website should work with both HTTP and HTTPS
#
WEBSITES="jeffsilverm.ddns.net jeffsilverman.ddns.net jeffsilverman-aaaa.ddns.net"
RPS="-4 -6"
SCHEME="HTTP HTTPS"
for SITE in $WEBSITES; do
  # echo "Working on site $SITE"
  for IP in $RPS; do
    # echo "Using internet protocol $IP"
    for H in $SCHEME; do
      URL="${H}://$SITE"      
      if curl -I --silent $IP ${H}://$SITE | fgrep "200 OK" > /dev/null; then
        echo "${URL} $IP is good"
      else
        echo "${URL} $IP is *** BAD ***"
      fi
    done
  done
done
