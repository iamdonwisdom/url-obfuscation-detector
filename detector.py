
import re

ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"

if re.search(ip_pattern, url):
    print("Warning: URL uses an IP address")
    score += 2
