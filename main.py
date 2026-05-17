from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class MainApp(App):
    def build(self):
        # Настраиваем темный хакерский фон
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        
        # Главный контейнер (все элементы идут сверху вниз)
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Текст главного меню
        self.title_label = Label(
            text="ГЛАВНОЕ МЕНЮ", 
            font_size='32sp', 
            bold=True
        )
        self.subtitle_label = Label(
            text="Система FARA готова", 
            font_size='18sp', 
            color=(0.5, 0.5, 0.5, 1)
        )
        
        # Большая красная кнопка
        self.btn = Button(
            text="ОТКРЫТЬ МЕНЮ",
            font_size='20sp',
            background_normal='',
            background_color=(0.8, 0.1, 0.1, 1), # Красный цвет
            size_hint=(None, None),
            size=(250, 60),
            pos_hint={'center_x': 0.5}
        )
        # Привязываем клик к функции переключения экрана
        self.btn.bind(on_press=self.open_secret_menu)
        
        # Добавляем всё на экран
        self.layout.add_widget(self.title_label)
        self.layout.add_widget(self.subtitle_label)
        self.layout.add_widget(self.btn)
        
        return self.layout

    def open_secret_menu(self, instance):
        # Очищаем старые виджеты и строим СЕКРЕТНЫЕ ТОМ И ДЖЕРРИ
        self.layout.clear_widgets()
        
        secret_label = Label(
            text="СЕКРЕТ", 
            font_size='32sp', 
            bold=True, 
            color=(1, 1, 0, 1) # Желтый
        )
        text_label = Label(
            text="я же надеюсь мы том и джерри посмотрим ?", 
            font_size='20sp',
            halign='center'
        )
        
        back_btn = Button(
            text="НАЗАД В ГЛАВНОЕ",
            font_size='18sp',
            size_hint=(None, None),
            size=(250, 60),
            pos_hint={'center_x': 0.5}
        )
        back_btn.bind(on_press=self.back_to_main)
        
        self.layout.add_widget(secret_label)
        self.layout.add_widget(text_label)
        self.layout.add_widget(back_btn)

    def back_to_main(self, instance):
        # Возвращаем всё взад
        self.layout.clear_widgets()
        self.layout.add_widget(self.title_label)
        self.layout.add_widget(self.subtitle_label)
        self.layout.add_widget(self.btn)

if __name__ == '__main__':
    MainApp().run()