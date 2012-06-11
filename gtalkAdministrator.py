import warnings
warnings.filterwarnings("ignore") # silence DeprecationWarning messages

from xmpp import *
class gtalkAdministrator(object):
	
	USERNAME = "xogost"       # don't include @gmail.com
	PASSWORD = "5CCjF3k2Vqg="
	RESOURCE = "gmail.com"

	"""docstring for gtalkAdministrator"""
	def __init__(self, arg=None):
		super(gtalkAdministrator, self).__init__()
		self.arg = arg

	def setState(self, state):
		cl=Client(server='gmail.com',debug=[])
		if not cl.connect(server=('talk.google.com',5222)):
			raise IOError('Can not connect to server.')
		if not cl.auth(self.USERNAME, self.PASSWORD, self.RESOURCE):
		    raise IOError('Can not auth with server.')
		cl.send(Iq('set','google:shared-status', payload=[
				Node('show',payload='dnd'),
				Node('status',payload=state if len(state)>2 else "")
		]))
		cl.disconnect()
		