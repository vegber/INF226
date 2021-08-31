from pwn import *

file = 'files_to_diss/pwnexercise'

conn = remote('158.39.77.181', 6001)
tekst = conn.recv(1024)
# receive password tekst
print(tekst)
conn.send(b'infA')
# send password

# remove all the pre tekst
first = conn.recv(94)
print(first)

def do_stuff(tall1, matteting, tall2):
    print(f"tall1 {tall1}, matte {matteting} tall2 {tall2}")
    if matteting == "+":
        return str(int(tall1) + int(tall2)) + "\n"
    else:
        return str(int(tall1) * int(tall2))+ "\n"


while (True):
    get_all = conn.recv(1024)
    print(get_all)
    get_all_as_string = get_all.decode()
    sequence = []
    sequence.append(re.sub("[^0-9*+]=?", " ", x) for x in get_all_as_string)
    var = list("".join(sequence[0]).split(" "))
    number = []
    char = []
    for x in var:
        if x.isdigit():
            number.append(x)
        if x == "+" or x == "*":
            char.append(x)
    calculated = do_stuff(number[0], char[0], number[1]).encode()
    print(calculated)
    conn.send(calculated)
