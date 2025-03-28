import sys

def read_file(path: str) -> list[str]:
    if not isinstance(path, str):
        raise TypeError("path must be a string")
    
    with open(path, 'r') as file:
        rows = file.readlines()

    return rows

def write_file(data: list[str], path: str):
    if not isinstance(data, list) or not all(isinstance(line, str) for line in data):
        raise TypeError("data must be a list of strings")
    if not isinstance(path, str):
        raise TypeError("path must be a string")
    
    with open(path, 'w') as file:
        file.writelines(data)

def filter_lines(lines: list[str], filter_word: str) -> list[str]:
    if not isinstance(lines, list) or not all(isinstance(line, str) for line in lines):
        raise TypeError("lines must be a list of strings")
    if not isinstance(filter_word, str):
        raise TypeError("filter_word must be a string")
    
    filtered = list(filter(lambda line: filter_word in line, lines))
    return filtered

def generate_output_path(input_path: str) -> str:
    if not isinstance(input_path, str):
        raise TypeError("input_path must be a string")
    
    extension_id = input_path.find(".txt")
    name_id = input_path.rfind("/")

    output_path = input_path[:(name_id+1)]      \
                    + "filtered"                \
                    + input_path[extension_id:] \

    return output_path



if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise ValueError("must provide arguments for path and filter_word")

    input_path = sys.argv[1]
    filter_word = sys.argv[2]

    lines = read_file(input_path)

    filtered = filter_lines(lines, filter_word)
    output_path = generate_output_path(input_path)

    write_file(filtered, output_path)