# # -*- coding: utf-8 -*-
#
# class HamaraBasket(object):
#
#     def __init__(self, items):
#         self.items = items
#
#     def update_quality(self):
#         for item in self.items:
#             if item.name != "Indian Wine" and item.name != "Movie Tickets":
#                 if item.quality > 0:
#                     if item.name != "Forest Honey":
#                         item.quality = item.quality - 1
#             else:
#                 if item.quality < 50:
#                     item.quality = item.quality + 1
#                     if item.name == "Movie Tickets":
#                         if item.sell_in < 11:
#                             if item.quality < 50:
#                                 item.quality = item.quality + 1
#                         if item.sell_in < 6:
#                             if item.quality < 50:
#                                 item.quality = item.quality + 1
#             if item.name != "Forest Honey":
#                 item.sell_in = item.sell_in - 1
#             if item.sell_in < 0:
#                 if item.name != "Indian Wine":
#                     if item.name != "Movie Tickets":
#                         if item.quality > 0:
#                             if item.name != "Forest Honey":
#                                 item.quality = item.quality - 1
#                     else:
#                         item.quality = item.quality - item.quality
#                 else:
#                     if item.quality < 50:
#                         item.quality = item.quality + 1
#
#
# class Item:
#     def __init__(self, name, sell_in, quality):
#         self.name = name
#         self.sell_in = sell_in
#         self.quality = quality
#
#     def update_quality(self):
#         raise NotImplementedError("Subclasses should implement this method")

from typing import List

class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        raise NotImplementedError("Subclasses should implement this method")


class HamaraBasket:
    def __init__(self, items: List[Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()


class IndianWine(Item):
    def update_quality(self):
        if self.sell_in < 1 and self.quality < 50:
            self.quality += 2
        elif self.quality < 50 and self.sell_in > 1:
            self.quality += 1
        self.sell_in -= 1


class MovieTickets(Item):
    def update_quality(self):
        if self.quality < 50:
            if self.sell_in <= 0:
                self.quality = 0
            elif self.sell_in < 6:
                self.quality += 3
            elif self.sell_in < 11:
                self.quality += 2
            else:
                self.quality += 1
        self.sell_in -= 1


class ForestHoney(Item):
    def update_quality(self):
        # Implement specific behavior for Forest Honey if needed
        pass


class SoftDrinks(Item):
    def update_quality(self):
        # Implement specific behavior for Soft Drinks if needed
        pass


class DefaultItem(Item):
    def update_quality(self):
        if self.quality > 0:
            if self.sell_in <= 0 and self.quality > 1:
                self.quality -= 2
            else:
                self.quality -= 1
        self.sell_in -= 1
