import sys



def watchdog():
    return sys.gettrace() is None

def build():
    data = [102, 108, 97, 103, 123, 114, 97, 109, 117, 107, 97, 105, 110, 111, 115, 125]
    return "".join(chr(x) for x in data)

def core():
    if watchdog():
        return None
    return build()

def main():
    out = core()
    if out:
        print("handoff token:")
        print(out)

if __name__ == "__main__":
    main()
