import tkinter as tk
from tkinter import messagebox
import webbrowser

# Словари для хранения текстов на разных языках
texts = {
    "ru": {
        "title": "SteamToolsLinkGenerator",
        "header": "Введите ID игры для генерации ссылки",
        "entry_default": "Введите ID игры...",
        "button": "Получить ссылку",
        "result": "Скачать",
        "footer1": "Для работы требуется Steam Tools",
        "footer2": "Если у вас ничего не скачалось значит не существует данного ID",
        "error": "Ошибка",
        "error_message": "Пожалуйста, вводите только ID игры."
    },
    "en": {
        "title": "SteamToolsLinkGenerator",
        "header": "Enter the game ID to generate a link",
        "entry_default": "Enter Game ID...",
        "button": "Get link",
        "result": "Download",
        "footer1": "Steam Tools is required to work",
        "footer2": "If nothing was downloaded, this ID does not exist",
        "error": "Error",
        "error_message": "Please enter only the game ID."
    }
}

# Текущий язык
current_language = "en"

# Функция для обработки ввода и вывода ссылки
def process_input():
    user_input = entry.get()

    # Проверка, что введены только цифры
    if not user_input.isdigit():
        messagebox.showerror(texts[current_language]["error"], texts[current_language]["error_message"])
        return

    # Пример формирования ссылки
    link = f"https://cysaw.top/uploads/{user_input}.zip"

    # Показ ссылки пользователю
    result_label.config(text=texts[current_language]["result"], fg="blue", cursor="hand2")
    result_label.bind("<Button-1>", lambda e: webbrowser.open(link))

# Функция для переключения языка
def switch_language():
    global current_language
    if current_language == "ru":
        current_language = "en"
    else:
        current_language = "ru"
    update_ui()

# Функция для обновления текста интерфейса
def update_ui():
    root.title(texts[current_language]["title"])
    header_label.config(text=texts[current_language]["header"])
    entry.delete(0, tk.END)
    entry.insert(0, texts[current_language]["entry_default"])
    entry.config(fg="grey")
    button.config(text=texts[current_language]["button"])
    result_label.config(text="")
    label_footer1.config(text=texts[current_language]["footer1"])
    label_footer2.config(text=texts[current_language]["footer2"])

# Создание окна приложения
root = tk.Tk()
root.title(texts[current_language]["title"])
root.geometry("400x300")
root.configure(bg="#ffffff")

# Заголовок
header_label = tk.Label(root, text=texts[current_language]["header"], font=("Arial", 16), bg="#ffffff", pady=10)
header_label.pack()

# Поле ввода
def on_entry_click(event):
    if entry.get() == texts[current_language]["entry_default"]:
        entry.delete(0, tk.END)  # Удаляем текст по умолчанию
        entry.config(fg="black")  # Меняем цвет текста на черный

entry = tk.Entry(root, font=("Arial", 14), width=30, fg="grey")
entry.insert(0, texts[current_language]["entry_default"])
entry.bind("<FocusIn>", on_entry_click)  # Привязываем обработчик события
entry.pack(pady=10)

# Кнопка подтверждения
button = tk.Button(root, text=texts[current_language]["button"], command=process_input, font=("Arial", 12), bg="#3abda3", fg="white", activebackground="#5f9ea0", activeforeground="white", relief="raised")
button.pack(pady=10)

# Место для отображения результата
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f8ff")
result_label.pack(pady=10)

# Подпись для пользователя
label_footer1 = tk.Label(root, text=texts[current_language]["footer1"], font=("Arial", 10), fg="gray", bg="#ffffff")
label_footer1.pack(pady=5)

label_footer2 = tk.Label(root, text=texts[current_language]["footer2"], font=("Arial", 10), fg="gray", bg="#ffffff")
label_footer2.pack(pady=5)

# Кнопка для переключения языка
switch_language_button = tk.Button(root, text="Русский/English", command=switch_language, font=("Arial", 10), bg="#f0f8ff", fg="black")
switch_language_button.pack(pady=10)

# Запуск приложения
root.mainloop()