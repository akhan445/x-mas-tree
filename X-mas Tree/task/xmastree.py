def check_and_validate_input():
    while True:
        try:
            nums = input().strip().split()

            total_nums = len(nums)

            if total_nums == 2:
                return {
                    "type": "tree",
                    "data": [int(nums[0]), int(nums[1])]
                }
            elif total_nums % 4 == 0:
                data = []
                for i in range(0, total_nums, 4):
                    H = int(nums[i])
                    I = int(nums[i + 1])
                    L = int(nums[i + 2])
                    C = int(nums[i + 3])

                    data.append([H, I, L, C])

                return {
                    "type": "postcard",
                    "data": data
                }
            else:
                continue
        except ValueError:
            continue

def create_postcard_template():
    postcard = []
    HEIGHT, WIDTH = 30, 50

    for x in range(HEIGHT):
        if x == 0 or x == HEIGHT - 1:
            line = list("-" * WIDTH)
            postcard.append(line)
        elif x == 27:
            spaces = " " * ((WIDTH - 12) // 2)
            line = list("|" + spaces + "Merry Xmas" + spaces + "|")
            postcard.append(line)
        else:
            line = list("|" + (" " * (WIDTH - 2)) + "|")
            postcard.append(line)

    return postcard

def create_tree(height, interval):
    tree = []
    counter = 0

    for i in range(height):
        if i == 0:
            x_top = list(" " * (height - 1 - i) + "X")
            tree.append(x_top)

            line = list(" " * (height - 1 - i) + "^")
            tree.append(line)
        else:
            slash_pos = " " * (height - 1 - i) + "/"
            inner = list("*" * (i * 2 - 1))

            for j in range(1, len(inner), 2):
                if counter % interval == 0:
                    inner[j] = "O"

                counter += 1

            line = list(slash_pos + ''.join(inner) + "\\")

            tree.append(line)

    stem = list(" " * (len(tree[0]) - 2) + "| |")
    tree.append(stem)

    return tree

def add_trees_to_postcard(postcard, data):
    for tree_info in data:
        H = tree_info[0]
        I = tree_info[1]
        L = tree_info[2]
        C = tree_info[3]

        tree = create_tree(H, I)

        for x in range(len(tree)):
            for y in range(len(tree[x])):
                if x + L >= 30 or y + C - H + 1 >= 50:
                    continue
                elif tree[x][y] != " ":
                    postcard[x + L][y + C - H + 1] = tree[x][y]


def print_to_console(data):
    for line in data:
        print(''.join(line))


def main():

    user_input = check_and_validate_input()
    match user_input["type"]:
        case "tree":
            height, interval = user_input["data"][0], user_input["data"][1]
            tree = create_tree(height, interval)
            print_to_console(tree)
        case "postcard":
            postcard = create_postcard_template()
            add_trees_to_postcard(postcard, user_input["data"])
            print_to_console(postcard)

if __name__ == "__main__":
    main()
