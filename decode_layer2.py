# Decode Layer 2: Decode base64 string to final payload
import base64
import re

# Read the Layer 1 decoded content
with open(r'c:\Users\tawk2\Downloads\forexbot\vbs\decoded_layer1.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the base64 string from the gzipfakw variable
# Pattern: gzipfakw = "BASE64_STRING"
match = re.search(r'gzipfakw = "([^"]+)"', content)
if not match:
    print("Could not find base64 string in the file")
    exit(1)

base64_string = match.group(1)
# Remove any line breaks from the base64 string
base64_string = base64_string.replace('\n', '').replace('\r', '')

print("Extracted base64 string:")
print(base64_string)
print()

# Decode base64
decoded_bytes = base64.b64decode(base64_string)
decoded_text = decoded_bytes.decode('utf-8')

print("Decoded Layer 2 (Final Payload):")
print("=" * 80)
print(decoded_text)
print("=" * 80)

# Save the decoded content
with open(r'c:\Users\tawk2\Downloads\forexbot\vbs\decoded_layer2.txt', 'w', encoding='utf-8') as f:
    f.write(decoded_text)

print("\nSaved to: decoded_layer2.txt")
