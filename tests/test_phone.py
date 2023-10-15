from src.item import Item
from src.phone import Phone
import pytest


@pytest.fixture
def test_item():
    return Item('fff', 100.0, 2)


@pytest.fixture
def test_phone():
    return Phone('aaa', 200.0, 10, 2)


def test_item_add(test_item, test_phone):
    assert test_item + test_phone == 12


def test_item_repr(test_phone):
    assert repr(test_phone) == "Phone('aaa', 200.0, 10, 2)"


def test_item_str(test_phone):
    assert str(test_phone) == 'aaa'


def test_number_of_sim(test_phone):
    assert test_phone.number_of_sim == 2

    with pytest.raises(ValueError):
        test_phone.number_of_sim = 0
