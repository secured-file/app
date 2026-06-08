# Decode Layer 1: Convert ChrW array to VBScript
import re

# Read the original obfuscated VBScript file
with open(r'c:\Users\tawk2\Downloads\forexbot\vbs\LastFriday.vbs', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the numeric array values using regex
# Pattern matches: Array( _\n  79, 112, 116, ... _)
array_match = re.search(r'Array\([^)]+\)', content, re.DOTALL)
if not array_match:
    print("Could not find Array in the file")
    exit(1)

array_content = array_match.group(0)

# Extract all numeric values from the array
numbers = re.findall(r'\d+', array_content)
numeric_codes = [int(n) for n in numbers]

print(f"Extracted {len(numeric_codes)} numeric values")

# Convert each numeric code to a character using ChrW
decoded_chars = []
for code in numeric_codes:
    decoded_chars.append(chr(code))

# Join all characters to form the decoded VBScript
decoded_vbs = ''.join(decoded_chars)

# Save the decoded content
with open(r'c:\Users\tawk2\Downloads\forexbot\vbs\decoded_layer1.txt', 'w', encoding='utf-8') as f:
    f.write(decoded_vbs)

print(f"Layer 1 decoded content saved to decoded_layer1.txt")
print(f"Total characters: {len(decoded_vbs)}")
print()
print("--- Decoded Layer 1 Content ---")
print(decoded_vbs)
