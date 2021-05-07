import pytest
from task_10_02_02_order import Заказ
from task_10_02_02_pizza import ПиццаБарбекю, ПиццаПепперони, ПиццаДарыМоря


def pizza_order(pizza_list):
    order = Заказ()
    for pizza in pizza_list:
        order.добавить(pizza)
    return order


test_str_test_data = [(Заказ(), f"Заказ №{Заказ.счетчик_заказов+3}\n\nСумма заказа: 0"),
                      (pizza_order([ПиццаБарбекю()]),
                       f"Заказ №{Заказ.счетчик_заказов+2}\n1. {ПиццаБарбекю().__str__()}\n"
                       f"\nСумма заказа: 450"),

                      (pizza_order([ПиццаБарбекю(), ПиццаПепперони()]),
                       f"Заказ №{Заказ.счетчик_заказов+1}\n1. {ПиццаБарбекю().__str__()}\n"
                       f"2. {ПиццаПепперони().__str__()}\n\nСумма заказа: 800"),

                      (pizza_order([ПиццаБарбекю(), ПиццаПепперони(), ПиццаДарыМоря()]),
                       f"Заказ №{Заказ.счетчик_заказов}\n1. {ПиццаБарбекю().__str__()}\n"
                       f"2. {ПиццаПепперони().__str__()}\n"
                       f"3. {ПиццаДарыМоря().__str__()}\n\nСумма заказа: 1350")
                      ]


@pytest.mark.parametrize("order, expected_str", test_str_test_data)
def test_str(order, expected_str):
    assert order.__str__() == expected_str
