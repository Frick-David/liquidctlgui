import tkinter as tk
from tkinter import Tk, Label, Button, LEFT, RIGHT, Frame, YES, NO, BOTH
from tkinter import W
from tkinter import ttk, Scale
from tkinter.colorchooser import askcolor


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

		Button(text='Select Color', command=self.get_color).pack()

		# Code to set the Speed of RGB
		speed_labels = {
			0: 'slowest',
			1: 'slower',
			2: 'normal',
			3: 'faster',
			4: 'fastest',
		}
		speed_scale = Scale(tab_settings, from_=min(speed_labels), to=max(speed_labels),
					showvalue=False, command=self.scale_labels)
		speed_scale.pack()

		modes = ['off', 'fixed', 'super-fixed', 'fading', 'spectrum-wave',
			'backwards-spectrum-wave', 'super-wave', 'backwards-super-wave',
			'marquee-<length>',]
			# Add the other modes.

		# for-loop the mode as each of their own widget say button to 
		# activate then add them to the window etc.

	def scale_labels(self):
		self.speed_scale.config(label=speed_labels[int(value)])

	def get_color(self):
		print(askcolor(parent=self, title='Pick a color.'))



class Window(Frame):
	def __init__(self, master=None, cnf={}, **kw):
		super().__init__(master, cnf, **kw)
		self.pack()


instance = Tk()
window = Window(instance)
instance.geometry('500x250')
my_gui = Rgbgui(instance)
instance.mainloop()
