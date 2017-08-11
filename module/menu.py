import inquirer
import sys

class MenuBase(object):
    def base(self, menu_name, menu_message, menu_parameter):
        questions = [
            inquirer.List(menu_name,
                message = menu_message,
                choices = menu_parameter
            ),
        ]
        answers = inquirer.prompt(questions)
        return answers[menu_name]


class SubMenu(MenuBase):
    def __init__(self, menu_params = None, response = None):
        from network import request
        if response != None:
            if response['code'] == 302:
                option = super(SubMenu, self).base('Person', 'Choose a person <3', menu_params)
                request.initialize_conversation(option)
            else:
                self.OptionForMenu()
        else:
            self.OptionForMenu()

    def OptionForMenu(self):
        from network import request
        option = super(SubMenu, self).base('Menu', 'Hi and welcome!.', ['Login', 'Register'])
        options = {
            'login': request.login(),
            'register': request.register(),
            'quit': sys.exit()
        }
        options[option]

