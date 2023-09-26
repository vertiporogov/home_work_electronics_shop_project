"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest

@pytest.fixture
def test_item():
    return Item('fff', 100.0, 2)
def test_item_init(test_item):
    assert test_item.name == 'fff'
    assert test_item.price == 100.0
    assert test_item.quantity == 2
    # assert 100 * 0.1 == 10

def test_apply_discount(test_item):
    test_item.pay_rate = 0.5
    test_item.apply_discount()
    assert test_item.price == 50.0

def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 200.0

