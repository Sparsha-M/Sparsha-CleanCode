# -*- coding: utf-8 -*-
from __future__ import print_function

from h_basket import *

if __name__ == "__main__":
    print("OMGHAI!")
    items = [
        Item(name="Tooth brush", sell_in=10, quality=20),
        Item(name="Indian Wine", sell_in=2, quality=0),

        Item(name="Forest Honey", sell_in=0, quality=80),
        Item(name="Forest Honey", sell_in=-1, quality=80),
        Item(name="Movie Tickets", sell_in=15, quality=20),
        Item(name="Movie Tickets", sell_in=10, quality=49),
        Item(name="Movie Tickets", sell_in=5, quality=49),
        # <-- :O
    ]

    days = 2
    import sys

    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        HamaraBasket(items).update_quality()
