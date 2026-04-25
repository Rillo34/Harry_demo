from nicegui import ui
from components.leftdrawer import left_drawer
from app_state import API_client, ui_controller


def backend_test_page():
    # Render drawer on this page
    ui.button("Test data", on_click=ui.notify("test"))
   