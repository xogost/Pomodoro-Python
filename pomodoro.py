from Tkinter import *
from threading import * 

class Pomodoro:
	_t = None
	_form = None
	_master = None
	_reloj = None
	_timeLabel = "01:00"
	_timeout = 1
	_menu = None
	_tkmenu = None
	_root = None

	def __init__(self):
		self.startApp(self._master)

	def startApp(self, master):
		self._root = Tk()

		#set title to form
		title = Label(self._form, text="Pomodoro by Xogost!")
		title.pack()
		#create label for time of pomodoro
		self._reloj = Label(self._form, text=self._timeLabel)
		self._reloj.pack()
		#create button for start pomodoro
		startButton = Button(self._form, text="Iniciar Pomodoro", command=self.startPomodoro)
		startButton.pack()
		
		self._menu = Menu(self._root)

		filemenu = Menu(self._menu, tearoff=0)
		acercade = Menu(self._menu, tearoff=0)

		filemenu.add_command(label="Aplicacion", command=self.hola)
		filemenu.add_separator()
		filemenu.add_command(label="Notificaciones y alertas", command=self.hola)

		acercade.add_command(label="Aplicacion", command=self.hola)
		acercade.add_separator()
		acercade.add_command(label="Desarrollador", command=self.hola)

		self._menu.add_cascade(label="Configuracion", menu=filemenu)		
		self._menu.add_cascade(label="Acerda de", menu=acercade)

		self._root.config(menu=self._menu)
		
		self._form = Frame(self._root, width=500, height=200)
		self._form.pack()

		self.center_window()

		self._root.mainloop()


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
		if self._timeLabel == '00:00':
			print 'Finzalizado!!!'
		else:
			_t = Timer(1.0, self.discountTime)
			_t.start()
	
	def center_window(self,w=300, h=200):
	    # get screen width and height
	    ws = self._root.winfo_screenwidth()
	    hs = self._root.winfo_screenheight()
	    # calculate position x, y
	    x = (ws/2) - (w/2)    
	    y = (hs/2) - (h/2)
	    self._root.geometry('%dx%d+%d+%d' % (w, h, x, y))	

	def startPomodoro(self):
		_t = Timer(1.0, self.discountTime)
		_t.start()
	def hola(self):
		print 'hola'