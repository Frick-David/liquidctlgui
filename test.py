import PySimpleGUI as sg

sg.change_look_and_feel('DarkAmber')	# Add a touch of color

# TODO: Add other modes
modes = ['off', 'fixed', 'super-fixed', 'fading', 'spectrum-wave',
        'backwards-spectrum-wave', 'super-wave', 'backwards-super-wave',
        'marquee-<length>']
leds = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# Code to set the Speed of RGB
speed_labels = {
    0: 'fastest',
    1: 'faster',
    2: 'normal',
    3: 'slower',
    4: 'slowest',
}

speeds = [[sg.T('Fastest')],
         [sg.T('')],
         [sg.T('- - -')],
         [sg.T('')],
         [sg.T('- - - - - -')],
         [sg.T('')],
         [sg.T('- - -')],
         [sg.T('')],
         [sg.T('Slowest')]]

mode_and_leds = [[sg.Combo(modes)]]
for led in leds:
    mode_and_leds.append([sg.T(led), sg.Input('Hex Color')])

tab1_layout =  [[sg.Column(mode_and_leds), sg.VerticalSeparator(pad=(5,5)),
                 sg.Slider(range=(0,4), default_value=2, size=(10, 20), orientation='vertical'),
                 sg.Column(speeds)]]
tab2_layout = [[sg.T('This is inside tab 2')],
               [sg.In(key='in')]]

# Presets include fixed (1 color), breathing (up to 9 colors, logo plus each ring),
# fading (between two and eight colors), marquee, covering marquee,
# pulse (up to eight colors), spectrum, alternating, candle, wings.

# All the stuff inside your window.
layout = [[sg.TabGroup([[sg.Tab('Presets', tab1_layout), sg.Tab('Settings', tab2_layout)]])],
              [sg.Button('Read')]]


# Create the Window
window = sg.Window('Liquidctl GUI', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
