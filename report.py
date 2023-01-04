"""Reporting module."""

###### Imports ######
import pprint
from dns_recon import Resolv

# Reporting Module pulls domains from here.
domain_list = ["ssl247.biz", "sectigo.com", "comodoca.com", "comodoca.net"]




def idomain(domain):
    '''List of tasks for each domain.'''
    a_record = Resolv.resolv_a(domain)
    aaaa_record = Resolv.resolv_aaaa(domain)
    ns_record = Resolv.resolv_nameserver(domain)
    spf_record = Resolv.resolv_spf(domain)
    dmarc_record = Resolv.resolv_dmarc(domain)
    domain_record = {
        "A" : a_record,
        "AAAA" : aaaa_record,
        "NS" : ns_record,
        "SPF": spf_record,
        "DMARC": dmarc_record
    }
    return {"domain": domain, "domain_record": domain_record}


def main():
    '''Main function.'''
    domain_details = [idomain(domain) for domain in domain_list]
    pretty_print = pprint.PrettyPrinter(indent=4)
    for i in domain_details:
        pretty_print.pprint(i)
        print()
    return True


# Run main function
if __name__ == "__main__":
    main()
