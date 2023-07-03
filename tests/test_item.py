"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest
test = Item("ttt", 100.0, 10)
def test_calculate_total_price():
    t = test.price
    v = test.quantity
    assert t * v == 1000.0
    # assert 100 * 0.1 == 10

# def test_apply_discount():
#
#     assert 2000 * 0.8 == 1600
#     # assert 2000 * 2 == 4000