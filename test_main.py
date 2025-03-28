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

