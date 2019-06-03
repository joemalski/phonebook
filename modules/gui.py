# Filename: app.py
# Date: June 3, 2019
# Description: Gui Object Class
# By: Joel F. Malinao

class GuiObject:

    def __init__(self, h, w, text):
        self.h = h
        self.w = w
        self.text = text

    # width center with offset
    def w_center(self, offset=0):
        return (self.w // 2) + offset

    # width center of texting
    def w_center_text(self, offset=0):
        return (self.w_center() - self.text_len_half()) + offset

    # height center with offset
    def h_center(self, offset=0):
        return (self.h // 2) + offset

    # texting length
    def text_len(self):
        return len(self.text)

    # half of texting's length
    def text_len_half(self):
        return len(self.text) // 2

    # center position with offset
    def center_coor(self, w_offset=0, h_offset=0):
        h = (self.h_center()) + h_offset
        w = (self.w_center() - self.text_len_half()) + w_offset
        return (h, w)