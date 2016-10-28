import time
import calendar
import datetime

class cl_TimeDate:
	'Common class for interacting with Date and Time'

# Class Constructor
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
	# def __init__(self):


# ClassMothod
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
	def getUTC(self):

		# Get the current date
		# dToday      = datetime.datetime.now()
		dToday = datetime.datetime.now()
		# Cast current date format into Tuple
		dTuple = dToday.timetuple()
		# Cast the Tuple format into UTC (seconds from January 1970)
		dUTC  = calendar.timegm( dTuple )
		# Nice source: http://www.saltycrane.com/blog/2008/11/python-datetime-time-conversions/

		return dUTC

# ClassMothod
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
	def getDate(self):
				# Get the current date
		dDate  = datetime.datetime.now()
		dToday = dDate.strftime('%d/%m/%Y')
		# ('%Y-%m-%d %H:%M:%S')

		return (dToday)

# ClassMothod
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
	def getTime(self):
				# Get the current date
		dDate  = datetime.datetime.now()
		dToday = dDate.strftime('%H:%M:%S')

		return (dToday)

# ClassMothod
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
	def delay(self, iDelay):
		time.sleep( iDelay )