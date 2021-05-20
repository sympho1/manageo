from kivy.app import App
from pages.register import RegisterScreen
from pages.login import LoginScreen
from kivy.uix.screenmanager import ScreenManager, Screen


class Manageo(App):
    sm = ScreenManager()
    def build(self):
        # self.title = "Lambert" add title
        self.sm.add_widget(LoginScreen(name="login"))
        self.sm.add_widget(RegisterScreen(name="register"))
        return self.sm

if __name__ == "__main__":
    Manageo().run()