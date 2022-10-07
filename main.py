# A start to represent the various objects for a scheduler.
# Structurally, the idea is to have to have Day, Role, and Employee objects
# that exist indepentaly of one another.

# The goal being: as they tie together, to allow for retrieval of specific, combined data
# to be used in further calculations.

import datetime, random

class Day:
	''' A 'Day' object that contains a date, and space for roles to be assigned to Day'''
	def __init__(self, datetimeObject, roles=[]):
		self.name = datetimeObject.weekday() # int representing day of the week, 0: Monday, 6: Sunday
		self.date = datetimeObject # datetime object.
		self.roles = roles # space to assign the roles of that day

class Role:
	'''There are several roles at the restaurant. Each role has attributes such as:\n
	 a name, shift call time, and an assignable employee.'''
	def __init__(self, name, callTime=None, employee=None): 
		self.name = name

		#TODO: Add calltimes for all roles
		#default values for calTime based on role:
		callTimes = {
			'lunch': datetime.time(hour=10, minute=30),
			'brunch':datetime.time(hour=10, minute=30),
			'bbar': datetime.time(hour=16, minute=30),
			'vbar': datetime.time(hour=16, minute=30),
			'middle': datetime.time(hour=18),
			'back': datetime.time(hour=18),
			'veranda': datetime.time(hour=16, minute=30),
			'front': datetime.time(hour=16, minute=30),
			'aux': datetime.time(hour=18),
			'shermans': datetime.time(hour=16, minute=30)
		}
		self.callTime = callTimes.get(name, callTime)
		if self.callTime is None:
			raise ValueError('Provide recognized role name or call time.')
		self.employee = employee

# a list of current roles at the restaurant
roles = [
	Role('lunch'),
	Role('brunch'),
	Role('bbar'),
	Role('vbar'),
	Role('middle'),
	Role('back'),
	Role('veranda'),
	Role('front'),
	Role('aux'),
	Role('shermans')
	]

class Employee:
	'''There are employees of the restaurant. an employee at Kiki's has a name,
and an amount of shifts they can work in a week.'''
	def __init__(self, name, numberOfShifts, avaliablity=[]):
		self.name = name
		self.numberOfShifts = numberOfShifts # number of shifts they can work this week
		self.avaliablity = avaliablity # a list of the employee's avalability for the week

employee1 = Employee(name='Dr. DeSpencer', numberOfShifts=4)
#Employee1's requests for the week are:
# Monday no Lunch, Wednesday no Lunch, and Saturday no Eve.
# Monday = workWeek[0].replace(hour=16, minute=30)

employee2 = Employee(name='Mea Culpa', numberOfShifts=5)
#employee2's requests for the week are:
#Tuesday and Wednesday off, Sunday no Brunch.

employee3 = Employee(name='The Protagonist', numberOfShifts=3)
#employee3's requests for the week are:
#Tuesday no eve, Thursday no eve, Friday and Saturday off.

employee4 = Employee(name='Deckard Cain', numberOfShifts=5)
#employee4's requests for the week are:
# Lunch on Monday Tuesday and Wednesday. Thursday no lunch, Aux Friday, and off Sunday.

employees = [employee1, employee2, employee3, employee4]
# A list of Employee objects to be assigned to Roles throughout the workWeek.
 

monday = Day(datetime.datetime(2022,10,3)) # this is Monday, Oct 3rd.


def createWeek(day):
	'''Create a list of seven consecutive Day objects from the given start day.\n
	arg = Day object.\n
	returns: List'''

	week = []
	for i in range(7):
		nextDay = Day((day.date + datetime.timedelta(days=i)))
		week.append(nextDay)
	return week

workWeek = createWeek(monday) # Seven day workWeek, starting from Monday, Oct 3rd.

def assignRolesToDays(workWeek):
	''' Assigns the list of roles to each day in the workWeek'''
	for day in workWeek:
		day.roles = roles
	return workWeek

weekAndRoles = assignRolesToDays(workWeek)

def createSchedule(workWeek, employees):
	'''assigns an employee to each role in each day of the week'''
	for day in workWeek:
		#for each role, assign an employee
		for role in day.roles:
			role.employee = random.choice(employees)

createSchedule(weekAndRoles, employees)

for day in weekAndRoles:
	print(day.date)
	for role in day.roles:
		print(role.name)
		print(role.callTime)
		print(role.employee.name, end='\n\n')

def getPossibleRoles(roles, avaliablity):
		"""
	roles: list of all Roles that must be staffed during a single day
			each Role has a callTime (start of shift), assume 6 hour shift
	availability: list of start/stop times indicating an employee's availability
			on that same day. Even indices represent start times, odds stop times
			every time is a date
			e.g. [time1, time2] means the employee is available from time1-time2
			e.g. [time1, time2, time3] means the employee is available from time-time2
				and from time3 until the end of the day
	"""