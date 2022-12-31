"""Utility class."""

import re
import os
import ipwhois

class Utility:
    """ Utility methods."""
    @staticmethod
    def validate_spf(spf_record):
        '''Validate SPF records.'''
        spf_file = os.path.join(os.path.dirname(__file__), 'spf_match.regex')
        with open(spf_file, "r", encoding="utf-8") as regex_file:
            spf_regex = regex_file.read()
        spf_compiled = re.compile(spf_regex)
        match = spf_compiled.match(spf_record)
        return bool(match)

    @staticmethod
    def spf_fail_all(spf_record):
        '''Validate that SPF records do not contain +all.'''
        fail = "+all" in spf_record
        return fail

    @staticmethod
    def whois(ip_address):
        '''Return dictionary with WHOIS information.'''
        who = ipwhois.IPWhois(ip_address).lookup_whois()
        return who
