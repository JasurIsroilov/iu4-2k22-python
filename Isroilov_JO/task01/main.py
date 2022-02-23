import sys

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def main(args: list):

    res = list([])
    status = 1
    s = args[1]

    if len(args[0]) > 1:
        print("Incorrect status input")
        sys.exit(-1)
    elif not args[2].isnumeric():
        print("Incorrect step input")
        sys.exit(-1)

    if args[0] == 'd':
        status = -1

    mod = int(args[2]) * status

    for sym in s:
        if sym in alphabet:
            tmp = alphabet.find(sym)
            new_mod = (tmp + mod) % len(alphabet)
            res.append(alphabet[new_mod])
        else:
            print("Prohibited message input")
            sys.exit(-1)

    msg = "".join(res)
    print(msg)


if __name__ == '__main__':
    main(sys.argv)
