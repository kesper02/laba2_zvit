from figure import Figure  # а не app

def main():
    # Введення даних
    a = input("Введіть число: ")
    assert a.isdigit(), "Потрібно ввести число!"  # Перевірка, чи введено число
    print(f"Введене число: {a}")

    # Створення фігур
    f1 = Figure("квадрат", 5)
    f2 = Figure("трикутник", 10)

    # Виведення результатів
    print(f"Тип фігури: {f1.get_figure_type()}")
    print(f"Довжина фігури: {f2.get_figure_length()}")

if __name__ == "__main__":
    main()
