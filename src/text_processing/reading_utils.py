import os


class FileReader:
    def __init__(self, dir_path:str, file_path:str, encoding="utf-8", type="raw"):
        """
        :param dir_path: Directory path
        :param file_path: path of the text file
        :param encoding: encoding of the text file
        :param type: html/json/raw, currently only supports raw
        """
        self.dir_path = dir_path
        self.file_path = file_path
        self.encoding = encoding
        self.type = type

    def get_full_text(self) -> str:
        if not os.path.exists(self.dir_path):
            raise FileNotFoundError(f"Directory {self.dir_path} does not exist")
        full_path = os.path.join(self.dir_path, self.file_path)
        if not os.path.exists(full_path):
            raise FileNotFoundError("File does not exist")
        try:
            with open(full_path, encoding=self.encoding) as f:
                text = f.read()
            return text
        except UnicodeDecodeError:
            raise UnicodeDecodeError(f"File {self.file_path} does not contain utf-8")
        finally:
            f.close()

    def get_single_line(self):
        """

        :return:
        """

        if not os.path.exists(self.dir_path):
            raise FileNotFoundError(f"Directory {self.dir_path} does not exist")
        full_path = os.path.join(self.dir_path, self.file_path)
        if not os.path.exists(full_path):
            raise FileNotFoundError("File does not exist")
        try:
            with open(full_path, encoding=self.encoding) as f:
                for line in f:
                    yield line.strip()
        except UnicodeDecodeError:
            raise UnicodeDecodeError(f"File {self.file_path} does not contain utf-8")
        finally:
            f.close()

class WebReader:
    ## TODO: Add utilities for reading directly from web
    pass
