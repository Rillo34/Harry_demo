from nicegui import ui
from components.leftdrawer import left_drawer
from app_state import API_client, ui_controller

async def test_backend():
    answer = await API_client.ping()
    ui.notify(f'Received from BE: {answer}')
    ui.label(f'Received from BE: {answer}')


def backend_test_page():
    left_drawer()
    # Render drawer on this page
    # ui.button("Test data", on_click= lambda e: ui.notify("test"))
    ui.button("Test backend", on_click= test_backend)
   