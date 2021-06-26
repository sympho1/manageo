from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from connection import create_connection, create_user, create_table
from db import database, User
from pony import orm
from kivy.app import App

class RegisterScreen(Screen):
    pass

    @orm.db_session
    def user_register(self, *args):
        # conn = create_connection("user.db")
        nom = self.ids.nom_id.text
        email = self.ids.email_id.text
        pwd = self.ids.pass_id.text
        confirm_pwd = self.ids.confirm_pass_id.text
        if nom == "" or email == "" or pwd == "" or confirm_pwd == "":
            print('erreur')
        else:
            User(name = nom, email = email, password = pwd)
            orm.commit()
            self.ids.nom_id.text = ""
            self.ids.email_id.text = ""
            self.ids.pass_id.text = ""
            print(nom, email, pwd, confirm_pwd)
            appli = App.get_running_app()
            appli.sm.current = "login"
       
    
Builder.load_file("pages/register.kv")