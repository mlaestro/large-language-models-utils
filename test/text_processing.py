from collections.abc import Iterator

from src.text_processing.reading_utils import FileReader

def test_reading_plain_text():
    dir_path = "dummy_data"
    file_name = "text_file_1.txt"

    data_loader = FileReader(dir_path, file_name)
    text = data_loader.get_full_text()
    ## basic one line file
    assert type(text) == str
    assert text == "Hello world"

    file_name = "text_file_2.txt"
    data_loader = FileReader(dir_path, file_name)
    text = data_loader.get_full_text()
    assert type(text) == str
    assert text == "Hello, world!\nThis is a\nmultiline\nfile."

    file_name = "text_file_3.txt"
    data_loader = FileReader(dir_path, file_name)
    text = data_loader.get_full_text()
    assert type(text) == str
    assert len(text) == 0


def test_get_single_line_text():
    dir_path = "dummy_data"
    file_name = "text_file_1.txt"

    data_loader = FileReader(dir_path, file_name)
    text = data_loader.get_single_line()
    ## basic one line file
    assert isinstance(text, Iterator)
    assert list(text) == ["Hello world"]

    file_name = "text_file_2.txt"
    data_loader = FileReader(dir_path, file_name)
    text = data_loader.get_single_line()
    assert isinstance(text, Iterator)
    assert list(text) == ["Hello, world!", "This is a", "multiline", "file."]

    file_name = "text_file_3.txt"
    data_loader = FileReader(dir_path, file_name)
    text = data_loader.get_single_line()
    assert isinstance(text, Iterator)
    assert len(list(text)) == 0