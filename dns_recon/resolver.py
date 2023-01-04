"""Resolve DNS records."""

import warnings
import logging
import dns.resolver
import dns.reversename
from dns.resolver import NXDOMAIN
from dns.resolver import NoAnswer

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=ImportWarning)

DEFAULT_NAMESERVER = '8.8.8.8'

class Resolv:
    """ Resolv DNS."""
    @staticmethod
    def resolv_a(domain, name_server=DEFAULT_NAMESERVER):
        '''Resolve A record.'''
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = [name_server]
        try:
            answer = resolver.resolve(domain, "A")
            first_record = answer.response.answer[0].name
            first_address = answer.response.answer[0][0].address
            return (str(first_record), first_address)
        except NXDOMAIN as err:
            logging.debug("Unexpected %s", err)
            return "None"
        except NoAnswer as err:
            logging.debug("Unexpected %s", err)
            return "None"

    @staticmethod
    def resolv_aaaa(domain, name_server=DEFAULT_NAMESERVER):
        '''Resolve AAAA record.'''
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = [name_server]
        try:
            answer = resolver.resolve(domain, "AAAA")
            first_record = answer.response.answer[0].name
            first_address = answer.response.answer[0][0].address
            return (str(first_record), first_address)
        except NXDOMAIN as err:
            logging.debug("Unexpected %s", err)
            return "None"
        except NoAnswer as err:
            logging.debug("Unexpected %s", err)
            return "None"

    @staticmethod
    def resolv_nameserver(domain, name_server=DEFAULT_NAMESERVER):
        '''Resolve nameserver records.'''
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = [name_server]
        try:
            answer = resolver.resolve(domain, "NS")
            response = [str(NS)[:-1] for NS in answer.rrset]
            return response
        except NXDOMAIN as err:
            logging.debug("Unexpected %s", err)
            return "None"
        except NoAnswer as err:
            logging.debug("Unexpected %s", err)
            return "None"

    @staticmethod
    def resolv_spf(domain, name_server=DEFAULT_NAMESERVER):
        '''Resolve SPF records. (Kind of)'''
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = [name_server]
        try:
            answer = resolver.resolve(domain, "TXT")
            response = [str(SPF) for SPF in answer if "spf" in str(SPF)]
            return response
        except NXDOMAIN as err:
            logging.debug("Unexpected %s", err)
            return "None"
        except NoAnswer as err:
            logging.debug("Unexpected %s", err)
            return "None"

    @staticmethod
    def resolv_txt(domain, name_server=DEFAULT_NAMESERVER):
        '''Resolve TXT records. Excluding SPF Records.'''
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = [name_server]
        try:
            answer = resolver.resolve(domain, "TXT")
            response = [str(SPF) for SPF in answer if "spf" not in str(SPF)]
            return response
        except NXDOMAIN as err:
            logging.debug("Unexpected %s", err)
            return "None"
        except NoAnswer as err:
            logging.debug("Unexpected %s", err)
            return "None"

    @staticmethod
    def resolv_soa(domain, name_server=DEFAULT_NAMESERVER):
        '''Resolve SOA records.'''
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = [name_server]
        try:
            answer = resolver.resolve(domain, "SOA")
            response = [str(SPF) for SPF in answer if "spf" not in str(SPF)]
            return response
        except NXDOMAIN as err:
            logging.debug("Unexpected %s", err)
            return "None"
        except NoAnswer as err:
            logging.debug("Unexpected %s", err)
            return "None"

    @staticmethod
    def resolv_dmarc(domain, name_server=DEFAULT_NAMESERVER):
        '''Resolve DMARC records.'''
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = [name_server]
        try:
            answer = resolver.resolve("_dmarc." + domain, "TXT")
            response = [str(DMARC) for DMARC in answer]
            return response
        except NXDOMAIN as err:
            logging.debug("Unexpected %s", err)
            return "None"
        except NoAnswer as err:
            logging.debug("Unexpected %s", err)
            return "None"

    @staticmethod
    def resolv_ptr(ip_addr):
        '''Resolve PTR records.'''
        try:
            addr = dns.reversename.from_address(ip_addr)
            return str(dns.resolver.resolve(addr, "PTR")[0])
        except NXDOMAIN as err:
            logging.debug("Unexpected %s", err)
            return "None"
        except NoAnswer as err:
            logging.debug("Unexpected %s", err)
            return "None"
