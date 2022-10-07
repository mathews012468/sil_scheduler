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

		#default values for calTime based on role:
		callTimes = {
			'lunch': datetime.time(hour=10, minute=30),
			'front': datetime.time(hour=16, minute=30),
			'aux': datetime.time(hour=18),
			'shermans': datetime.time(hour=16, minute=30)
		}
		self.callTime = callTimes.get(name, callTime)
		if self.callTime is None:
			raise ValueError('Provide recognized role name or call time.')
		self.employee = employee

class Employee:
	'''There are employees of the restaurant. an employee at Kiki's has a name,
and an amount of shifts they can work in a week.'''
	def __init__(self, name, numberOfShifts, avaliablity=[]):
		self.name = name
		self.numberOfShifts = numberOfShifts # number of shifts they can work this week
		self.avaliablity = avaliablity # a list of the employee's avalability for the week

	# This requests idea is too far a reach while the core objects,
	# Days, Roles, and Employees are not yet sorted out. Can be ignored for now
	def requests(self):
		''' An attempt to figure out how to store employee requests\n
		using employee1's requests (see below) as an example'''
		monday = self.avaliablity[0].replace(hour=16, minute=30) # avaliable from 16:30 on
		tuesday = self.avaliablity[1] # open avaliablity on Tuesday
		Wednesday = self.avaliablity[2].replace(hour=16, minute=30) # same as monday
		#..
		#..
		saturday = self.avaliablity[5] # a timedelta object? how to get the duration of 
		# 'avaliable between 10:30am-4:30pm'?

#The idea is to have the callTime indepenant of a date at role creation, and ideally, once a role is 'assigned'-
# to a Day object, be able to 'retrieve a concrete Date + Time' object useable in further calculations
# e.g: endTime - callTime = hours worked

front = Role(name='Front', callTime = datetime.time(hour=16))
lunch = Role(name='Lunch', callTime = datetime.time(hour=10, minute=30))
aux = Role(name='Aux', callTime = datetime.time(hour=18))
shermans = Role(name='Shermans', callTime=datetime.time(hour=16, minute=30))
bbar = Role(name='BBar',callTime=datetime.time(hour=16, minute=30))
middle = Role(name='Middle', callTime=datetime.time(hour=18))
back = Role(name='Back', callTime=datetime.time(hour=18))
brunch = Role(name='Brunch', callTime=datetime.time(hour=10, minute=30))

roles = [front, lunch, aux, shermans, bbar, middle, back, brunch]
# A list of roles objects, ready to be tied to Day objects

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



def createWeek(day):
	'''Create a 7 day week from the given start day.\n
	arg = Day object.\n
	returns: List'''

	week = []
	for i in range(7):
		nextDay = Day((day.date + datetime.timedelta(days=i)))
		week.append(nextDay)
	return week

monday = Day(datetime.datetime(2022,10,3)) # this is Monday, Oct 3rd.

workWeek = createWeek(monday) # A list of seven consecutive Day objects.
for day in workWeek:
	day.roles = [Role('front'), Role('lunch'), Role('aux'), Role('shermans')]

def createSchedule(workWeek, employees):
	for day in workWeek:
		#for each role, assign an employee
		for role in day.roles:
			role.employee = random.choice(employees)

createSchedule(workWeek, employees)

for day in workWeek:
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



# # Old code that the above code grew from.
# # Question: Is this part of what 'version control' can be used for?
# # to keep a document focused while previously written code remains accessible?

# monday = datetime.datetime(2022,10,3) # this is Monday, Oct 3rd.

# def weekOf(startDate):
# 	'''Create a 7 day week from the given startDate.

# 	arg = datetime.datetime object.

# 	returns Week as a list object'''
# 	week = []
# 	for i in range(7):
# 		nextDay = [startDate + datetime.timedelta(days=(i))]
# 		week.append(nextDay)
# 	return week

# week = weekOf(monday) # The week of Monday, Oct 3rd.
# #The idea here is to represent 'a week made up of days',
# #to create a space for roles to be assinged to each day.

# def scheduleTemplate(week,roles):
# 	""" Appends a list of roles into each day of the week
# 	returning a 'scheduleTemplate'"""
# 	for i in range(len(week)):
# 		week[i].append(roles)
# 	return week

# workWeek = scheduleTemplate(week, roles)
# #This is the attempt at 'tieing' the roles onto each day of the week
# #Though now that it's here- this is messy and not the desired outcome.