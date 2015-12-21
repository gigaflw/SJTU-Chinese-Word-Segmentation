"""Code responsible for GUI interface"""
from tkinter import *


class DemoView:
    def __init__(self):
        # Root window
        self.root = Tk()
        self.root.title("Y")

        # Three main text pads
        self.raw_text_pad = Text()
        self.sen_text_pad = Listbox()
        self.wrd_text_pad = Text()

        self.set_text_pad()
        self.make_menu()
        self.make_button()

    def run(self):
        self.root.mainloop()

    def make_menu(self):
        main_menu=Menu(self.root)

        #file_menu
        file_menu=Menu(main_menu)
        file_menu.add_command(label="New",accelerator="Ctrl+N")
        file_menu.add_command(label="Open",accelerator="Ctrl+O")
        file_menu.add_command(label="Open Recent")
        file_menu.add_separator()
        file_menu.add_command(label="Save",accelerator="Ctrl+S")
        file_menu.add_command(label="Save As")
        file_menu.add_separator()
        file_menu.add_command(label="Export")
        file_menu.add_command(label="Exit",accelerator="Ctrl+Q")

        #edit_menu
        edit_menu=Menu(main_menu)
        edit_menu.add_command(label="Undo",accelerator="Ctrl+Z")
        edit_menu.add_command(label="Redo",accelerator="Shift+Ctrl+Z")
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut",accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy",accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste",accelerator="Ctrl+V")
        edit_menu.add_command(label="Find_All",accelerator="Ctrl+F",command=self.find_all)

        #segment_menu
        segment_menu=Menu(main_menu)
        segment_menu.add_command(label="Segment")
        segment_menu.add_command(label="File to file")

        #lexicon_menu
        lexicon_menu=Menu(main_menu)
        lexicon_menu.add_command(label="Load")
        lexicon_menu.add_command(label="Add")
        lexicon_menu.add_command(label="Modify")
        lexicon_menu.add_command(label="Delete")

        #rule_menu
        rule_menu=Menu(main_menu)
        rule_menu.add_command(label="Rule",command=self.rule)

        #help_menu
        help_menu=Menu(main_menu)
        help_menu.add_command(label="Help",command=self.help)
        help_menu.add_command(label="About",command=self.about)

        #main_menu
        main_menu.add_cascade(label="File",menu=file_menu)
        main_menu.add_cascade(label="Edit",menu=edit_menu)
        main_menu.add_cascade(label="Segment",menu=segment_menu)
        main_menu.add_cascade(label="Lexicon",menu=lexicon_menu)
        main_menu.add_cascade(label="Rule",menu=rule_menu)
        main_menu.add_cascade(label="Help",menu=help_menu)

        self.root.configure(menu=main_menu)

    def find_all():
        pass

    def rule():
        pass

    def help():
        pass

    def about():
        pass


    def set_text_pad(self):
        """This function setting the properties of raw_text_pad,sen_text_pad and wrd_text_pad"""
        # setting raw_text_pad
        self.raw_text_pad = Text(self.root)
        self.raw_text_pad.pack()

        # setting sen_text_pad
        self.sen_text_pad = Listbox(self.root)
        self.sen_text_pad.pack()

        # setting wrd_text_pad
        self.wrd_text_pad = Text(self.root)
        self.wrd_text_pad.pack()



    def make_button(self):
        # Buttons
        btn1 = Button(self.root, text="seb_seg")
        btn2 = Button(self.root, text="wor_seg")

        btn1.configure(command=self.__sen_seg)
        btn2.configure(command=self.__wrd_seg)

        btn1.pack(side='left', expand=True)
        btn2.pack(side='left', expand=True)

    # Following functions involves conversation with controller
    def register(self, controller):
        """Make connection with controller"""
        self.controller = controller

    def __sen_seg(self):
        # Get the unprocessed variable
        before = self.raw_text_pad.get('1.0', END)

        # Get the sentence-segmentation function provided by controller
        seg = self.controller.sentence_segment
        # Do sentence segmentation
        after = seg(before)
        # Renew variable
        self.sen_text_pad.insert('end', after)

    def __wrd_seg(self):
        seg = self.controller.word_segment
        after_wrd_seg = seg(self.sen_text_pad.get('1.0', END))
        self.wrd_text_pad.insert('1.0', END, after_wrd_seg)

    def __read_file(self):
        s = self.raw_text_pad.get('1.0', END)
        s.set(self.controller.read_file(s.get()))


if __name__ == '__main__':
    t = DemoView()
    t.run()