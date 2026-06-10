
from urllib.parse import urlparse
import re

url = input("Enter URL: ")

score = 0

keywords = [
    "login",
    "verify",
    "secure",
    "update",
    "account",
    "password"
]

print("\n===== URL ANALYSIS REPORT =====")

# Check suspicious keywords
for word in keywords:
    if word in url.lower():
        print(f"[!] Suspicious keyword detected: {word}")
        score += 1

# Check for IP address URLs
ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"

if re.search(ip_pattern, url):
    print("[!] URL uses an IP address")
    score += 2

# Parse URL
parsed = urlparse(url)

# Check excessive subdomains
if parsed.netloc.count('.') > 2:
    print("[!] Excessive subdomains detected")
    score += 2

# Risk classification
print(f"\nRisk Score: {score}")

if score >= 5:
    print("Risk Level: HIGH")
elif score >= 3:
    print("Risk Level: MEDIUM")
else:
    print("Risk Level: LOW")

print("\nRecommendation:")
if score >= 3:
    print("Avoid interacting with this URL until verified.")
else:
    print("No obvious phishing indicators detected.")
