from pwn import *
file = 'files_to_diss/pwnexercise'
qword = 'infA'
conn = remote('158.39.77.181', 6001)
tekst = conn.recv(1024)
conn.send(b'infA')
# cheat
first = conn.recv(94)

while(True):
    math = conn.recv(1024)
    as_str = str(math, 'utf-8')
    print(as_str)
    liste = as_str.split(" ")
    print(liste[0])
    print(liste[2])

    var1 = int(re.sub("[^0-9]", "", liste[0]))
    var2 = int(re.sub("[^0-9]", "", liste[2]))

    print(f"Tall 1 er: {var1} Tall 2 er: {var2}")

    if liste[1] == "+":
        sendthis =  var1 + var2
        print(f"this was sendt {sendthis}")
        print(b"{sendthis}")
        conn.send(b"{sendthis}")
        liste = []
    else:
        sendit = var1 * var2
        print(f"this was sendt {sendit}")
        conn.send(b"{sendit}")
        liste= []

# conn.close()