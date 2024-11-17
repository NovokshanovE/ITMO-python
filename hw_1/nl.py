import sys

def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        with open(file_path, 'r') as file:
            lines = file.readlines()
    else:
        lines = sys.stdin.readlines()

    for index, line in enumerate(lines, start=1):
        print(f"{index} {line}", end='')

if __name__ == "__main__":
    main()
