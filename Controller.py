"""Code responsible for application logic"""
import tkinter as tk
from View import DemoView

import hgs_part


class MainController:
    """The main controller of app activity"""
    def __init__(self):
        self.root = tk.Tk()
        self.view = DemoView(self.root)
        self.view.register(self)
        self.model = hgs_part.Segmentation()

    def run(self):
        self.root.mainloop()

    @staticmethod
    def read_file(filename: str) -> str:
        """
        This function opens a file according to its name,and return its context.
        If can't open with 'utf-8',try 'gbk',
        since 'gbk' always opens a file even if open it as error codes

        Questions:
        1.Error message should not be only print!
        2.Not tested yet
        """

        context = ""
        try:
            with open(filename, "r", encoding='utf') as f:
                context = f.read()
        except IOError:
            print("Can't find file!")
        except UnicodeDecodeError:
            with open(filename, "r", encoding='utf') as f:
                context = f.read()
        return context

    def sentence_segment(self, raw: str) -> list:
        """
        This function receive complete long string from View,
        ask for Model to do sentence segmentation,
        return processed string list to View.

        Only called by View.

        Examples:
        >>> c = MainController()
        >>> c.sentence_segment("你好，再见。")
        ["你好，","再见。"]

        QUESTIONS:
        1.Does the list contain punctuation at the end of each sentence?
        2.Can it recognize both Chinese and English punctuations?
        """
        return self.model.sentence_segment(raw)

    def word_segment(self, sentence: str) -> str:
        """
        This function receive a sentence from View,
        ask for Model to do word segmentation,
        return processed string to View.

        Only called by View.

        Examples:
        >>> c = MainController()
        >>> c.word_segment("我喜欢踢足球")
        "我｜喜欢｜踢|足球"

        QUESTIONS:
        1.What should be the separator character?
        """
        return self.model.word_segment(sentence)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
