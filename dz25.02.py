from tkinter import*
from tkinter import messagebox
import time

window = Tk()
window.title("Auto Clicker")
window.geometry("400x300")
window.configure(bg = "#def6fa")


running = False # змінна, що зберігатиме стан: програма зараз працює або ні
delay = 0 # змінна, що зберігатиме тривалість перерви після кожного кліку

clicks = Entry(window, width=40)
clicks.place(relx=0.5, rely=0.3, anchor="n")

def start_clicker():
    try:
        global running, delay  # "знаходимо" змінні, що існують поза функцією
        clicks_per_second = int(clicks.get())
        delay = 1 / clicks_per_second  # рахуємо затримку між кліками
        messagebox.showinfo("Auto Clicker", "Auto Clicker розпочинає роботу.")
        running = True
    except ValueError:
        messagebox.showerror("Помилка", "Напишіть число.")
        # я додала try/except

def schedule_click():
    if running:
        print("Клац!") # тут потім додамо клацання миші замість print
        time.sleep(delay) # затримка між кліками
        schedule_click() # функція знову викликає сама себе

def exit_app():
    window.destroy()
    # тут буде завершення програми


def show_info(event):
    messagebox.showinfo("Інформація", "Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!")


label1 = Label(window, text = "Auto Clicker", bg = "#def6fa", font = ("Arial 20 bold"),  fg = "#08827e")
label1.place(relx=0.5, rely=0.05, anchor="n")

label2 = Label(window, text = "Кліків на секунду:", bg = "#def6fa", font = ("Arial", 15),  fg = "#08827e")
label2.place(relx=0.5, rely=0.2, anchor="n")

def startbtn():
    print("Клацнуто кнопку 'Почати'.")

btn1 = Button(window, text = "Почати", command=start_clicker, bg = "#4baf4f", fg = "white", font = ("Arial", 13), height=2, width=10)
btn1.place(relx=0.35, rely=0.42, anchor="n")

btn2 = Button(window, text = "Вийти", command=exit_app, bg = "#f54035", fg = "white", font = ("Arial", 13), height=2, width=8)
btn2.place(relx=0.65, rely=0.42, anchor="n")

window.bind("i", show_info)

window.mainloop()