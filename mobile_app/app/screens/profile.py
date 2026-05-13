from kivy.uix.screenmanager import Screen


class ProfileScreen(Screen):

    def logout(self):
        self.manager.current = "login"