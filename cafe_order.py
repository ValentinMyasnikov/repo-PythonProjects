from tkinter import *


class Aplication(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text='Добро пожаловать в ресторан!').grid(row=0, column=0, sticky=W)
        Label(self, text='Выберете блюда на заказ').grid(row=1, column=0, sticky=W)
        self.dish_1 = BooleanVar()
        self.price_dish_1 = 10
        Checkbutton(self, text=f'Жареха, цена {self.price_dish_1} руб.', variable=self.dish_1,
                    command=self.update_text_dishes).grid(row=2, column=0, sticky=W)
        self.dish_2 = BooleanVar()
        self.price_dish_2 = 8
        Checkbutton(self, text=f'Солянка, цена {self.price_dish_2} руб.', variable=self.dish_2,
                    command=self.update_text_dishes).grid(row=3, column=0, sticky=W)
        self.dish_3 = BooleanVar()
        self.price_dish_3 = 7
        Checkbutton(self, text=f'Пельмени, цена {self.price_dish_3} руб.', variable=self.dish_3,
                    command=self.update_text_dishes).grid(row=4, column=0, sticky=W)
        self.dish_4 = BooleanVar()
        self.price_dish_4 = 3
        Checkbutton(self, text=f'Компот, цена {self.price_dish_4} руб.', variable=self.dish_4,
                    command=self.update_text_dishes).grid(row=5, column=0, sticky=W)
        self.dish_5 = BooleanVar()
        self.price_dish_5 = 3
        Checkbutton(self, text=f'Чай, цена {self.price_dish_5} руб.', variable=self.dish_5,
                    command=self.update_text_dishes).grid(row=6, column=0, sticky=W)
        self.dish_6 = BooleanVar()
        self.price_dish_6 = 2
        Checkbutton(self, text=f'Печенье, цена {self.price_dish_6} руб.', variable=self.dish_6,
                    command=self.update_text_dishes).grid(row=7, column=0, sticky=W)

        self.result_txt_dishes = Text(self, width=40, height=7, wrap=WORD)
        self.result_txt_dishes.grid(row=8, column=0, columnspan=3)

        Label(self, text='Выберете время доставки').grid(row=10, column=0, sticky=W)
        self.time = StringVar()
        self.time.set(None)
        Radiobutton(self, text='10.00-11.00', variable=self.time, value='10.00-11.00', command=self.update_text_delivery).grid(row=11, column=0, sticky=W)
        Radiobutton(self, text='11.00-12.00', variable=self.time, value='11.00-12.00', command=self.update_text_delivery).grid(row=12,
                                                                                                            column=0,
                                                                                                            sticky=W)
        Radiobutton(self, text='12.00-13.00', variable=self.time, value='12.00-13.00', command=self.update_text_delivery).grid(row=13,
                                                                                                            column=0,
                                                                                                            sticky=W)
        Radiobutton(self, text='13.00-14.00', variable=self.time, value='13.00-14.00', command=self.update_text_delivery).grid(row=14,
                                                                                                            column=0,
                                                                                                            sticky=W)
        Radiobutton(self, text='15.00-16.00', variable=self.time, value='15.00-16.00', command=self.update_text_delivery).grid(row=15,
                                                                                                            column=0,
                                                                                                      sticky=W)

        self.result_txt = Text(self, width=40, height=1, wrap=WORD)
        self.result_txt.grid(row=16, column=0, columnspan=3)

#Способ оплаты
        Label(self, text='Выберете способ оплаты').grid(row=17, column=0, sticky=W)
        self.pay = StringVar()
        self.pay.set(None)
        Radiobutton(self, text='Наличными курьеру', variable=self.pay, value='Наличными курьеру',
                    command=self.update_pay_delivery).grid(row=18, column=0, sticky=W)
        Radiobutton(self, text='Картой курьеру', variable=self.pay, value='Картой курьеру',
                    command=self.update_pay_delivery).grid(row=19, column=0, sticky=W)
        Radiobutton(self, text='Онлайн оплата', variable=self.pay, value='Онлайн оплата',
                    command=self.update_pay_delivery).grid(row=20, column=0, sticky=W)

        self.pay_txt = Text(self, width=40, height=1, wrap=WORD)
        self.pay_txt.grid(row=21, column=0, columnspan=3)

# Запрос ФИО

        self.fio_lbl = Label(self, text='Введите Ваше имя: ').grid(row=22, column=0, sticky=W)
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row=22, column=1, sticky=W)

        self.submit_bttn = Button(self, text='Подтвердить заказ', command=self.reveal).grid(row=23, column=0, sticky=W)
        self.total_txt = Text(self, width=40, height=10, wrap=WORD)
        self.total_txt.grid(row=24, column=0, columnspan=3)

        # Label(self, text=f'Стоимость заказа: {self.total_price}, время доставки: {self.time.get}, способ оплата: {self.pay.get}').grid(row=22, column=0, sticky=W)

    def update_text_dishes(self):
        dish = ''
        self.total_price = 0
        if self.dish_1.get():
            self.total_price += self.price_dish_1
            # dish += f'Жареха\nобщая стоимость заказа {self.total_price} руб.'
            dish += f'Жареха\n'
        if self.dish_2.get():
            self.total_price += self.price_dish_2
            # dish += f'\nСолянка\nобщая стоимость заказа {self.total_price} руб.'
            dish += f'Солянка\n'
        if self.dish_3.get():
            self.total_price += self.price_dish_3
            # dish += f'\nПельмени\nобщая стоимость заказа {self.total_price} руб.'
            dish += f'Пельмени\n'
        if self.dish_4.get():
            self.total_price += self.price_dish_4
            # dish += f'\nКомпот\nобщая стоимость заказа {self.total_price} руб.'
            dish += f'Компот\n'
        if self.dish_5.get():
            self.total_price += self.price_dish_5
            # dish += f'\nЧай\nобщая стоимость заказа {self.total_price} руб.'
            dish += f'Чай\n'
        if self.dish_6.get():
            self.total_price += self.price_dish_6
            # dish += f'\nПеченье\nобщая стоимость заказа {self.total_price} руб.'
            dish += f'Печенье\n'
        self.result_txt_dishes.delete(0.0, END)
        self.result_txt_dishes.insert(0.0, dish)
        return dish


    def update_text_delivery(self):
        # message = 'Выбранное время доставки: '
        message = ''
        message += self.time.get()
        self.result_txt.delete(0.0, END)
        self.result_txt.insert(0.0, message)
        return message

    def update_pay_delivery(self):
        # message = 'Выбранный способ оплаты: '
        message = ''
        message += self.pay.get()
        self.pay_txt.delete(0.0, END)
        self.pay_txt.insert(0.0, message)
        return message

    def reveal(self):
        self.contents = self.pw_ent.get()
        total_message = f'{self.contents}!\nВаш заказ:\n{self.update_text_dishes()}Сумма заказа: {self.total_price} руб.\n' \
                        f'Время доставки: {self.update_text_delivery()}\nСпособ оплаты: {self.update_pay_delivery()}'
        self.total_txt.delete(0.0, END)
        self.total_txt.insert(0.0, total_message)


root = Tk()
root.title('Доставка')
root.geometry('450x950')
app = Aplication(root)
root.mainloop()