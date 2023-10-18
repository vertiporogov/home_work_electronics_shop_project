import pytest

from src.keyboard import Keyboard

@pytest.fixture
def test_keyboard():
    return Keyboard('aser', 100.0, 5)


def test_keyboard_name(test_keyboard):
    assert test_keyboard.name == 'aser'


def test_keyboard_lang(test_keyboard):
    assert test_keyboard.language == 'EN'


def test_keyboard_change_lang(test_keyboard):
    test_keyboard.change_lang()
    assert test_keyboard.language == 'RU'
