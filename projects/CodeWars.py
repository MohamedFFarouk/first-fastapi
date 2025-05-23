def binary_to_string(binary):
    fin = ""
    for i in range(0, len(binary), 8):
        byte = binary[i : i + 8]
        fin += chr(int(byte, 2))
    return fin
