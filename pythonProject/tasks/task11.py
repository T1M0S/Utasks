import tkinter as tk

from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk


def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2

        messagebox.showinfo("Результат", "Результат: " + str(result))
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числа.")


def show_selections():
    selected_options = []

    if checkbox1_var.get():
        selected_options.append("первый вариант")
    if checkbox2_var.get():
        selected_options.append("второй вариант")
    if checkbox3_var.get():
        selected_options.append("третий вариант")

    messagebox.showinfo("Выбранные варианты", f"Вы выбрали: {', '.join(selected_options)}")


def open_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, "r") as file:
        file_contents = file.read()
        text.delete(1.0, tk.END)
        text.insert(tk.END, file_contents)


# Создание основного окна приложения
app = tk.Tk()
app.title("Кутькин Роман Александрович Ум-232")

# Создание вкладок
tab_control = tk.ttk.Notebook(app)

# Первая вкладка - калькулятор
tab1 = tk.Frame(tab_control)
tab_control.add(tab1, text="Калькулятор")

operator_var = tk.StringVar(tab1)
operator_var.set("+")

label1 = tk.Label(tab1, text="Первое число:")
label1.pack()

entry1 = tk.Entry(tab1)
entry1.pack()

label2 = tk.Label(tab1, text="Второе число:")
label2.pack()

entry2 = tk.Entry(tab1)
entry2.pack()

operator_dropdown = tk.OptionMenu(tab1, operator_var, "+", "-", "*", "/")
operator_dropdown.pack()

calculate_button = tk.Button(tab1, text="Выполнить", command=calculate)
calculate_button.pack()

# Вторая вкладка - чекбоксы
tab2 = tk.Frame(tab_control)
tab_control.add(tab2, text="Чекбоксы")

checkbox1_var = tk.BooleanVar()
checkbox2_var = tk.BooleanVar()
checkbox3_var = tk.BooleanVar()

checkbox1 = tk.Checkbutton(tab2, text="Первый", variable=checkbox1_var)
checkbox1.pack()

checkbox2 = tk.Checkbutton(tab2, text="Второй", variable=checkbox2_var)
checkbox2.pack()

checkbox3 = tk.Checkbutton(tab2, text="Третий", variable=checkbox3_var)
checkbox3.pack()

show_selections_button = tk.Button(tab2, text="Показать выбранные варианты", command=show_selections)
show_selections_button.pack()

# Третья вкладка - работа с текстом
tab3 = tk.Frame(tab_control)
tab_control.add(tab3, text="Работа с текстом")

menu = tk.Menu(app)
app.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Открыть", command=open_file)

text = tk.Text(tab3)
text.pack()

# Отображение вкладок
tab_control.pack(expand=1, fill="both")

# Запуск основного цикла приложения
app.mainloop()
