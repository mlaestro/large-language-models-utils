from src.text_processing import reading_utils

def test_reading_plain_text():
    file_path = "../dummy_data/sample_text.txt"
    data_loader = reading_utils.FileReader(file_path)
    text = data_loader.get_full_text()
    assert type(text) == str
    assert text == ""
