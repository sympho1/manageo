from kivy.app import App
from pages.register import RegisterScreen
from pages.login import LoginScreen
from pages.home import HomeScreen
from kivy.uix.screenmanager import ScreenManager, Screen


class Manageo(App):
    sm = ScreenManager()
    def build(self):
        self.title = "Manageo"
        self.sm.add_widget(LoginScreen(name="login"))
        self.sm.add_widget(RegisterScreen(name="register"))
        self.sm.add_widget(HomeScreen(name="home_screen"))
        return self.sm

if __name__ == "__main__":
    Manageo().run()