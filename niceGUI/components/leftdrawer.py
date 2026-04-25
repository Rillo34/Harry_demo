from nicegui import ui

def left_drawer():
    with ui.row().classes('items-center gap-4 p-2'):
        ui.button(icon='menu', on_click=lambda: drawer.toggle()).props('flat round color=primary')
        ui.label('Menu').classes('text-xl font-bold')

    with ui.left_drawer(value=False, bordered=True, elevated=True) as drawer:
        drawer.props('width=240 bordered')

        with ui.list().classes('w-full bg-transparent'):

            # HOME
            with ui.item(on_click=lambda: ui.navigate.to('/')).props('tag=a'):
                with ui.item_section():
                    ui.item_label('Home').classes('text-lg')
                with ui.item_section().props('side'):
                    ui.icon('home')

            ui.separator()

            # CANDIDATE JOBS
            with ui.item(on_click=lambda: ui.navigate.to('/consultants')).props('tag=a'):
                with ui.item_section():
                    ui.item_label('Consultants').classes('text-lg')
                with ui.item_section().props('side'):
                    ui.icon('work')

            # # JOBS
            # with ui.item(on_click=lambda: ui.navigate.to('/jobs')).props('tag=a'):
            #     with ui.item_section():
            #         ui.item_label('Jobs').classes('text-lg')
            #     with ui.item_section().props('side'):
            #         ui.icon('business_center')

            # # AVAILABILITY
            # with ui.item(on_click=lambda: ui.navigate.to('/availability')).props('tag=a'):
            #     with ui.item_section():
            #         ui.item_label('Availability').classes('text-lg')
            #     with ui.item_section().props('side'):
            #         ui.icon('event_available')

            # # ALLOCATIONS
            # with ui.item(on_click=lambda: ui.navigate.to('/allocations')).props('tag=a'):
            #     with ui.item_section():
            #         ui.item_label('Allocations').classes('text-lg')
            #     with ui.item_section().props('side'):
            #         ui.icon('timeline')

            # with ui.item(on_click=lambda: ui.navigate.to('/inspiration')).props('tag=a'):
            #     with ui.item_section():
            #         ui.item_label('Inspiration').classes('text-lg')
            #     with ui.item_section().props('side'):
            #         ui.icon('lightbulb')

            # # DATA VALIDATION
            # with ui.item(on_click=lambda: ui.navigate.to('/datavalidation')).props('tag=a'):
            #     with ui.item_section():
            #         ui.item_label('Data Validation').classes('text-lg')
            #     with ui.item_section().props('side'):
            #         ui.icon('rule')

            # INSPIRATION
            with ui.item(on_click=lambda: ui.navigate.to('/inspiration')).props('tag=a'):
                with ui.item_section():
                    ui.item_label('Inspiration').classes('text-lg')
                with ui.item_section().props('side'):
                    ui.icon('auto_awesome')   # wizard/magic icon
            
            with ui.item(on_click=lambda: ui.navigate.to('/backend_test')).props('tag=a'):
                with ui.item_section():
                    ui.item_label('Backend test').classes('text-lg')
                with ui.item_section().props('side'):
                    ui.icon('developer_board')   # wizard/magic icon
