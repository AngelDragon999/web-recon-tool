import dns.resolver

def enumerate_subdomains(domain, wordlist):
    found = []

    for word in wordlist: 
        subdomain = f"{word}.{domain}"
        try:
            dns.resolver.resolve(subdomain, "A")
            found.append(subdomain)
        except Exception:
            pass
    
    return found