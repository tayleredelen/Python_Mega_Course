# Create a program that converts feet and inches to meters.

# Solution:
# import PySimpleGUI as sg
#
# layout = [
#     [sg.Text("Enter feet:"), sg.InputText(key='feet')],
#     [sg.Text("Enter inches:"), sg.InputText(key='inches')],
#     [sg.Button("Convert"), sg.Text("", size=(20, 1), key='result')],
# ]
#
# window = sg.Window("Converter", layout)
#
# def conversion(feet, inches):
#     feet = float(feet)
#     inches = float(inches)
#     total_inches = (feet * 12) + inches
#     meters = total_inches * 0.0254
#     return meters
#
# while True:
#     event, values = window.read()
#
#     if event == sg.WIN_CLOSED:
#         break
#     elif event == 'Convert':
#         feet = values['feet']
#         inches = values['inches']
#         result_meters = conversion(feet, inches)
#         window['result'].update(f'{result_meters:.2f} meters')
#
# window.close()


# Define a function that converts fluid ounces to milliliters knowing that 1 fluid ounce
# is equal to 29.57353 milliliters. For example, I was to call your function with foo(1)
# I would get an output of 29.57353. If I called it with  foo(5) I would get 147.86765, and so on.

# Solution:
# def foo(ounces):
#     oz_conv = float(ounces)
#     ml_conv = oz_conv * 29.57353
#     return ml_conv
