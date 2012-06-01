from Tkinter import *
from threading import * 

class Pomodoro:
	_t = None
	_form = None
	_master = None
	_reloj = None
	_timeLabel = "25:00"
	_timeout = 1

	def __init__(self):
		self.startApp(self._master)

	def startApp(self, master):
		self._form = Frame(master)
		self._form.pack()

		title = Label(self._form, text="Pomodoro by Xogost!")

		self._reloj = Label(self._form, text=self._timeLabel)

		startButton = Button(self._form, text="Iniciar Pomodoro", command=self.startPomodoro())

		title.pack()
		self._reloj.pack()
		startButton.pack()
		self._form.mainloop()

	def discountTime(self):
		runtime = self._timeLabel.split(':')
		if runtime[1] == "00":
			runtime[0] = int(runtime[0]) - 1
			runtime[1] = 59
		elif int(runtime[0]) == 0 and int(runtime[1]) == 0:
			self._timeout = 0
		else:
			runtime[1] = int(runtime[1]) - 1

		if int(runtime[1]) < 10 and int(runtime[0]) < 10:
			self._timeLabel = "0%d:0%d" % (int(runtime[0]), int(runtime[1]))
		elif int(runtime[1]) < 10:
			self._timeLabel = "%d:0%d" % (int(runtime[0]), int(runtime[1]))
		elif int(runtime[0]) < 10:
			self._timeLabel = "0%d:%d" % (int(runtime[0]), int(runtime[1]))
		else:
			self._timeLabel = "%d:%d" % (int(runtime[0]), int(runtime[1]))
		
		self._reloj.config(text=self._timeLabel)
		self._reloj.update_idletasks()
		_t = Timer(1.0, self.discountTime)
		_t.start()

	def startPomodoro(self):
		_t = Timer(1.0, self.discountTime)
		_t.start()