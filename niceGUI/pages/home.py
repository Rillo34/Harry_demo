from nicegui import ui
from components.leftdrawer import left_drawer

def home_page():
    # Render drawer on this page
    left_drawer()
    with ui.column().classes('w-full items-start gap-6 p-4'):

        # Title with a "Harry" icon
        with ui.row().classes('items-center gap-3'):
            ui.icon('auto_awesome').classes('text-4xl text-purple-600')
            ui.label('Harry Demo – Home').classes(
                'text-3xl font-bold text-slate-800'
            )

        ui.label(
            'Welcome! This is the landing page for your recruitment and matching demo. '
            'Use the menu on the left to navigate between features.'
        ).classes('text-slate-600 text-md max-w-2xl')

        # --- Quick navigation cards ---
        with ui.row().classes('gap-4 mt-4'):

            with ui.card().classes('p-4 w-64 cursor-pointer hover:shadow-lg transition') \
                    .on('click', lambda: ui.notify(f'Work in progress')):
                ui.icon('groups').classes('text-4xl text-blue-600')
                ui.label('Candidate Jobs').classes('font-bold text-lg')
                ui.label('Match candidates to jobs').classes('text-sm text-slate-500')

            with ui.card().classes('p-4 w-64 cursor-pointer hover:shadow-lg transition') \
                    .on('click', lambda: ui.navigate.to('/consultants')):
                ui.icon('work').classes('text-4xl text-green-600')
                ui.label('Jobs').classes('font-bold text-lg')
                ui.label('Consultant matching powered by Marcus W').classes('text-sm text-slate-500')

            with ui.card().classes('p-4 w-64 cursor-pointer hover:shadow-lg transition') \
                    .on('click', lambda: ui.navigate.to('/inspiration')):
                ui.icon('lightbulb').classes('text-4xl text-amber-500')
                ui.label('Inspiration').classes('font-bold text-lg')
                ui.label('Legacy Harry‑demo visualizations').classes('text-sm text-slate-500')

        ui.separator().classes('my-6')

        # --- Info section ---
        ui.label('Quick Info').classes('text-xl font-semibold text-slate-700')

        with ui.row().classes('gap-6'):
            with ui.card().classes('p-4 w-60'):
                ui.icon('analytics').classes('text-3xl text-purple-600')
                ui.label('Data Visualization').classes('font-bold')
                ui.label('Plotly-based charts').classes('text-sm text-slate-500')

            with ui.card().classes('p-4 w-60'):
                ui.icon('grid_on').classes('text-3xl text-indigo-600')
                ui.label('Score Grids').classes('font-bold')
                ui.label('Automatic matching matrices.').classes('text-sm text-slate-500')

            with ui.card().classes('p-4 w-60'):
                ui.icon('dashboard').classes('text-3xl text-rose-600')
                ui.label('UI Components').classes('font-bold')
                ui.label('Tables, filters, dialogs, and more.').classes('text-sm text-slate-500')