def check_input():
    while True:
        try:
            height, interval = map(int, input().split())
            if height >= 3:
                return height, interval
            else:
                continue
        except ValueError:
            continue

def create_tree(height, interval):
    tree = []
    counter = 0

    for i in range(height):
        if i == 0:
            x_top = " " * (height - 1 - i) + "X"
            tree.append(x_top)

            line = " " * (height - 1 - i) + "^"
            tree.append(line)
        else:
            slash_pos = " " * (height - 1 - i) + "/"
            inner = list("*" * (i * 2 - 1))

            for j in range(1, len(inner), 2):
                if counter % interval == 0:
                    inner[j] = "O"

                counter += 1

            line = slash_pos + ''.join(inner) + "\\"

            tree.append(line)

    stem = " " * (len(tree[0]) - 2) + "| |"
    tree.append(stem)

    return tree

def print_tree(tree):
    for line in tree:
        print(line)


def main():
    height, interval = check_input()
    tree = create_tree(height, interval)
    print_tree(tree)

if __name__ == "__main__":
    main()
