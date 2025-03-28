def read_file(path: str) -> list[str]:
    with open(path, 'r') as file:
        rows = file.readlines()

    return rows

def write_file(data: list[str], path: str):
    with open(path, '2') as file:
        file.writelines(data)