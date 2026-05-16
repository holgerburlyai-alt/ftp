import flet as ft

def main(page: ft.Page):
    # Настройки экрана приложения
    page.title = "Для Александры"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Текст и кнопка
    title_text = ft.Text(
        "Привет, Сашаа :)🎬", 
        size=28, 
        weight=ft.FontWeight.BOLD, 
        color=ft.Colors.PINK_200
    )
    
    info_text = ft.Text(
        "Нажми на кнопку ниже", 
        size=16, 
        color=ft.Colors.WHITE70
    )

    def button_click(e):
        info_text.value = "Погнали смотреть Том и Джерри! 🍿"
        page.update()

    action_button = ft.ElevatedButton(
        text="План на вечер", 
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.PINK_200,
        on_click=button_click
    )

    # Добавляем элементы на экран
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[title_text, info_text, action_button],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            padding=30,
            bgcolor=ft.Colors.BLACK12,
            border_radius=20
        )
    )

# Запуск приложения
if __name__ == "__main__":
    ft.app(target=main)