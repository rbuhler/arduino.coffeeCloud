
import platform
import serial

class cl_Arduino:
	'Common class for interacting with Arduino Boards'

# Class Constructor
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
	def __init__(self):

# Identify current SysOp
		self.sSisOp    = platform.system()

# Supported Operating Systems
		self.WINDOWS = 'Windows' 
		self.LINUX   = 'Linux'
		self.MACOSX  = 'Darwin'

# ClassMothod
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
	def serialOpenConn(self, connPort, connBaudrate):
		try:
			conn = serial.Serial( port=connPort, baudrate=connBaudrate )
			return conn
		except:
			return None

# ClassMothod
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
	def serialCloseConn(self, conn):
		conn.close()

# ClassMothod
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
	def serialReadJson(self, conn):

		iOpen    = 0
		bLoop    = True
		cRead    = ''
		jMessage = ''

		while bLoop:
			cRead = conn.read()
			jMessage = jMessage + cRead

			if ( cRead == '{'):
				iOpen += 1
			if ( cRead == '}'):
				iOpen -= 1

			if ( iOpen <= 0 ):
				bLoop = False
		
		return(jMessage)