from commit import commit
from confirm import confirm


def handshake():
    sA, sB, eA, eB, kck = commit()
    check = confirm(sA, sB, eA, eB, kck)

    print(check)

    sA, sB, eA, eB, kck = commit()
    check = confirm(sA, sB, eA, eB, kck)

    print(check)

def main():
    handshake()


if __name__ == "__main__":
    main()
