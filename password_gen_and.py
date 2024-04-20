from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from random import choice, randint, shuffle
import pyperclip
import string

class PasswordManager(GridLayout):
    def __init__(self, **kwargs):
        super(PasswordManager, self).__init__(**kwargs)
        self.cols = 2
        self.spacing = [10, 10]
        self.padding = [20, 20, 20, 20]  # [padding_left, padding_top, padding_right, padding_bottom]

        self.add_widget(Label(text="Website:"))
        self.website_entry = TextInput(multiline=False)
        self.add_widget(self.website_entry)

        self.add_widget(Label(text="Email/Username:"))
        self.email_entry = TextInput(multiline=False)
        self.add_widget(self.email_entry)

        self.add_widget(Label(text="Password:"))
        self.password_entry = TextInput(multiline=False)
        self.add_widget(self.password_entry)

        self.add_widget(Button(text="Generate Password", on_press=self.generate_password))
        self.add_widget(Button(text="Add", on_press=self.save))
        self.add_widget(Button(text="Copy Password", on_press=self.copy_password))

    def generate_password(self, instance):
        numbers = [str(i) for i in range(10)]
        c_letters = list(string.ascii_uppercase)
        s_letters = list(string.ascii_lowercase)
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '<', '>', ',', '.', '/', '?']

        c_letter = [choice(c_letters) for i in range(randint(4,5))]
        s_letter = [choice(s_letters) for i in range(randint(4,5))]
        p_number = [choice(numbers) for i in range(randint(2,4))]
        p_symbol = [choice(symbols) for i in range(randint(2,4))]

        p_list = c_letter + s_letter + p_number + p_symbol
        shuffle(p_list)

        password = "".join(p_list)
        self.password_entry.text = password
        pyperclip.copy(password)

    def copy_password(self, instance):
        password = self.password_entry.text
        if password:
            pyperclip.copy(password)
            popup = Popup(title='Password Copied', content=Label(text='Password copied to clipboard!'), size_hint=(None, None), size=(300, 200))
            popup.open()
        else:
            popup = Popup(title='No Password', content=Label(text='No password to copy!'), size_hint=(None, None), size=(300, 200))
            popup.open()

    def save(self, instance):
        website = self.website_entry.text
        email = self.email_entry.text
        password = self.password_entry.text

        if len(website)==0 or len(password)==0:
            popup = Popup(title='Oops', content=Label(text='Please enter the correct info.'), size_hint=(None, None), size=(300, 200))
            popup.open()
        else:
            message = f"These are the details entered:\nEmail: {email}\nPassword: {password}\n\nIs it ok to save?"
            popup = Popup(title=website, content=Label(text=message), size_hint=(None, None), size=(400, 300))
            popup.open()
            # You can add saving functionality here

class PasswordManagerApp(App):
    def build(self):
        return PasswordManager()

if __name__ == '__main__':
    PasswordManagerApp().run()
