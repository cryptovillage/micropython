print(b"1" == 1)
print(b"123" == bytearray(b"123"))
print(b'123' < bytearray(b"124"))
print(b'123' > bytearray(b"122"))
print(bytearray(b"23") in b"1234")
