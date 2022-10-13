import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    '''
    Пользовательский интерфейс.
    '''
    def __init__(self):
        super().__init__()

        self.title('Расчет подбора состава бетона')

        for i in range(2):
            self.columnconfigure(index=i, weight=1,)
        for i in range(9):
            self.rowconfigure(index=i, weight=1,)

        self.label_top = ttk.Label(self,
                                   text='Укажите необходимые данные',)
        self.label_top.grid(columnspan=2, row=0,)

        self.label_concrete = ttk.Label(self,
                                        text='Класс бетона',)
        self.label_concrete.grid(column=0, row=1,)

        self.label_cement = ttk.Label(self,
                                      text='Марка цемента',)
        self.label_cement.grid(column=0, row=2,)

        self.label_water = ttk.Label(self,
                                     text='Расход воды',)
        self.label_water.grid(column=0, row=3,)

        self.label_sand = ttk.Label(self,
                                    text='Истинная плотность песка',)
        self.label_sand.grid(column=0, row=4,)

        self.label_rubble = ttk.Label(self,
                                      text='Средняя плотность щебня',)
        self.label_rubble.grid(column=0, row=5,)

        self.label_proportion = ttk.Label(self,
                                          text='Соотношение заполнителей',)
        self.label_proportion.grid(column=0, row=6,)

        self.combo_concrete = ttk.Combobox(self,
                                           values=[
                                            '15',
                                            '20',
                                            '25',
                                            '30', ],)
        self.combo_concrete.grid(column=1, row=1,)
        self.combo_concrete.current(0)

        self.combo_cement = ttk.Combobox(self,
                                         values=[
                                            '32.5',
                                            '42.5',
                                            '52.5', ],)
        self.combo_cement.grid(column=1, row=2,)
        self.combo_cement.current(0)

        self.entry_water = ttk.Entry(self)
        self.entry_water.grid(column=1, row=3,)
        self.entry_water.insert(0, "200")

        self.entry_sand = ttk.Entry(self)
        self.entry_sand.grid(column=1, row=4,)
        self.entry_sand.insert(0, "2.6")

        self.entry_rubber = ttk.Entry(self)
        self.entry_rubber.grid(column=1, row=5)
        self.entry_rubber.insert(0, "2.6")

        self.entry_proportion = ttk.Entry(self)
        self.entry_proportion.grid(column=1, row=6)
        self.entry_proportion.insert(0, "0.5")

        self.save_button = ttk.Button(text='Рассчитать',
                              command=self.save_button_clicked,)

        self.save_button.grid(columnspan=2, row=7)

        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(columnspan=2, row=8,)

        self.controller = None

    def set_controller(self, controller) -> None:
        """
        Установить контроллер.
        """
        self.controller = controller

    def save_button_clicked(self) -> None:
        """
        Обработать событие нажатия на кнопку сохранить.
        """
        if self.controller:
            self.controller.save(self.combo_concrete.get(),
                                 self.combo_cement.get(),
                                 self.entry_water.get(),
                                 self.entry_proportion.get(),
                                 self.entry_sand.get(),
                                 self.entry_rubber.get(),)

    def show_error(self, message: str) -> None:
        """
        Показать сообщение об ошибке.
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)

    def show_success(self, message: str) -> None:
        """
        Показать сообщение об успешном выполнении.
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

    def hide_message(self) -> None:
        """
        Скрыть сообщение.
        """
        self.message_label['text'] = ''
