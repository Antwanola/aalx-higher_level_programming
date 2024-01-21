#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    if num == 1:
        print("{} arguments.".format(num - 1))
    elif num == 2:
        print(f"{num - 1} arguments")
    else:
        print(f"{num - 1} argument")
    for n in range(1, num):
        print(f"{num - 1} {sys.argv[n]}")
