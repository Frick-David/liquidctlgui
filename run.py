import PySimpleGUI as sg
# from wrapper import device_descs

# Want to trouble shoot code heree
# if os.environ.get('DISPLAY','') == '':
#     print('no display found. Using non-interactive Agg backend')

# Add a touch of color
sg.change_look_and_feel('Reddit')

# Hue 2
# Rainbow, blackout, backwards-marquee-<length>, covering-marquee,
# covering-backwards-marquee, alternating, moving-alternating,
# backwards-moving-alternating, breathing, super-breathing,
# pulse, candle, wings
modes = ['off', 'fixed', 'super-fixed', 'fading', 'spectrum-wave',
        'backwards-spectrum-wave', 'super-wave', 'backwards-super-wave',
        'marquee-<length>']
# NXZT smart device v2 -
# alternating-<length>, moving-alternating-<length>,
# backwards-moving-alternating-<length>, starry-night,
# rainbow-flow, backwards-rainbow-flox,
# super-rainbow, backwards-super-rainbow,
# rainbow-pulse, backwards-rainbow-pulse
# wings

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
    mode_and_leds.append([sg.T(led), sg.Input(key='Color'.join(led)), sg.ColorChooserButton('Input', target='Color'.join(led))])


# RGB presets
presents_tab =  [[sg.Column(mode_and_leds), sg.VerticalSeparator(pad=(5,5)), sg.Column([[sg.Text('Speed')],
                 [sg.Column([[sg.Slider(range=(0,4), default_value=2, size=(10, 20), orientation='vertical')]]), sg.Column(speeds)]])]]


# Should list all devices detected by Liquidctl
# Need a --time-per-color preset --time-off
# Need an --alert-color --alert-threshold
devices_tab = [
    [sg.T('Detected Devices')],
    [sg.T('Will put liquidctl status information here')],
]

# Settings Tab - Fan Speed, Pump Speed
settings_tab = [[sg.T('This is inside tab 2')],
               [sg.In(key='in')]]

# i = 1
# for desc in device_descs:
#     devices_tab.append([sg.Frame(title='Device ' + str(i), layout=[[sg.T(desc)]])])
#     i += 1


# All the stuff inside Main Window window.
layout = [[sg.TabGroup([[sg.Tab('Presets', presents_tab),
            sg.Tab('Devices', devices_tab),
            sg.Tab('Settings', settings_tab),
            ]])], [sg.Button('Read')]]


if __name__ == '__main__':
    # Create the Window
    window = sg.Window('Liquidctl GUI', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):	# if user closes window or clicks cancel
            break
        print('You entered ', values[0])

    window.close()
