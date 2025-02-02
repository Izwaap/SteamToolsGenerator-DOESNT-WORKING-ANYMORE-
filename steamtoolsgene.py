import tkinter as tk
from tkinter import messagebox
import webbrowser

# Функция для обработки ввода и вывода ссылки
def process_input():
    user_input = entry.get()

    # Проверка, что введены только цифры
    if not user_input.isdigit():
        messagebox.showerror("Ошибка", "Пожалуйста, вводите только ID игры.")
        return

    # Пример формирования ссылки
    link = f"https://cysaw.top/uploads/{user_input}.zip"

    # Показ ссылки пользователю
    result_label.config(text=f"Скачать", fg="blue", cursor="hand2")
    result_label.bind("<Button-1>", lambda e: webbrowser.open(link))

# Создание окна приложения
root = tk.Tk()
root.title("SteamToolsLinkGenerator")
root.geometry("400x300")
root.configure(bg="#ffffff")

# Заголовок
header_label = tk.Label(root, text="Введите ID игры для генерации ссылки", font=("Arial", 16), bg="#ffffff", pady=10)
header_label.pack()

# Поле ввода
def on_entry_click(event):
    if entry.get() == "Введите число...":
        entry.delete(0, tk.END)  # Удаляем текст по умолчанию
        entry.config(fg="black")  # Меняем цвет текста на черный

entry = tk.Entry(root, font=("Arial", 14), width=30, fg="grey")
entry.insert(0, "Введите число...")
entry.bind("<FocusIn>", on_entry_click)  # Привязываем обработчик события
entry.pack(pady=10)

# Кнопка подтверждения
button = tk.Button(root, text="Получить ссылку", command=process_input, font=("Arial", 12), bg="#3abda3", fg="white", activebackground="#5f9ea0", activeforeground="white", relief="raised")
button.pack(pady=10)

# Место для отображения результата
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f8ff")
result_label.pack(pady=10)

# Подпись для пользователя
label_footer = tk.Label(root, text="Для работы требуется Steam Tools", font=("Arial", 10), fg="gray", bg="#f0f8ff")
label_footer = tk.Label(root, text="Если у вас ничего не скачалось значит не существует данного ID", font=("Arial", 10), fg="gray", bg="#ffffff")
label_footer.pack(pady=20)
label_footer.pack(pady=20)

# Запуск приложения
root.mainloop()