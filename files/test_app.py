# test_app.py

from app import Figure

def test_app_triangle():
    """Тестуємо створення фігури трикутник."""
    fig = "трикутник"
    triangle = Figure(fig, 4)
    assert triangle.type == fig, f"Фігура має бути {fig}"

def test_get_angles():
    """Тестуємо чи правильно повертається кількість кутів."""
    fig = "трикутник"
    triangle = Figure(fig, 1)
    assert triangle.get_angles == 3, f"У {fig} є 3 кути!"
