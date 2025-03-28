import pytest
import main
import subprocess

@pytest.fixture
def sample_file(tmp_path):
    content = ["line1\n", "line2\n", "line3\n"]
    file_path = tmp_path / "sample.txt"
    file_path.write_text("".join(content))
    return file_path, content

def test_read_file(sample_file):
    file_path, content = sample_file
    result = main.read_file(str(file_path))
    assert result == content

@pytest.fixture
def temp_output_file(tmp_path):
    return tmp_path / "output.txt"

@pytest.mark.parametrize("data", [
    (["hello\n", "world\n"]),
    (["foo\n", "bar\n", "baz\n"])
])
def test_write_file(temp_output_file, data):
    main.write_file(data, str(temp_output_file))
    read_data = temp_output_file.read_text().splitlines(keepends=True)
    assert read_data == data

@pytest.mark.parametrize("lines, filter_word, expected", [
    (["apple pie\n", "banana smoothie\n", "apple tart\n", "cherry cake\n"], "apple", ["apple pie\n", "apple tart\n"]),
    (["one\n", "two\n", "three\n"], "two", ["two\n"]),
    (["hello world\n", "goodbye world\n"], "world", ["hello world\n", "goodbye world\n"]),
    (["hello\n", "goodbye\n"], "missing", [])
])
def test_filter_lines(lines, filter_word, expected):
    result = main.filter_lines(lines, filter_word)
    assert result == expected

@pytest.mark.parametrize("input_path, expected", [
    ("/home/user/input.txt", "/home/user/filtered.txt"),
    ("input.txt", "filtered.txt"),
    ("./dir/test.txt", "./dir/filtered.txt")
])
def test_generate_output_path(input_path, expected):
    output_path = main.generate_output_path(input_path)
    assert output_path == expected


def test_pep8_compliance():
    result = subprocess.run(
        ["flake8", "--exclude=.venv,__pycache__,venv", "main.py"],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0, f"PEP8 style errors:\n{result.stdout}"