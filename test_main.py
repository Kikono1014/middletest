import pytest



def test_read_file(tmp_path):
    file_content = ["line1\n", "line2\n", "line3\n"]
    file_path = tmp_path / "test.txt"
    file_path.write_text("".join(file_content))
    
    result = main.read_file(str(file_path))
    assert result == file_content