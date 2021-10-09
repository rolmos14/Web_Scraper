number = int(input())
bytes_object = number.to_bytes(2, 'little')
print(bytes_object[0] + bytes_object[1])
