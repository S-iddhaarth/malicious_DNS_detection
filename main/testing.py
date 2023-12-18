import dns.resolver

def get_cname(domain):
    try:
        result = dns.resolver.resolve(domain, 'CNAME')
        for cname_record in result:
            print(f'{domain} has CNAME record: {cname_record.target}')
    except dns.resolver.NXDOMAIN:
        print(f'{domain} does not exist.')
    except dns.resolver.NoAnswer:
        print(f'{domain} does not have a CNAME record.')
    except dns.resolver.Timeout:
        print(f'DNS query for {domain} timed out.')
        

# Example usage
get_cname('openaicom-api-bdcpf8c6d2e9atf6.z01.azurefd.net')
