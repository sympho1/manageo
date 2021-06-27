from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from db import database, User
from pony import orm
from kivy.app import App


class LoginScreen(Screen):
   pass

   @orm.db_session
   def user_login(self, *args):
      email = self.ids.email_id.text
      pwd = self.ids.pass_id.text
      if email == "" or pwd == "":
         print('erreur')
         
      else:
         # fichier = open("../inscription.db")
         # (p for p in User)

         for i in User.select():
            # print(User.select().show())
            if email == i.email and pwd == i.password:
               appli = App.get_running_app()
               appli.sm.current = "home_screen"
            else:
               print('ff')
            
            

Builder.load_file("pages/login.kv")