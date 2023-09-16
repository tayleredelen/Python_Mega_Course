import functions
import PySimpleGUI as sg
# ^renaming sg for easier code

label = sg.Text("Type in a ToDo: ")
input_box = sg.InputText(tooltip="Enter ToDo")
add_button = sg.Button("Add")

window = sg.Window("My ToDo App", layout=[[label], [input_box, add_button]])
# ^layout types have to be of PySimpleGUI
window.read()
# ^the .read() method displays window on screen
print("Hello")
# ^prints after clicking anything in window
window.close()

