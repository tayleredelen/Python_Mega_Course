# Add an exit button to the conversion gui

# Solution:
import PySimpleGUI as sg

exit_button = sg.Button("Exit")

layout = [
    [sg.Text("Enter feet:"), sg.InputText(key='feet')],
    [sg.Text("Enter inches:"), sg.InputText(key='inches')],
    [sg.Button("Convert"), sg.Text("", size=(20, 1), key='result')],
    [exit_button]
]


window = sg.Window("Converter", layout)

def conversion(feet, inches):
    feet = float(feet)
    inches = float(inches)
    total_inches = (feet * 12) + inches
    meters = total_inches * 0.0254
    return meters

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or 'Exit':
        break
    elif event == 'Convert':
        feet = values['feet']
        inches = values['inches']
        result_meters = conversion(feet, inches)
        window['result'].update(f'{result_meters:.2f} meters')


window.close()