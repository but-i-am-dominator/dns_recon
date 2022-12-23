"Pytest Module for Resolver"

from dns_recon import Resolv

def test_resolv_a():
    '''Test resolv_a static method.'''
    test = Resolv.resolv_a("sectigo.com")
    assert test == ('sectigo.com.', '151.139.128.14')

def test_resolv_aaaa():
    '''Test resolv_aaaa static method.'''
    test = Resolv.resolv_aaaa("reddit.com")
    assert test == ('reddit.com.', '2a04:4e42:200::396')

def test_resolv_ns():
    '''Test resolv_aaaa static method.'''
    test = Resolv.resolv_nameserver("sectigo.com")
    assert 'ns1.as48447.net' in test
