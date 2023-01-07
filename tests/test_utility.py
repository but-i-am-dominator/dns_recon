"Pytest Module for Utility Class."

from dns_recon import Utility

def test_validate_spf():
    '''Test validate_spf static method.'''
    spf = "v=spf1 include:spf.protection.outlook.com ip4:91.199.212.0/24 ip6:2a0e:ac00::/32 -all"
    test = Utility.validate_spf(spf)
    assert test

def test_spf_fail_all():
    '''Test spf_fail_all static method.'''
    spf = "v=spf1 include:spf.protection.outlook.com ip4:91.199.212.0/24 ip6:2a0e:ac00::/32 +all"
    test = Utility.spf_fail_all(spf)
    assert test

def test_whois():
    '''Test whois static method.'''
    taget = "151.139.128.14"
    test = Utility.whois(taget)
    assert 'neteng@stackpath.com' in test['emails']
