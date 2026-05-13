from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from screens.login import LoginScreen
from screens.dashboard import DashboardScreen
from screens.devices import DevicesScreen
from screens.rooms import RoomsScreen
from screens.automation import AutomationScreen
from screens.analytics import AnalyticsScreen
from screens.profile import ProfileScreen


class SmartControlApp(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        Builder.load_file("../ui/login.kv")
        Builder.load_file("../ui/dashboard.kv")
        Builder.load_file("../ui/devices.kv")
        Builder.load_file("../ui/rooms.kv")
        Builder.load_file("../ui/automation.kv")
        Builder.load_file("../ui/analytics.kv")
        Builder.load_file("../ui/profile.kv")

        sm = ScreenManager()

        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(DevicesScreen(name="devices"))
        sm.add_widget(RoomsScreen(name="rooms"))
        sm.add_widget(AutomationScreen(name="automation"))
        sm.add_widget(AnalyticsScreen(name="analytics"))
        sm.add_widget(ProfileScreen(name="profile"))

        return sm


SmartControlApp().run()