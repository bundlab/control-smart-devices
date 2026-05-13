from kivy.uix.screenmanager import Screen
from kivymd.toast import toast


class LoginScreen(Screen):

    def login(self, username, password):

        if username == "admin" and password == "admin":
            self.manager.current = "dashboard"
            toast("Login Successful")
        else:
            toast("Invalid Credentials")