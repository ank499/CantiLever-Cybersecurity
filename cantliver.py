import whois
import csv
import os

# CSV file ka naam
file_name = 'domain_info.csv'

# Agar file nahi hai, to header add karo
if not os.path.exists(file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Domain', 'Registrar', 'Creation Date', 'Expiry Date', 'Name Servers'])

# Function to fetch domain info
def fetch_domain_info(domain_name):
    try:
        domain = whois.whois(domain_name)
        registrar = domain.registrar
        creation_date = domain.creation_date
        expiry_date = domain.expiration_date
        name_servers = domain.name_servers

        # Terminal output
        print(f"\nDomain: {domain_name}")
        print(f"Registrar: {registrar}")
        print(f"Creation Date: {creation_date}")
        print(f"Expiry Date: {expiry_date}")
        print(f"Name Servers: {name_servers}")

        # CSV me save
        with open(file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([domain_name, registrar, creation_date, expiry_date, name_servers])

    except Exception as e:
        print(f"Error fetching info for {domain_name}: {e}")

# Single or multiple domains input
domains_input = input("Enter domain names separated by comma: ")
domains = [d.strip() for d in domains_input.split(',') if d.strip() != ""]

for domain in domains:
    fetch_domain_info(domain)

print(f"\nAll domain info saved to {file_name}")
