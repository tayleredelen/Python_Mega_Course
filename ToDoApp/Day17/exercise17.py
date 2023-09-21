import PySimpleGUI as sg

label1 = sg.Text("Enter feet:")
input1 = sg.Input()

label2 = sg.Text("Enter inches:")
input2 = sg.Input()

# How to convert feet & inces to meters:
# The input is 5′7″.
# Convert the feet to inches: 5 feet = 5* 12 = 60 inches.
# Add the 7 inches, for a total of 67 inches.
# Multiply by 25.4, thus: 67 * 25,4 = 1 701.8 mm, exactly.

def conversion(feet, inches):
    feet_conv = feet * 12
    inch_conv = inches
    feet_inch = feet_conv + inch_conv
    meters = feet_inch * 25.4
    return meters


convert_button = sg.Button("Convert")
result = sg.Text(conversion(feet=label1, inches=label2))
window = sg.Window("Convertor", layout=[[label1, input1],
                                              [label2, input2],
                                                [convert_button, result]])
window.read()
window.close()
