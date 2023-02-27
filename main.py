# Imports
from pywinauto.application import Application
# Start Application
app = Application(backend="uia").start(
    "C:\Program Files\Oracle\VirtualBox\VirtualBox.exe")
# Identifiers
# app.oraclevmvirtualboxManager.print_control_identifiers()
# Open Virtual macine
# Chnage virtual macine name "eg: title:"test" should be change to any other name"
fileopen = app.oraclevmvirtualboxManager.child_window(
    title="test", control_type="ListItem").wrapper_object()
fileopen.click_input()
# Select task
startmachine = app.oraclevmvirtualboxManager.child_window(
    title="Start", control_type="Button").wrapper_object()
startmachine.click_input()
# Continue to add macine if more
