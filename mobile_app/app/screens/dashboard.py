from kivy.uix.screenmanager import Screen
from kivymd.toast import toast


class DashboardScreen(Screen):

    def refresh_dashboard(self):
        toast("Dashboard Updated")