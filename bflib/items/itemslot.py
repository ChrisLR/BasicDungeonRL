class ItemSlot(object):
    __slots__ = ("keyword", "item")

    def __init__(self, keyword):
        self.keyword = keyword
        self.item = None
