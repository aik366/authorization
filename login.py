import customtkinter as ctk
from PIL import Image
from data.database import db_insert, login_exist, db_check
from CTkMessagebox import CTkMessagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("320x250+700+350")
app.title("Login Page")
app.resizable(False, False)


def segmented_button_callback(value):
    if value == "Авторизация":
        frame_login.pack(padx=10, pady=10, fill="both", expand=True)
        frame_register.pack_forget()
    elif value == "Регистрация":
        frame_login.pack_forget()
        frame_register.pack(padx=10, pady=10, fill="both", expand=True)


def show_password(entry, button):
    if entry.cget("show") == "*":
        entry.configure(show="")
        button.configure(image=hide_image)
    else:
        entry.configure(show="*")
        button.configure(image=show_image)


def register():
    if login_exist(entry_login_register.get()):
        segmented_button_callback("Регистрация")
        CTkMessagebox(title="Error", message="Такой логин уже существует")
        return
    if entry_login_register.get() == "" or entry_password_register.get() == "":
        segmented_button_callback("Регистрация")
        CTkMessagebox(title="Error", message="Заполните все поля")
        return
    if len(entry_password_register.get()) < 6:
        segmented_button_callback("Регистрация")
        CTkMessagebox(title="Error", message="Пароль должен быть не менее 6 символов")
        return
    db_insert(entry_login_register.get(), entry_password_register.get())
    entry_login_register.delete(0, "end")
    entry_password_register.delete(0, "end")
    button_register.focus_set()
    segmented_button_callback("Авторизация")
    segemented_button.set("Авторизация")
    entry_login.delete(0, "end")
    entry_password.delete(0, "end")
    entry_login.configure(placeholder_text="Логин")
    entry_password.configure(placeholder_text="Пароль")
    CTkMessagebox(title="Success", message="Регистрация прошла успешно")


def login():
    if db_check(entry_login.get(), entry_password.get()):
        segmented_button_callback("Авторизация")
        entry_login.delete(0, "end")
        entry_password.delete(0, "end")
        button_login.focus_set()
        CTkMessagebox(title="Success", message="Авторизация прошла успешно")
    else:
        CTkMessagebox(title="Error", message="Такого логина не существует\nИли неверный пароль")


segemented_button_var = ctk.StringVar(value="Авторизация")
segemented_button = ctk.CTkSegmentedButton(app, values=["Авторизация", "Регистрация"],
                                           command=segmented_button_callback,
                                           variable=segemented_button_var)
segemented_button.pack(padx=10, pady=(10, 0))
segemented_button.set("Авторизация")

frame_login = ctk.CTkFrame(app)
frame_login.pack(padx=10, pady=10, fill="both", expand=True)

label_login = ctk.CTkLabel(frame_login, text="Логин", height=40, font=("Arial", 16))
label_login.grid(row=0, column=0, padx=10, pady=20)

entry_login = ctk.CTkEntry(frame_login, placeholder_text="Логин", height=40, font=("Arial", 16))
entry_login.grid(row=0, column=1, pady=20, sticky="we")

label_password = ctk.CTkLabel(frame_login, text="Пароль", height=40, font=("Arial", 16))
label_password.grid(row=1, column=0, padx=10)

entry_password = ctk.CTkEntry(frame_login, show="*", placeholder_text="Пароль", height=40, font=("Arial", 16))
entry_password.grid(row=1, column=1, sticky="we")

show_image = ctk.CTkImage(Image.open("img/show.png"), size=(30, 30))
hide_image = ctk.CTkImage(Image.open("img/hide.png"), size=(30, 30))
log_image = ctk.CTkImage(Image.open("img/log.png"), size=(25, 25))
reg_image = ctk.CTkImage(Image.open("img/reg.png"), size=(25, 25))

button_show_password = ctk.CTkButton(frame_login, text="", height=30, width=30, image=show_image,
                                     command=lambda: show_password(entry_password, button_show_password))
button_show_password.grid(row=1, column=2, padx=10)

button_login = ctk.CTkButton(frame_login, text="     Войти", height=40, font=("Arial", 16), command=login,
                             image=log_image, anchor="w", width=160)
button_login.grid(row=2, column=1, pady=20, sticky="ew")

frame_register = ctk.CTkFrame(app)
frame_register.pack(padx=10, pady=10, fill="both", expand=True)

label_login_register = ctk.CTkLabel(frame_register, text="Логин", height=40, font=("Arial", 16))
label_login_register.grid(row=0, column=0, padx=10, pady=20)

entry_login_register = ctk.CTkEntry(frame_register, placeholder_text="Логин", height=40, font=("Arial", 16), )
entry_login_register.grid(row=0, column=1, pady=20, sticky="we")

label_password_register = ctk.CTkLabel(frame_register, text="Пароль", height=40, font=("Arial", 16))
label_password_register.grid(row=1, column=0, padx=10)

entry_password_register = ctk.CTkEntry(frame_register, show="*", placeholder_text="Пароль", height=40,
                                       font=("Arial", 16))
entry_password_register.grid(row=1, column=1, sticky="we")

button_show_password_register = ctk.CTkButton(frame_register, text="", height=30, width=30, image=show_image,
                                              command=lambda: show_password(entry_password_register,
                                                                            button_show_password_register))
button_show_password_register.grid(row=1, column=2, padx=10)

button_register = ctk.CTkButton(frame_register, text="Регистрация", height=40, font=("Arial", 16), image=reg_image,
                                command=register, anchor="w", width=160)
button_register.grid(row=2, column=1, pady=20, sticky="we")

if __name__ == '__main__':
    segmented_button_callback("Авторизация")
    app.mainloop()
