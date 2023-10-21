import pytest

from src.error import InstantiateCSVError
from src.item import Item


@pytest.fixture
def test_item():
    return Item('fff', 100.0, 2)


# test_item.instantiate_from_csv()

def test_instantiate_from_csv_error(test_item):
    with pytest.raises(InstantiateCSVError):
        test_item.instantiate_from_csv()


def test_instantiate_from_csv_not_found(test_item):
    with pytest.raises(FileNotFoundError):
        test_item.instantiate_from_csv()
