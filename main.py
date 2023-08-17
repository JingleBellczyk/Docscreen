# base Class of your App inherits from the App class.
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


# GridLayout arranges children in a matrix.
# Label is used to label something
# used to take input from users


class LoginScreen(GridLayout):
    def __init__(self, **var_args):
        super(LoginScreen, self).__init__(**var_args)

        #make screen
        button = Button(text='Make screenshot', font_size=20,size=(200,200), pos=(400,400))
        button.bind(on_press=self.button_act)
        self.add_widget(button)

        #close window
        but_close = Button(text="Close",font_size=20,size=(200,200), pos=(400,200))
        but_close.bind(on_press=self.close_application)
        self.add_widget(but_close)

    def close_application(self,instace):
        # closing application
        App.get_running_app().stop()

    def button_act(self, instance):
        print("button was clicked")


# the Base Class of our Kivy App
class MyApp(App):
    def build(self):
        # return a LoginScreen() as a root widget
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
