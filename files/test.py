# test.py
import unittest  # Імпортуємо модуль для тестування
from figure import Figure  # Імпортуємо клас Figure для тестування

class TestFigure(unittest.TestCase):
    
    def test_figure_type(self):
        # Тестуємо, чи правильний тип фігури
        f = Figure("квадрат", 5)
        self.assertEqual(f.get_figure_type(), "квадрат")  # Перевіряємо, чи тип фігури "квадрат"
    
    def test_figure_length(self):
        # Тестуємо, чи правильна довжина фігури
        f = Figure("трикутник", 10)
        self.assertEqual(f.get_figure_length(), 10)  # Перевіряємо, чи довжина фігури 10

if __name__ == '__main__':
    unittest.main()  # Запуск тестів
