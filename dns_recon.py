import dns.resolver
from utils import item, warn

def query_record(domain, record_type, debug=True):
    try:
        if debug:
            warn(f"\n[*] Querying {record_type} record")
        answers = dns.resolver.resolve(domain, record_type)
        return [str(record_data) for record_data in answers]
    except Exception as e:
        if debug:
            warn(f"\n[!] No {record_type} record found")
        return []


def dns_recon(domain):
    warn(f"\n[+] Recon for {domain}\n")

    records = {
        "A": "A", 
        "NS": "NS",
        "MX": "MX",
        "TXT": "TXT"
    }

    for record_name, record_type in records.items():
        results = query_record(domain, record_type)
        if results:
            item(f"\n{record_name} :")
            for single_result in results:
                item(f"- {single_result}")
