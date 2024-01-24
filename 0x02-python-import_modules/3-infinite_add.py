#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_content = sys.argv[1:]
    result = sum(int(n) for n in arg_content)
    print(result)
