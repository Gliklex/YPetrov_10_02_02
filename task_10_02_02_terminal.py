# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_10_02_02.
#
# Выполнил: Фамилия И.О.
# Группа: !!!
# E-mail: !!!


import task_10_02_02_order as заказ
import task_10_02_02_pizza as пицца


# Уберите raise и добавьте необходимый код - импортируйте необходимые модули

class Терминал:
    """Класс Терминал обеспечивает взаимодействие с клиентом."""

    КОМПАНИЯ = "Пицерилло"
    КОМАНДА_ОТМЕНА_ЗАКАЗА = -1
    КОМАНДА_ПОДТВЕРЖДЕНИЕ_ЗАКАЗА = 0

    def __init__(self):
        """Конструктор класса.

        self.меню: список доступных пицц;
        self.заказ: список заказанных пицц;
        self.отображать_меню: определяет отображение меню
                              равен True: при создании терминала,
                              после отмены или подтверждения заказа.
        """
        # Доступные пиццы
        self.меню = [пицца.ПиццаПепперони(), пицца.ПиццаБарбекю(), пицца.ПиццаДарыМоря()]
        self.заказ = None
        self.отображать_меню = True

    def __str__(self):
        """Вернуть строковое представление класса.

        Формат вывода:

        Имя пиццерии, версия программы.
        """
        return "{} #1 \nДобро пожаловать!".format(self.КОМПАНИЯ)
        # Уберите raise и добавьте необходимый код

    def показать_меню(self):
        """Показать меню.

        Показать меню следует только при наличии флага self.отображать_меню
        self.отображать_меню устанавливается в False после вывода меню.

        Формат вывода:

        Пиццерия #1
        Добро пожаловать!

        Меню:
        1. Пицца: Пепперони | Цена: 350.00 р.
           Тесто: тонкое Соус: томатный
           Начинка: пепперони, сыр моцарелла
        2. Пицца: Барбекю | Цена: 450.00 р.
           Тесто: тонкое Соус: барбекю
           Начинка: бекон, ветчина, зелень, сыр моцарелла
        3. Пицца: Дары моря | Цена: 550.00 р.
           Тесто: пышное Соус: тар-тар
           Начинка: кальмары, креветки, мидии, сыр моцарелла
        Для выбора укажите цифру через <ENTER>.
        Для отмены заказа введите -1
        Для подтверждения заказа введите 0
        """
        if not self.отображать_меню:
            return
        self.отображать_меню = False
        return print(f"Меню: \n1. {self.меню[0].__str__()}\n2. {self.меню[1].__str__()}\n3. {self.меню[2].__str__()}"                     
                     f" \nДля выбора укажите цифру через <ENTER>."
                     f"\nДля отмены заказа введите -1"
                     f"\nДля подтверждения заказа введите 0")

        # Уберите raise и добавьте необходимый код

    def обработать_команду(self, пункт_меню):
        """Обработать действие пользователя.

        Аргументы:
          - пункт_меню (str): выбор пользователя.

        Возможные значения "пункт_меню":
          - -1: отменить заказ;
          -  0: подтвердить заказ; при этом осуществляется
                выставление счета, оплата, а также выполняется заказ;
                после заказ удаляется (= None)
          - 1..len(self.меню): добавление пиццы к добавить_к_заказу;
                               если заказ не создан, его нужно создать.
          - иначе: сообщить о невозможности обработать команду.

        Каждое действие подтверждается выводом на экран, например:
        1
        Пицца Пепперони добавлена!
        2
        Пицца Барбекю добавлена!
        0
        Заказ подтвержен.
        """

        try:
            пункт_меню = int(пункт_меню)
            if пункт_меню == Терминал.КОМАНДА_ОТМЕНА_ЗАКАЗА:
                if self.заказ is not None:
                    self.заказ = None
                    return print("Отмена заказа")
                # Уберите raise и добавьте необходимый код
                # Проверьте, что отмена вызывается для созданного заказа
            elif пункт_меню == Терминал.КОМАНДА_ПОДТВЕРЖДЕНИЕ_ЗАКАЗА: #!!!!
                if self.заказ is not None:
                    print("Заказ подтвержден")
                    print(self.заказ)
                    self.рассчитать_сдачу(self.принять_оплату())
                    self.заказ.выполнить()
                    self.заказ = None
                else:
                    return Терминал.КОМАНДА_ОТМЕНА_ЗАКАЗА, print("Отмена заказа")
                # Уберите raise и добавьте необходимый код
                # Проверьте, что подтверждение вызывается для созданного заказа
                # При возникновении ошибки необходимо вызвать команду
                # отмены заказа
            elif 1 <= пункт_меню <= len(self.меню):
                if self.заказ is None:
                    self.заказ = заказ.Заказ()
                self.заказ.добавить(self.меню[пункт_меню-1])
                return self.заказ, print(f"Пицца {self.меню[пункт_меню-1].название} добавлена!")
                # Уберите raise и добавьте необходимый код
                # Если заказ не создан, его нужно предварительно создать
            else:
                # За границей меню передаем управление в обработку исключений
                raise ValueError
        except ValueError:
            print("Не могу распознать команду! Проверьте ввод.")
        except Exception:
            print("Во время работы терминала произошла ошибка...")

    def рассчитать_сдачу(self, оплата):
        """Вернуть сдачу для 'оплата'.

        Если оплата меньше стоимости заказа, возбудить исключение ValueError.
        """
        if оплата < self.заказ.сумма():
            raise ValueError("Сумма недостаточна для оплаты")
        else:
            sdacha = оплата - self.заказ.сумма()
        return print(f"Вы ввели {оплата:.2f}р, ваша сдача {sdacha:.2f}р")
        # Уберите raise и добавьте необходимый код

    def принять_оплату(self):
        """Обработать оплату.

        Эмулирует оплату заказа (клиент вводит сумму с клавиатуры).

        Если сумма оплаты недостаточна (определяет метод рассчитать_сдачу())
        или возникает другая ошибка - исключние передается выше.
        """
        try:
            оплата = int(input("Введите сумму: "))
            if оплата < self.заказ.сумма():
                raise ValueError("Сумма недостаточна для оплаты")
            return оплата
        except Exception:
            print("Оплата не удалась. Заказ будет отменен.")
            raise
