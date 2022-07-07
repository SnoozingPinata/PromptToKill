
import os
import time
import PySimpleGUI as sg

# notes:
# need to fix the display of the timer in the GUI
# want to be able to pass process name and amount of time to wait into program fro CLI


# format is: year, month, day, hour, minute, second, microsecond
start_time = int(round(time.time() * 100))


def Cancel_program(executable_name):
    os.system(f"taskkill /f /im {executable_name}")


layout = [ 
    [sg.Text('ProContractor will be terminated in:')], 
    [sg.Text("timer text", key='-TIMER-')], 
    [sg.Button('Kill'), sg.Button('Cancel'), sg.Button('DoesNothing')]
    ]

window = sg.Window('Prompt2Kill', layout)

while True:
    event, values = window.read()
    current_time = int(round(time.time() * 100)) - start_time
    window['-TIMER-'].update("this text was updated")
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Kill':
        #Cancel_program("maxwell.stp.infrastructure.shell.exe")
        Cancel_program("chrome.exe")
        window.close()
    window.refresh()
    