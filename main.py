from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math

class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        # Поле для отображения результата
        self.result = TextInput(
            font_size='24sp',
            readonly=True,
            halign='right',
            size_hint_y=0.2
        )
        self.add_widget(self.result)

        # Создаем сетку для кнопок
        button_layout = GridLayout(cols=4, spacing=10, size_hint_y=0.8)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '!', '√', '^'
        ]

        for btn in buttons:
            if btn == '=':
                button = Button(text=btn, font_size='20sp')
                button.bind(on_press=self.evaluate)
            elif btn == 'C':
                button = Button(text=btn, font_size='20sp')
                button.bind(on_press=self.clear)
            elif btn == '!':  # факториал
                button = Button(text=btn, font_size='20sp')
                button.bind(on_press=self.factorial)
            elif btn == '√':  # квадратный корень
                button = Button(text=btn, font_size='20sp')
                button.bind(on_press=self.square_root)
            elif btn == '^':  # возведение в степень
                button = Button(text=btn, font_size='20sp')
                button.bind(on_press=self.power)
            else:
                button = Button(text=btn, font_size='20sp')
                button.bind(on_press=self.button_pressed)
            button_layout.add_widget(button)

        self.add_widget(button_layout)

    def button_pressed(self, instance):
        current = self.result.text
        new_text = current + instance.text
        self.result.text = new_text

    def clear(self, instance):
        self.result.text = ''

    def evaluate(self, instance):
        try:
            # Для возведения в степень предполагается, что пользователь вводит выражение с ^
            expression = self.result.text.replace('^', '**')
            self.result.text = str(eval(expression))
        except:
            self.result.text = 'Ошибка'

    def factorial(self, instance):
        try:
            num = int(self.result.text)
            if num < 0:
                self.result.text = 'Ошибка'
            else:
                self.result.text = str(math.factorial(num))
        except:
            self.result.text = 'Ошибка'

    def square_root(self, instance):
        try:
            num = float(self.result.text)
            if num < 0:
                self.result.text = 'Ошибка'
            else:
                self.result.text = str(math.sqrt(num))
        except:
            self.result.text = 'Ошибка'

    def power(self, instance):
        # Для возведения в степень пользователь должен ввести число, затем нажать "^", затем второе число
        # Простая реализация: при нажатии, добавляем "^" к текущему выражению
        # В evaluate заменяем "^" на '**'
        current = self.result.text
        new_text = current + '^'
        self.result.text = new_text

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == '__main__':
    CalculatorApp().run()