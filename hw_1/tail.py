import sys

def print_last_lines(lines, count):
    for line in lines[-count:]:
        print(line, end='')

def main():
    if len(sys.argv) > 1:
        file_paths = sys.argv[1:]
        for file_path in file_paths:
            try:
                with open(file_path, 'r') as file:
                    lines = file.readlines()
            except FileNotFoundError:
                print(f"tail: {file_path}: No such file or directory", file=sys.stderr)
                continue

            if len(file_paths) > 1:
                print(f"==> {file_path} <==")

            print_last_lines(lines, 10)

            if file_path != file_paths[-1]:
                print()
    else:
        lines = sys.stdin.readlines()
        print_last_lines(lines, 17)

if __name__ == "__main__":
    main()
