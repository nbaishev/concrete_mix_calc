from model import Model
from view import View


class Controller:
    '''
    Связь интерфейса и модели.
    '''

    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def save(self, concrete: str, cement: str,
             water: str, proportion: str,
             sand_density: str, rubber_density: str,):
        """
        Сохранять результаты расчета.
        """
        try:
            self.model.concrete = concrete
            self.model.cement = cement
            self.model.water = water
            self.model.proportion = proportion
            self.model.sand_density = sand_density
            self.model.rubber_density = rubber_density

            self.model.calculate()

            self.view.show_success('Файл сохранен')

        except ValueError as error:
            self.view.show_error(error)
