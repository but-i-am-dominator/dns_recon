"""Utility class."""

import re
import os
import whois

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
    def whois(ip_addr):
        '''Whois Capability by IP address.'''
        try:
            target = whois.whois(ip_addr)
            return target
        except ValueError as err:
            print(f"Unexpected {err}, {type(err)}")
            return ("NONE", "NONE")
