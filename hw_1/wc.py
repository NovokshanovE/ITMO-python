import sys

def count_words_lines_bytes(content):
    lines = content.count('\n')
    words = len(content.split())
    bytes_count = len(content.encode('utf-8'))
    return lines, words, bytes_count

def print_stats(file_path, lines, words, bytes_count):
    print(f"{lines} {words} {bytes_count} {file_path}")

def main():
    total_lines = total_words = total_bytes = 0
    file_count = len(sys.argv) - 1

    if file_count > 0:
        for file_path in sys.argv[1:]:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
            except FileNotFoundError:
                print(f"wc: {file_path}: No such file or directory", file=sys.stderr)
                continue

            lines, words, bytes_count = count_words_lines_bytes(content)
            print_stats(file_path, lines, words, bytes_count)

            total_lines += lines
            total_words += words
            total_bytes += bytes_count

        if file_count > 1:
            print(f"{total_lines} {total_words} {total_bytes} total")
    else:
        content = sys.stdin.read()
        lines, words, bytes_count = count_words_lines_bytes(content)
        print(f"{lines}\t{words}\t{bytes_count}")

if __name__ == "__main__":
    main()
