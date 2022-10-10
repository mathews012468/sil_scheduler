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
			'lunch': '10:30 AM',
			'brunch': '10:30 AM',
			'bbar': '4:30 PM',
			'vbar': '4:30 PM',
			'middle': '6:00 PM',
			'back': '6:00 PM',
			'veranda': '4:30 PM',
			'front': '4:30 PM',
			'aux': '6:00 PM',
			'shermans': '4:30 PM',
			'swing': '1:00 PM'
		}
		self.callTime = callTimes.get(name, callTime)
		if self.callTime is None:
			raise ValueError('Provide recognized role name or call time.')
		self.employee = employee

# a list representing all current roles with Role objects
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
	Role('shermans'),
	Role('swing')
	]


#TODO: I'd like avaliabity to be a set of all role callTimes, referenced from the Roles class
# where they are defined, so that it's 'neat' / coming from a single source. How do I set that up?
roleCallTimes = []
for role in roles:
	roleCallTimes.append(role.callTime)

# The idea is to have an employee week that lines up wit the workWeek list of day objects.
# Then when we're in day object 0, workweek[0], there's a date that matches with the employee's
# avalabilit[0].

#The idea here is to have a list of seven sets of call times that mimics the structure of
# the workWeek, where workWeek[0] is monday, and availability[0] is the employee's availability for
# monday as well.
availability = []
for _ in range(7):
	availability.append(list(set(roleCallTimes)))

manualSorted = []
for _ in range(7):
	manualSorted.append(['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'])

#for day in manualSorted:
	#print(f'HEADER DATE')
	#print('Select shifts you are unavailable for:')
	#for i in range(len(day)):
	#	print(f'{i}: {day[i]}')
	#input()

#TODO: Create input menu function
	#takes arguement list, and for each item in the list, allows user to select an option
	#that option is then returned and can be captured as input.

#TODO: Set up a 'main()' function for the code will step through

#GOAL: Have the above done, by Wednesday, 3pm. To send to Mat to be ready for refactoring and orginization.


class Employee:
	'''There are employees of the restaurant. an employee at Kiki's has a name,
and an amount of shifts they can work in a week.'''
	def __init__(self, name, numberOfShifts, availability=manualSorted):
		self.name = name
		self.numberOfShifts = numberOfShifts # number of shifts they can work this week
		self.availability = availability # a list of the employee's avalability for the week

employee1 = Employee(name='Dr. DeSpencer', numberOfShifts=4, availability=[
	['4:30 PM', '6:00 PM'], # Monday
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'], # Tuesday
	['4:30 PM', '6:00 PM'], # Wednesday
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'], # Thursday
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'], # Friday
	['10:30 AM', '1:00 PM'], # Saturday
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'] # Sunday
	])
#Employee1's requests for the week are:
# Monday no Lunch, Wednesday no Lunch, and Saturday no Eve.

employee2 = Employee(name='Mea Culpa', numberOfShifts=5, availability=[
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'], # Monday
	[], # Tuesday
	[], # Wednesday
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'], # Thursday
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'], # Friday
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'], # Saturday
	['1:00 PM', '4:30 PM', '6:00 PM'] # Sunday
	])
#employee2's requests for the week are:
#Tuesday and Wednesday off, Sunday no Brunch.

employee3 = Employee(name='The Protagonist', numberOfShifts=3, availability=[
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'], # Monday
	['10:30 AM', '1:00 PM'], # Tuesday
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'], # Wednesday
	['10:30 AM', '1:00 PM'], # Thursday
	[], # Friday
	[], # Saturday
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'] # Sunday
	])
#employee3's requests for the week are:
#Tuesday no eve, Thursday no eve, Friday and Saturday off.

employee4 = Employee(name='Deckard Cain', numberOfShifts=5, availability=[
	['10:30 AM'], # Monday
	['10:30 AM'], # Tuesday
	['10:30 AM'], # Wednesday
	['4:30 PM', '6:00 PM'], # Thursday
	['6:00 PM'], # Friday
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'], # Saturday
	[] # Sunday
	])
#employee4's requests for the week are:
# Lunch on Monday Tuesday and Wednesday. Thursday no lunch, Aux Friday, and off Sunday.

employee5 = Employee(name='Cliff Booth', numberOfShifts=4, availability=[
	['4:30 PM', '6:00 PM'], # Monday
	['4:30 PM', '6:00 PM'], # Tuesday
	['10:30 AM', '1:00 PM'], # Wednesday
	['10:30 AM', '1:00 PM'], # Thursday
	['10:30 AM', '1:00 PM'], # Friday
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'], # Saturday
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'] # Sunday
	])
#employee5's requests are:
# No lunch or swing Monday and Tuesday. No eve Wed, Thur, Fri
employee6 = Employee(name='The Humungus', numberOfShifts=6, availability=[
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'], # Monday
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'], # Tuesday
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'], # Wednesday
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'], # Thursday
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'], # Friday
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'], # Saturday
	['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'] # Sunday
	])
#No requests

employees = [employee1, employee2, employee3, employee4, employee5, employee6]
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

# For the moment, all roles get assigned to each day,
#TODO: Think about which days get which roles, and why.
	# Is it static?
	# How do I want this represented?
def assignRolesToDays(workWeek):
	''' Assigns the list of roles to each day in the workWeek'''
	for day in workWeek:
		day.roles = roles
	return workWeek

weekWithRoles = assignRolesToDays(workWeek)

def createSchedule(workWeek, employees):
	'''assigns an employee to each role in each day of the week'''
	for day in workWeek:
		print(f'{day.date}')
		for role in day.roles:
			callTime = role.callTime
			print(f'{role.name}: {callTime}')
			matchPool = [] #find employees who are eligable for the current role
			for employee in employees: # for each employee the list
				for avail in employee.availability[day.name]: # get availabilty for that employee's day
					if callTime in avail:
						matchPool.append(employee.name) # add employee to match pool
			print(f'{matchPool}')
			role.employee = random.choice(matchPool) # random.choice from pool of matches
			print(f'{role.employee}')
			input()
			


schedule = createSchedule(weekWithRoles, employees)



#for day in weekWithRoles:
#	print(day.date)
#	for role in day.roles:
#		print(role.name)
#		print(role.callTime)
#		print(role.employee.name, end='\n\n')


# def getPossibleRoles(roles, avaliablity):
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

# we're in this current day (Day object), and with this current role.
# from this day there's also a matching employee pool.
# this day object, there are employees assigned to it.
# All the employees?
# Assign employees to Days? hold on.
# No it's that this Day object contains a list of roles to be filled, yes
# This employee object contains employee data.
# There is a shared connection, to a day.
# A Day object contains roles, yes
# The Day object also shares an identitfier with the employee object
# The employee pool is part of the day.
# Yes, the employee pool is part of the day. by default.
# without a request
# each employee is part of the day as Roles are part of the day.
# with the list of employees, next to the title of the Day, the datetime object
# sharing an identifier with the datetime object is different than sittig next to the datetime object.
# I think what I may be interested in, is sharing the same 'identinfier' of the object
# when thinking of the employee's avaliabiliy for the day. yes
# is this possible.


#Once we're in the date
