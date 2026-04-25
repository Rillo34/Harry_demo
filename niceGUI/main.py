from nicegui import ui

from pages.home import home_page
from pages.inspiration import inspiration_page
from pages.consultants import consultants_page
from pages.backend_test import backend_test_page


@ui.page('/')
def route_home():
    home_page()

@ui.page('/inspiration')
def route_inspiration():
    inspiration_page()

@ui.page('/consultants')
def route_consultants():
    consultants_page()

@ui.page('/backend_test')
def route_backend_test():
    backend_test_page()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(host="0.0.0.0", port=8091)



