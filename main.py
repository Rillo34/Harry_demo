from nicegui import ui
import sys
import os
from pathlib import Path

# Gör det möjligt att importera backend från Harry_linux
# sys.path.append(os.path.expanduser("~/Python/Harry_linux"))

ui.label("Harry Demo – Minimal UI")

with ui.row():
    ui.button("Visa kandidater", on_click=lambda: ui.notify("Kommer snart"))
    ui.button("Matchning", on_click=lambda: ui.notify("Kommer snart"))
    ui.label ("För mer information, besök vår GitHub:").classes("text-sm")
    ui.label("bajen är bäst").classes("text-sm text-blue-500")
    
if __name__ in {"__main__", "__mp_main__"}:
    ui.run(port=8091)
