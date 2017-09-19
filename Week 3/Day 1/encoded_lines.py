# Create a method that decrypts encoded-lines.txt
def decrypt(file_name):
    of = open("encoded_lines.txt", "r")
    wf = open("decoded_lines.txt", "w")
    wf.write(chr(ord(file_name) - 1))

shifted_list = list(map(decrypt, list("encoded_lines.txt")))
"".join(shifted_list)