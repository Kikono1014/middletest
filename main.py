import sys

def read_file(path: str) -> list[str]:
    with open(path, 'r') as file:
        rows = file.readlines()

    return rows

def write_file(data: list[str], path: str):
    with open(path, '2') as file:
        file.writelines(data)

def filter_lines(lines: list[str], filter_word: str) -> list[str]:
    filtered = list(filter(lambda line: filter_word in line, lines))
    return filtered

def generate_output_path(input_path: str) -> str:
    extension_id = input_path.find(".txt")
    name_id = input_path.rfind("/")

    output_path = input_path[:(name_id+1)]      \
                    + "filtered"                \
                    + input_path[extension_id:] \

    return output_path



if __name__ == "__main__":
    input_path = sys.argv[1]
    filter_word = sys.argv[2]

    lines = read_file(input_path)

    filtered = filter_lines(lines, filter_word)
    output_path = generate_output_path(input_path)

    write_file(filtered, output_path)