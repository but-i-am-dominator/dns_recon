"Pytest Module for Resolver"

import ipaddress
from dns_recon import Resolv

def test_resolv_a():
    '''Test resolv_a static method.'''
    test = Resolv.resolv_a("sectigo.com")
    assert test == ('sectigo.com.', '151.139.128.14')

def test_resolv_aaaa():
    '''Test resolv_aaaa static method.'''
    test = Resolv.resolv_aaaa("reddit.com")
    ipv6 = ipaddress.ip_address(test[1])
    assert ipv6.version == 6

def test_resolv_ns():
    '''Test resolv_ns static method.'''
    test = Resolv.resolv_nameserver("sectigo.com")
    assert 'ns1.as48447.net' in test

def test_resolv_spf():
    '''Test resolv_spf static method.'''
    test = Resolv.resolv_spf("sectigo.com")
    assert "spf" in test[0]

def test_resolv_txt():
    '''Test resolv_spf static method.'''
    test = Resolv.resolv_txt("sectigo.com")
    assert "google" in test[0]

def test_resolv_soa():
    '''Test resolv_soa static method.'''
    test = Resolv.resolv_soa("sectigo.com")
    assert "ns1.as48447.net" in test[0]

def test_resolv_dmarc():
    '''Test resolv_dmarc static method.'''
    test = Resolv.resolv_dmarc("sectigo.com")
    assert "DMARC" in test[0]

def test_resolv_ptr():
    '''Test resolv_ptr.'''
    test = Resolv.resolv_ptr("151.139.128.10")
    assert test == 'map3.hwcdn.net.'
