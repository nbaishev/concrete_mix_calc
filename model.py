class Model:
    '''
    Модель представления данных.
    '''

    def __init__(self, concrete: float, cement: float,
                 water: float, proportion: float, sand_density: float,
                 rubber_density: float) -> None:
        self.concrete = concrete
        self.cement = cement
        self.water = water
        self.proportion = proportion
        self.sand_density = sand_density
        self.rubber_density = rubber_density

    @property
    def concrete(self) -> float:
        return self.__concrete

    @concrete.setter
    def concrete(self, value: str):
        if self.is_number(value):
            self.__concrete = float(value)
        else:
            raise ValueError(f'Неправильное значение {value}')

    @concrete.getter
    def concrete(self):
        return self.__concrete

    @property
    def cement(self):
        return self.__cement

    @cement.setter
    def cement(self, value: str):
        if self.is_number(value):
            self.__cement = float(value)
        else:
            raise ValueError(f'Неправильное значение {value}')

    @cement.getter
    def cement(self):
        return self.__cement

    @property
    def water(self):
        return self.__water

    @water.setter
    def water(self, value: str):
        if self.is_number(value):
            self.__water = float(value)
        else:
            raise ValueError(f'Неправильное значение {value}')

    @water.getter
    def water(self):
        return self.__water

    @property
    def proportion(self):
        return self.__proportion

    @proportion.setter
    def proportion(self, value: str):
        if self.is_number(value):
            self.__proportion = float(value)
        else:
            raise ValueError(f'Неправильное значение {value}')

    @proportion.getter
    def proprtion(self):
        return self.__proportion

    @property
    def sand_density(self):
        return self.__sand_density

    @sand_density.setter
    def sand_density(self, value: str):
        if self.is_number(value):
            self.__sand_density = float(value)
        else:
            raise ValueError(f'Неправильное значение {value}')

    @sand_density.getter
    def sand_density(self):
        return self.__sand_density

    @property
    def rubber_density(self):
        return self.__rubber_density

    @rubber_density.setter
    def rubber_density(self, value: str):
        if self.is_number(value):
            self.__rubber_density = float(value)
        else:
            raise ValueError(f'Неправильное значение {value}')

    @rubber_density.getter
    def rubber_density(self):
        return self.__rubber_density

    def cement_water_proportion(self) -> float:
        '''
        Рассчитать цементно-водное отношение.
        '''
        CEM_MULTIPLIER_1: float = 0.06
        CEM_MULTIPLIER_2: float = 0.24
        CEM_ADDITION: float = 13
        CONCRETE_COEF: float = 1.305
        return ((float(self.concrete) * CONCRETE_COEF - CEM_MULTIPLIER_1
                * float(self.cement) + CEM_ADDITION) / (CEM_MULTIPLIER_2
                * float(self.cement) + CEM_ADDITION))

    def cement_consumption(self) -> float:
        '''
        Рассчитать расход цемента.
        '''
        return self.cement_water_proportion() * self.water

    def aggregate_volume(self) -> float:
        '''
        Рассчитать объем заполнителей.
        '''
        WATER_DENSITY: float = 1.0
        CEMENT_DENSITY: float = 3.1
        return (1000 - self.water / WATER_DENSITY
                - self.cement_consumption() / CEMENT_DENSITY)

    def sand_consumption(self) -> float:
        '''
        Рассчитать содержание песка.
        '''
        return self.aggregate_volume() * self.proportion * self.sand_density

    def rubber_consumption(self) -> float:
        '''
        Рассчитать содержание щебня.
        '''
        return (self.aggregate_volume() * (1 - self.proportion)
                * self.rubber_density)

    def calculate(self) -> None:
        '''
        Сохранить расчет в файл.
        '''
        CONCRETE_MIX_RECIPE: str = ('Цемент: {:.1f}; Щебень: {:.1f}; '
                                    'Песок: {:.1f}; Вода: {:.1f};\n')
        with open('mix_recipe.txt', 'a') as f:
            f.write(CONCRETE_MIX_RECIPE.format(Model.cement_consumption(self),
                                               Model.rubber_consumption(self),
                                               Model.sand_consumption(self),
                                               self.water))

    def is_number(self, string: str):
        '''
        Проверить является ли строка числом.
        '''
        try:
            float(string)
            return True
        except:
            return False
