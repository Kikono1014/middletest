import pytest
import main


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