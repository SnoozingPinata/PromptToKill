
import os
import datetime
import PySimpleGUI as sg


def prompttokill(friendly_name: str, process_name: str, wait_time_seconds: int) -> None:
    start_time = datetime.datetime.now()
    kill_time = start_time + datetime.timedelta(seconds=wait_time_seconds)

    layout = [ 
        [sg.Text(f'{friendly_name} will be terminated at:')], 
        [sg.Text(text=f"{kill_time.ctime()}")],
        [sg.Text('Press "Cancel" to close this pop-up or press "Kill Now" to terminate the process immediately.')],
        [sg.Button('Kill Now'), sg.Button('Cancel')]
        ]

    window = sg.Window('Prompt To Kill', layout)

    while True:
        event, values = window.read(timeout=1000)
        current_time = datetime.datetime.now()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'Kill Now' or current_time >= kill_time:
            os.system(f"taskkill /im {process_name}")
            break
    
    window.close()


if __name__ == "__main__":
    friendly_name = "ProContractor"
    # used for testing
    #process_name = "chrome.exe"
    process_name = "maxwell.stp.infrastructure.shell.exe"
    wait_time_seconds = 1200
    prompttokill(friendly_name, process_name, wait_time_seconds)