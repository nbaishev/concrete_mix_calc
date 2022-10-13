from controller import Controller
from model import Model
from view import View


class App:
    model = Model('15', '32.5', '200', '0.5', '2.66', '2.66')
    view = View()
    controller = Controller(model, view)
    view.set_controller(controller) 
    view.mainloop()

if __name__ == '__main__':
    app = App()