encoded_msg = input()
key = int(input())
key_byte = key.to_bytes(2, 'little')
key_sum = key_byte[0] + key_byte[1]
print("".join(chr(ord(letter) + key_sum) for letter in encoded_msg))
