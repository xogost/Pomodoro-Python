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
	_stop = False
	_startButton = None

	def __init__(self):
		self.startApp(self._master)

	def startApp(self, master):
		self._root = Tk()

		self._root.title('Pomodoro by Xogost!!!')
		#self._root.iconbitmap( bitmap=None, default='pomodoro.ico')

		#set title to form
		title = Label(self._form, text="Pomodoro")
		title.pack()
		#create label for time of pomodoro
		self._reloj = Label(self._form, text=self._timeLabel)
		self._reloj.pack()
		#create button for start pomodoro
		self._startButton = Button(self._form, text="Iniciar Pomodoro", command=self.startPomodoro)
		self._startButton.pack()
		#create button for stop pomodoro
		stopButton = Button(self._form, text="Parar Pomodoro", command=self.stopPomodoro)
		stopButton.pack()
		
		self._menu = Menu(self._root)

		filemenu = Menu(self._menu, tearoff=0)
		acercade = Menu(self._menu, tearoff=0)

		filemenu.add_command(label="Aplicacion", command=self.hola)
		filemenu.add_command(label="Notificaciones y alertas", command=self.hola)

		acercade.add_command(label="Aplicacion", command=self.hola)
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
		if self._stop == False:			
			if self._timeLabel == '00:00':
				print 'Finzalizado!!!'
				self.modalPausa()
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
		self._stop = False
		self._t = Timer(1.0, self.discountTime)
		self._t.start()

	def stopPomodoro(self):
		self._startButton.config(text="Reanudar Pomodoro")
		self._stop = True

	def modalPausa(self):
		modalpausa = Tk()
		#set title to form
		title = Label(modalpausa, text="Has una Pausa!!!")
		title.pack()
		#create label for time of pomodoro
		labelpausa = Label(self._form, text=self._timeLabel)
		labelpausa.pack()
		#create button for start pomodoro
		startpausa = Button(modalpausa, text="Iniciar Pausa", command=self.pausa)
		startpausa.pack()

		modalpausa.mainloop()

	def pausa(self):
		self._timeLabel = "05:00"
		self.discountTime()

	def hola(self):
		print 'hola'