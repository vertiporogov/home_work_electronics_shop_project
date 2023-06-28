"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest

def test_calculate_total_price():

    assert 100 * 10 == 1000


def test_apply_discount():

    assert 2000 * 0.8 == 1600