import tkinter as tk
from tkinter import Tk, Label, Button, LEFT, RIGHT, Frame, YES, NO, BOTH
from tkinter import W
from tkinter import ttk, Scale
from tkinter.colorchooser import askcolor

import subprocess

class Rgbgui(object):
	def __init__(self, master):
		self.master = master
		master.title('GUI to control RGB')

		tab_control = ttk.Notebook(master)
		tab_presets = tk.Frame(tab_control, background='bisque')
		tab_control.add(tab_presets, text='Presets')
		tab_control.pack(expand=1, fill='both')

		tab_profile = tk.Frame(tab_control, background='bisque')
		tab_control.add(tab_profile, text='Profile')



		tab_settings = tk.Frame(tab_control, background='bisque')
		tab_control.add(tab_settings, text='Settings')
		tab_control.pack(expand=1, fill='both')


		# Code to set the Speed of RGB
		speed_labels = {
			0: 'fastest',
			1: 'faster',
			2: 'normal',
			3: 'slower',
			4: 'slowest',
		}
		label_of_scale = Label(tab_settings, text='Speed')
		label_of_scale.pack()
		speed_scale = Scale(tab_settings, from_=min(speed_labels), to=max(speed_labels),
					showvalue=False)
		speed_scale.pack()

		for label in speed_labels:
			speed_label_label = Label(speed_scale, text=speed_labels[label])
			speed_label_label.pack()

		def send_speed_to_linux():
			subprocess.run(['liquidctl', '--device 0', 'set sync color fixed ffffff'])

		set_speed = Button(text='Set Speed', command=send_speed_to_linux)
		set_speed.pack()


		modes = ['off', 'fixed', 'super-fixed', 'fading', 'spectrum-wave',
			'backwards-spectrum-wave', 'super-wave', 'backwards-super-wave',
			'marquee-<length>']
			# Add the other modes.

		# for-loop the mode as each of their own widget say button to 
		# activate then add them to the window etc.


class Window(Frame):
	def __init__(self, master=None, cnf={}, **kw):
		super().__init__(master, cnf, **kw)
		self.pack()


instance = Tk()
window = Window(instance)
instance.geometry('500x250')
my_gui = Rgbgui(instance)
instance.mainloop()
