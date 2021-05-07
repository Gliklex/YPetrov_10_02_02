import pytest
from task_10_02_02_terminal import *

def test_terminal_str():
    assert Терминал().__str__() == "Пицерилло #1 \nДобро пожаловать!"