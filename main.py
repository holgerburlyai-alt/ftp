import flet as ft

def main(page: ft.Page):
    # Базовые настройки страницы
    page.title = "FARA MOBILE SYSTEM"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400  # Для теста на компе, чтобы было похоже на телефон
    page.window_height = 700
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- ФУНКЦИИ ПЕРЕКЛЮЧЕНИЯ ЭКРАНОВ ---

    def go_to_menu(e):
        page.clean()
        show_second_menu()

    def go_to_main(e):
        page.clean()
        show_main_menu()

    # --- ЭКРАНЫ ---

    def show_main_menu():
        page.add(
            ft.Text("ГЛАВНОЕ МЕНЮ", size=32, weight="bold"),
            ft.Text("Система FARA готова", color="grey"),
            ft.Divider(height=50, color="transparent"),
            ft.ElevatedButton(
                text="ОТКРЫТЬ МЕНЮ",
                width=250,
                height=60,
                on_click=go_to_menu,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                    bgcolor="red",
                    color="white"
                )
            )
        )

    def show_second_menu():
        page.add(
            ft.Text("СЕКРЕТ", size=32, weight="bold", color="yellow"),
            ft.Container(
                content=ft.Text("я же надеюсь мы том и джерри посмотрим ?", text_align="center"),
                padding=20
            ),
            ft.Divider(height=50, color="transparent"),
            ft.OutlinedButton(
                text="НАЗАД В ГЛАВНОЕ",
                width=250,
                height=60,
                on_click=go_to_main
            )
        )

    # Запускаем первый экран при старте
    show_main_menu()

# Запуск приложения
if __name__ == "__main__":
    ft.app(target=main)