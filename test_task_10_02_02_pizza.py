import pytest
from task_10_02_02_pizza import *


test_str_test_data = [(ПиццаПепперони(), f"Пицца: Пепперони | цена: 350.00 р."
                                         f" \n   Тесто: тонкое Соус: кетчуп \n   Начинка: пепперони, сыр моцарелла"),

                      (ПиццаБарбекю(), f"Пицца: Барбекю | цена: 450.00 р."
                                       f" \n   Тесто: тонкое Соус: барбекю \n   Начинка: бекон, ветчина, зелень,"
                                       f" сыр моцарелла"),

                      (ПиццаДарыМоря(), f"Пицца: ДарыМоря | цена: 550.00 р."
                                        f" \n   Тесто: тонкое Соус: Тар-тар \n   Начинка: кальмары, креветки,"
                                        f" мидии, сыр моцарелла")
                      ]


@pytest.mark.parametrize("pizza, expected_str", test_str_test_data)
def test_pizza_str(pizza, expected_str):
    assert pizza.__str__() == expected_str