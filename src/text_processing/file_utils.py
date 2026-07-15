import json
import os

import ijson


class FileReader:
    def __init__(self, dir_path:str, file_path:str, encoding="utf-8"):
        """
        :param dir_path: Directory path
        :param file_path: path of the text file
        :param encoding: encoding of the text file
        :param type: html/json/raw, currently only supports raw
        """
        self.dir_path = dir_path
        self.file_path = file_path
        self.encoding = encoding

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


class JSONReader(FileReader):
    """

    """
    def __init__(self, dir_path:str, file_path:str, encoding="utf-8",top_key:str=None, text_keys:list=None, label_keys:list=None):
        """

        :param dir_path: path of directory
        :param file_path: path of the JSON file
        :param encoding: type of encoding of the JSON file
        :param text_keys: the keys containing text
        :param label_keys: the keys containing labels
        """
        super().__init__(dir_path, file_path, encoding)
        self.top_key = top_key
        self.text_keys = text_keys
        self.label_keys = label_keys


    def get_all_items(self):
        """

        :return: full text of the file in form of dictionary
        """
        if not os.path.exists(self.dir_path):
            raise FileNotFoundError(f"Directory {self.dir_path} does not exist")
        full_path = os.path.join(self.dir_path, self.file_path)
        if not os.path.exists(full_path):
            raise FileNotFoundError("File does not exist")
        try:
            with open(full_path, encoding=self.encoding) as f:
                data_dict = json.load(f)
            return data_dict
        except UnicodeDecodeError:
            raise UnicodeDecodeError(f"File {self.file_path} does not contain utf-8")

    def get_single_item(self):
        """

        :return: return one item at a time
        """
        if not os.path.exists(self.dir_path):
            raise FileNotFoundError(f"Directory {self.dir_path} does not exist")
        full_path = os.path.join(self.dir_path, self.file_path)
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"File {full_path} does not exist")
        try:
            with open(full_path, "rb") as file:
                # 'item' targets individual elements inside a root array [ {}, {}, {} ]
                parser = ijson.items(file, self.top_key)
                for item in parser:
                    yield item
        except UnicodeDecodeError:
            raise UnicodeDecodeError(f"File {self.file_path} does not contain utf-8")


