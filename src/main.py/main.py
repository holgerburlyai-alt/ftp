import flet as ft

def main(page: ft.Page):
    # Настройки страницы
    page.title = "FARA SYSTEM"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#121212" # Чёткий чёрный фон
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    def go_to_secret(e):
        page.clean()
        page.add(
            ft.Text("СЕКРЕТ 🤫", size=40, weight="bold", color="yellow"),
            ft.Text("я же надеюсь мы том и джерри посмотрим ?", 
                    size=20, text_align="center"),
            ft.Divider(height=40, color="transparent"),
            ft.ElevatedButton("НАЗАД", on_click=lambda _: start())
        )
        page.update()

    def start():
        page.clean()
        page.add(
            ft.Text("FARA SYSTEM V1", size=32, weight="bold"),
            ft.Text("Готовность 100%", color="grey"),
            ft.Divider(height=50, color="transparent"),
            ft.ElevatedButton(
                text="ОТКРЫТЬ СЮРПРИЗ",
                width=280,
                height=70,
                on_click=go_to_secret,
                style=ft.ButtonStyle(
                    bgcolor="red",
                    color="white",
                    shape=ft.RoundedRectangleBorder(radius=15)
                )
            )
        )
        page.update()

    start()

# Запуск без лишних проверок
ft.app(target=main)
