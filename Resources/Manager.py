from dearpygui import *

set_main_window_size(270, 110)
add_group("Group", width=50)
add_button("App", callback="Launcher", height=50)
add_same_line(spacing=10)
add_button("Demo", callback="Launcher", height=50)
add_same_line(spacing=10)
add_button("Docs", callback="Launcher", height=50)
add_same_line(spacing=10)
add_button("IDE", callback="Launcher", height=50)
end_group()

def Launcher(sender, data):

    if sender == "App":
        run_file("App.py", "")
        
    elif sender == "Demo":
        run_file("Demo.py", "")
        
    if sender == "Documentation":
        run_file("Demo.py", "--documentation --noconfig")
        
    if sender == "IDE":
        run_file("Demo.py", "--editor --noconfig")

start_dearpygui()