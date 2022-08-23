from math import ceil

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection_length = len(collection)
        self.items_per_page = items_per_page
        self.pages = [collection[items_per_page * i:items_per_page * (i + 1)] 
                      for i in range(ceil(len(collection)/items_per_page))]

    # returns the number of items within the entire collection
    def item_count(self):
        return self.collection_length

    # returns the number of pages
    def page_count(self):
        return len(self.pages)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index not in range(len(self.pages)):
            return -1
        return len(self.pages[page_index])

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index == 0 and self.collection_length > 0:
            return 0
        if item_index not in range(self.collection_length):
            return -1
        return ceil(item_index / self.items_per_page - 1)


helper = PaginationHelper(['a','b','c','d','e','f'], 4)
print(helper.pages)
print(helper.item_count())
print(helper.page_count())
print(helper.page_item_count(0))
print(helper.page_item_count(1))
print(helper.page_item_count(2))
print(helper.page_index(5))
print(helper.page_index(2))
print(helper.page_index(20))
print(helper.page_index(0))
print(helper.page_index(-1))