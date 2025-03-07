import unittest
from unittest.mock import MagicMock

from h_basket import Item, HamaraBasket, IndianWine, ForestHoney, MovieTickets, DefaultItem


class HamaraBasketTest(unittest.TestCase):
    def setUp(self):
        self.qualityRuleEngine = None

    def InitSingleItemList(self, name, sell_by, quality):
        if name == "Indian Wine":
            items = [IndianWine(name, sell_by, quality)]
        elif name == "Forest Honey":
            items = [ForestHoney(name, sell_by, quality)]
        elif name == "Movie Tickets":
            items = [MovieTickets(name, sell_by, quality)]
        else:
            items = [DefaultItem(name, sell_by, quality)]

        self.qualityRuleEngine = HamaraBasket(items)
        return items[0]

    # interaction test
    def test_should_update_quality_for_all_items_intentionally_failed(self):
        # should fail
        item = MagicMock()
        items = [item]
        self.qualityRuleEngine = HamaraBasket(items)
        self.qualityRuleEngine.update_quality()
        item.update_quality.assert_not_called()  # update_quality is called once but I'm checking
        # whether it's not called

    def test_should_update_quality_for_all_items(self):
        # should pass
        item = MagicMock()
        items = [item]
        self.qualityRuleEngine = HamaraBasket(items)
        self.qualityRuleEngine.update_quality()
        item.update_quality.assert_called_once()

    # functional test
    def test_should_reduce_quality_by_one(self):
        item = self.InitSingleItemList("lux soap", 10, 20)
        self.qualityRuleEngine.update_quality()
        self.assertEqual(19, item.quality)

    def test_should_not_reduce_quality_for_generic_products_when_quality_is_zero(self):
        item = self.InitSingleItemList("T V", 10, 0)
        self.qualityRuleEngine.update_quality()
        self.assertEqual(0, item.quality)

    def test_should_not_reduce_quality_for_generic_products_when_quality_is_less_than_zero_defect(self):
        item = self.InitSingleItemList("T V", 10, -10)
        self.qualityRuleEngine.update_quality()
        self.assertEqual(-10, item.quality)

    def test_should_reset_to_fifty_and_reduce_by_one_for_generic_products_when_quality_is_greater_than_fifty_defect(
            self):
        item = self.InitSingleItemList("T V", 10, 54)
        self.qualityRuleEngine.update_quality()
        self.assertEqual(53, item.quality)

    def test_should_reduce_for_generic_product_sell_by_value_by_one(self):
        item = self.InitSingleItemList("lux soap", 10, 0)
        self.qualityRuleEngine.update_quality()
        self.assertEqual(9, item.sell_in)

    def test_should_reduce_by_two_for_quality_value_for_generic_products_when_sell_by_degrades(self):
        item = self.InitSingleItemList("Phone", -1, 40)
        self.qualityRuleEngine.update_quality()
        self.assertEqual(38, item.quality)

    def test_should_increase_by_one_for_indian_wine_when_sell_by_is_older(self):
        item = self.InitSingleItemList("Indian Wine", 30, 30)
        self.qualityRuleEngine.update_quality()
        self.assertEqual(31, item.quality)

    def test_should_increase_by_two_for_indian_wine_when_sell_by_is_zero_or_less_than_zero(self):
        item = self.InitSingleItemList("Indian Wine", 0, 40)
        self.qualityRuleEngine.update_quality()
        self.assertEqual(42, item.quality)

    def test_should_remain_fifty_for_indian_wine_when_sell_by_is_zero_and_quality_is_greater_than_fifty_defect(self):
        item = self.InitSingleItemList("Indian Wine", 0, 51)
        self.qualityRuleEngine.update_quality()
        self.assertEqual(51, item.quality)

    def test_should_remain_zero_for_indian_wine_when_sell_by_is_zero_and_quality_is_lesser_than_zero_defect(self):
        item = self.InitSingleItemList("IndianWine", 0, -10)
        self.qualityRuleEngine.update_quality()
        self.assertEqual(-10, item.quality)

    def test_should_increase_by_one_for_forest_honey_when_sell_by_is_older(self):
        item = self.InitSingleItemList("Forest Honey", 30, 30)
        self.qualityRuleEngine.update_quality()
        self.assertEqual(30, item.quality)

    def test_should_remain_fifty_for_forest_honey_when_sell_by_is_zero_and_quality_is_greater_than_fifty_defect(self):
        item = self.InitSingleItemList("Forest Honey", 0, 51)
        self.qualityRuleEngine.update_quality()
        self.assertEqual(51, item.quality)

    def test_should_remain_zero_for_forest_honey_when_sell_by_is_zero_and_quality_is_lesser_than_zero_defect(self):
        item = self.InitSingleItemList("Forest Honey", 0, -10)
        self.qualityRuleEngine.update_quality()
        self.assertEqual(-10, item.quality)

    def test_should_increase_by_one_for_movie_tickets_when_sell_by_is_older(self):
        item = self.InitSingleItemList("Movie Tickets", 30, 30)
        self.qualityRuleEngine.update_quality()
        self.assertEqual(31, item.quality)

    def test_should_increase_by_two_for_movie_tickets_when_sell_by_is_older(self):
        item = self.InitSingleItemList("Movie Tickets", 10, 30)
        self.qualityRuleEngine.update_quality()
        self.assertEqual(32, item.quality)

    def test_should_increase_by_three_for_movie_tickets_when_sell_by_is_zero_or_less_than_zero(self):
        item = self.InitSingleItemList("Movie Tickets", 5, 30)
        self.qualityRuleEngine.update_quality()
        self.assertEqual(33, item.quality)


if __name__ == '__main__':
    unittest.main()
