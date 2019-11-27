import PySimpleGUI as sg

sg.change_look_and_feel('DarkAmber')	# Add a touch of color

tab1_layout =  [[sg.T('This is inside tab 1')]]
tab2_layout = [[sg.T('This is inside tab 2')],
               [sg.In(key='in')]]

# Code to set the Speed of RGB
speed_labels = {
    0: 'fastest',
    1: 'faster',
    2: 'normal',
    3: 'slower',
    4: 'slowest',
}


# Presets include fixed (1 color), breathing (up to 9 colors, logo plus each ring),
# fading (between two and eight colors), marquee, covering marquee,
# pulse (up to eight colors), spectrum, alternating, candle, wings.

# All the stuff inside your window.
layout = [[sg.TabGroup([[sg.Tab('Presets', tab1_layout), sg.Tab('Settings', tab2_layout)]])],
              [sg.Button('Read')]]


# Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
