
import os
import datetime
import PySimpleGUI as sg

# notes:
# need to fix the display of the timer in the GUI
# want to be able to pass process name and amount of time to wait into program fro CLI


# format is: year, month, day, hour, minute, second, microsecond
start_time = datetime.datetime.now()
end_time = start_time + datetime.timedelta(minutes=10)


def Cancel_program(executable_name):
    os.system(f"taskkill /f /im {executable_name}")


sg.theme('BluePurple')

layout = [
            [sg.Text('ProContractor will be terminated in:')],
            [sg.Text(key='-TIMER-')],
            [sg.Button('Kill'), sg.Button('Cancel')]
        ]

window = sg.Window('Prompt2Kill', layout)

while True:
    event, values = window.read()
    print(event, values)
    current_time = datetime.datetime.now()
    window['-TIMER-'].update(end_time - current_time)
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Kill' or current_time >= end_time:
        #Cancel_program("maxwell.stp.infrastructure.shell.exe")
        Cancel_program("chrome.exe")
        window.close()