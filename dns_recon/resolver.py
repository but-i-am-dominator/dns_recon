"""Resolve DNS records."""

import dns.resolver
from dns.resolver import NXDOMAIN

class Resolv:
    """ Resolv DNS"""
    @staticmethod
    def resolv_a(domain, name_server='8.8.8.8'):
        '''Resolve A record.'''
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = [name_server]
        try:
            answer = resolver.resolve(domain, "A")
            first_record = answer.response.answer[0].name
            first_address = answer.response.answer[0][0].address
            return (str(first_record), first_address)
        except NXDOMAIN as err:
            print(f"Unexpected {err}, {type(err)}")
            return ("NONE", "NONE")

    @staticmethod
    def resolv_aaaa(domain, name_server='8.8.8.8'):
        '''Resolve AAAA record.'''
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = [name_server]
        try:
            answer = resolver.resolve(domain, "AAAA")
            first_record = answer.response.answer[0].name
            first_address = answer.response.answer[0][0].address
            return (str(first_record), first_address)
        except NXDOMAIN as err:
            print(f"Unexpected {err}, {type(err)}")
            return ("NONE", "NONE")




test = Resolv.resolv_aaaa("sectigo69.com")
print(test)
