import flet as ft

def main(page: ft.Page):
    # Настройки страницы для мобилки
    page.title = "FARA MOBILE SYSTEM"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # --- ФУНКЦИИ КНОПОК ---
    def go_to_menu(e):
        page.clean()
        page.add(
            ft.Text("СЕКРЕТ", size=32, weight="bold", color="yellow"),
            ft.Container(
                content=ft.Text(
                    "я же надеюсь мы том и джерри посмотрим ?", 
                    text_align=ft.TextAlign.CENTER, 
                    size=20
                ),
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
        page.update()

    def go_to_main(e):
        page.clean()
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
        page.update()

    # --- ЗАПУСК ПЕРВОГО ЭКРАНА ПРИ СТАРТЕ ---
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
    
    page.update()

# СТРОГИЙ ЗАПУСК ДЛЯ АНДРОИДА
ft.app(main)
