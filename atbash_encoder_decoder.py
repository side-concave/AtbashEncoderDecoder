def encode_decode(message):
    for letter in message:
        if 'a' in letter:
            print('z')
        elif 'b' in letter:
            print('y')
        elif 'c' in letter:
            print('x')
        elif 'd' in letter:
            print('w')
        elif 'e' in letter:
            print('v')
        elif 'f' in letter:
            print('u')
        elif 'g' in letter:
            print('t')
        elif 'h' in letter:
            print('s')
        elif 'i' in letter:
            print('r')
        elif 'j' in letter:
            print('q')
        elif 'k' in letter:
            print('p')
        elif 'l' in letter:
            print('o')
        elif 'm' in letter:
            print('n')
        elif 'n' in letter:
            print('m')
        elif 'o' in letter:
            print('l')
        elif 'p' in letter:
            print('k')
        elif 'q' in letter:
            print('j')
        elif 'r' in letter:
            print('i')
        elif 's' in letter:
            print('h')
        elif 't' in letter:
            print('g')
        elif 'u' in letter:
            print('f')
        elif 'v' in letter:
            print('e')
        elif 'w' in letter:
            print('d')
        elif 'x' in letter:
            print('c')
        elif 'y' in letter:
            print('b')
        elif 'z' in letter:
            print('a')

message = (input('\nWhat is the meessage you want to encode\decode?\n'))
message = message.lower()
encode_decode(message)