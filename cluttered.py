# WIP: Schedular for Kiki's restaurant


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


#TODO: Avaliabity could be a Set of all role callTimes, referenced from a single source where they are defined
# currently in the Roles class
roleCallTimes = []
for role in roles:
	roleCallTimes.append(role.callTime)

availability = []
for _ in range(7):
	availability.append(list(set(roleCallTimes)))

manualSorted = [] # manual representation of a week's avaliablity.
for _ in range(7):
	manualSorted.append(['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM'])


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
# A list of all Employee objects.
 

def createWeek(day):
	'''Create a list of seven consecutive Day objects from the given start day.\n
	arg = Day object.\n
	returns: List'''

	week = []
	for i in range(7):
		nextDay = Day((day.date + datetime.timedelta(days=i)))
		week.append(nextDay)
	return week

def assignRolesToDays(workWeek):
	''' Assigns all roles to each day of the week'''
	for day in workWeek:
		day.roles = roles
	return workWeek

#TODO: Storing an employee's requests:
	# a function that could take input() and return an employee's requests for the week.
def requests(week):
	'''Creates a week's availability with user input'''
	#Display date and start times for the date.
	startTimes = ['10:30 AM', '1:00 PM', '4:30 PM', '6:00 PM']
	for day in week:
		print(f'{day.date}')
		for num, time in enumerate(startTimes):
			print(f'{num}: {time}')
		input()

#There is a frusteration with the way this function is written
#It seems quite tangled and fragile- hard to add anything to it. Such as an employee's 'numberOfShifts',
# or future ideas of 'aptitude' for roles.
def createSchedule(workWeek, employees):
	'''Assigns employees to each role in the week, based on employee's availability '''
	for day in workWeek: # Day object in workWeek
		print(f'{day.date}')
		for role in day.roles: # list of roles in the Day object.
			callTime = role.callTime
			print(f'{role.name}: {callTime}')
			matchPool = [] # find employees who are eligable for the current role
			for employee in employees: # employee object in list of employees
				if callTime in employee.availability[day.name]: # get the day's availabilty from employee
					matchPool.append(employee.name) # add employee to match pool
			print(f'{matchPool}')
			role.employee = random.choice(matchPool) # random.choice from pool of matches
			print(f'{role.employee}')


def main(startDate):
	workWeek = createWeek(startDate) # list of seven consecutive Day objects from startDate
	weekWithRoles = assignRolesToDays(workWeek) # Assigns all roles to each Day object of the workWeek

	createSchedule(weekWithRoles, employees) 



monday = Day(datetime.datetime(2022,10,3)) # this is Monday, Oct 3rd.
main(monday)

