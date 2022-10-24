# WIP: Scheduler for Kiki's restaurant

from enum import Enum

class Weekday(Enum):
	MONDAY = 0
	TUESDAY = 1
	WEDNESDAY = 2
	THURSDAY = 3
	FRIDAY = 4
	SATURDAY = 5
	SUNDAY = 6

class Day:
	#the appeal of a Day object seems again to have a container that day's roles.
	# having some reason or sense to the order of roles stored in a day is appealing-
	# for having a grasp on the steps taken in 'createSchedule'.
	# a space for a date is attractive too.
	def __init__(self, name, roles, date=None):
		self.name = name # enum of weekday
		self.date = date #date object?
		
		# This mimics callTimes from Roles, with a few unelegant hitches.
		# copied all the roles from the current week's schedule-
		# a one-off specifc role of FMN that only a single employee can do.
		# multiple instances of 'brunch', 'lunch', 'door',
		# and an unelegant solution for 'shermans6pm'

		# I do like the idea of a day object knowing which roles to assign to itself with from a general 'role database'.
		# the idea being that the roles each day calls for can be exposed later as it can change week-to-week/month-to-month

		roles = {
			Weekday.MONDAY: {'lunch', 'swing', 'shermans', 'door', 'uber', 'vbar', 'bbar','front','veranda','outside','back','middle'},
			Weekday.TUESDAY: {'lunch', 'swing', 'FMN', 'shermans', 'shermans6pm', 'door', 'uber', 'vbar', 'bbar','front','veranda','outside','back','middle'},
			Weekday.WEDNESDAY: {'lunch', 'swing', 'shermans', 'door', 'uber', 'vbar', 'bbar','front','veranda','outside','back','middle'},
			Weekday.THURSDAY: {'lunch', 'swing', 'shermans','shermans2','shermans6pm','door','door2', 'uber', 'vbar', 'bbar','front','veranda','outside','back','middle'},
			Weekday.FRIDAY: {'lunch', 'lunch2', 'shermans','shermans2','shermans6pm', 'shermans6pm-2', 'door', 'door2','aux', 'uber', 'vbar', 'bbar','front','veranda','outside','back','middle'},
			Weekday.SATURDAY: {'door', 'door2', 'brunch_door', 'brunch1', 'brunch2', 'brunch3', 'shermans', 'shermans6pm_1', 'shermans6pm_2','veranda','front','outside','vbar','back','middle','uber'},
			Weekday.SUNDAY: {'door', 'brunch_door','shermans', 'front', 'bbar', 'vbar','shermans_2','brunch_1', 'brunch_2','outside','brunch_3','veranda','back','middle','uber'}
		}
		self.roles = roles.get(name, roles)

class Role:
	def __init__(self, name, day, callTime=None): 
		self.name = name

		#enum of weekday
		self.day = day
  
		#default values for callTime based on role:
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

class Employee:
	#max number of shifts
	#availability
	#for each role, aptitude
	#name
	def __init__(self, name, max_shifts, availability):
		self.name = name
		self.max_shifts = max_shifts
		self.availability = availability


	def shiftsRemaining(self, schedule):
		'''employee's shifts remaining is max_shifts - the number of shifts they are currently in the schedule for'''
		remainingShifts = self.max_shifts
		for shift in schedule:
			if self in shift:
				remainingShifts -= 1
		return remainingShifts

	"""
	{
		"Monday": {"Aux", "Lunch", "Eve"},
		"Tuesday": {"Lunch"},
		"Wednesday": None,
		"Thursday": None,
		"Friday": {"Aux", "Lunch", "Eve"},
		"Saturday": {"Aux", "Lunch", "Eve"},
		"Sunday": {"Aux", "Lunch"}
	}
	"""

def isDouble(employee, schedule, role): # How to think about consolidating the same use of arguements here?
	for grouping in schedule:
		if not grouping[0].day == role.day or not grouping[1].name == employee.name:
			return False
	return True

def can_take_on_role(employee, role, schedule=None): # Chaining the schedule in here to get it to 'shifts remaining' does not seem optimal.
													# TODO: fix this
	#number of shifts available > 0
	if not employee.shiftsRemaining(schedule) > 0:
		return False
	
	# employee must have availabilty for the role
	if role.name.lower() not in employee.availability[role.day]:
		return False
	
	return True

def employee_role_rank(employee, schedule, role): #Oh, maybe I could pass in the role_and_employees list directly, to consolidate arguments?
	employeeRank = 100
	#TODO highest aptitude for role

	if isDouble(employee, schedule, role):
		employeeRank -=80
	if employee.shiftsRemaining(schedule) <= 2:
		employeeRank -= 40
	# print(employee.name)
	# print(employeeRank)

	return employeeRank


#the desire is to create a 'schedule' for a single day.
# no, not quite. not to create a schedule in isolation. it 'can' be created for a single day or any number of days needed
# however, when an employee gets matches with a role- inserted into the schedule-
# this should definitely be taken into account i.e. 'employee role rank will change accordingly'
# so the sectioning of a day is desirable (why now?), while the full container of 'whatever number of days' a schedule is made of-
# is neccesary for apt decision making.

#this introduces the idea of a container of 'whatever number of days' the schedule is made of.
#that container, is for some reason what I long for.

#the Day objects have their place.
# for storing a list of roles, a name of the day, and a date.
# This container to allow for 'open' finding and matching employees is currently the empty list of week_schedule.
# This container seems important- more so than the simple definition it currently takes at the start of createSchedule.
# is that so?
def fillDay(day, employees):
	'''finds matches for each role in a Day'''
	#for roles in Day('monday').roles:
	#find possible employees for each role
	# store that possible list
	

	pass

def createSchedule(roles, employees):
	week_schedule = []
	for role in roles:
		#find all the available employees for role
		possible_employees = [employee for employee in employees if can_take_on_role(employee, role, week_schedule)]
		#assign the best employee for the role
		try:
			role_and_employee = (role, max(possible_employees, key=lambda employee: employee_role_rank(employee, week_schedule, role) ))
		except ValueError:
			role_and_employee = (role, Employee('Unassinged',99,{}))
		week_schedule.append(role_and_employee)

	return week_schedule

#Is this container of 'roles' the sticking point?
# I want this container to 'come from somewhere'
#The roles of a Day? A list of Days, each bringing their list of roles?
# What is this a representaion of?
# it's source is a list of roles, which come from Days- of which there can be n number of.
roles = [
	Role(name="lunch", day=Weekday(0)), 
	Role(name="back", day=Weekday(0)), 
	Role(name="aux", day=Weekday(0)),
	Role(name="lunch", day=Weekday(1))
]

employees = [
	Employee(
		name="Sil", 
		max_shifts=2,
		availability={
			Weekday(0): {"aux", "lunch", "eve"}, # Question: Why a set?
			Weekday(1): {"lunch"}
		}
	),
	Employee(
		name="Mathew",
		max_shifts=3,
		availability={
			Weekday(0): {"back"},
			Weekday(1): {}
		}
	),
	Employee(
		name="Ashlynn",
		max_shifts=4,
		availability={
			Weekday(0): {"lunch"},
			Weekday(1): {}
		}
	)
]

def scheduleView_Restaurant(schedule):
	'''print the schedule in 'Restaurant View' '''
	for i in range(7): # for the seven days of the week.
		headerDate= Weekday(i)
		print(f'{headerDate}')
		for grouping in schedule:
			role = grouping[0]
			employee = grouping[1]
			if role.day == headerDate:
				print(f'{role.name}: {employee.name}')

def scheduleView_SinglePerson(schedule, employee):
	'''print schedule for single person point of view '''
	print(employee.name)
	employeeShifts = sorted([grouping[0] for grouping in schedule if employee in grouping], key=lambda role: role.day.value)
	for role in employeeShifts:
		print(f'{role.day.name.capitalize()}- {role.name.capitalize()} {role.callTime}')
	
		
		
		# get weekday(i) role 
		# find monday's role and print it.
	# get all the roles assigned to this employee

	#print {Weekday(i)}: {role}, {callTime}
	pass

if __name__ == "__main__":
	weekly_schedule = createSchedule(roles, employees)

	# scheduleView_Restaurant(weekly_schedule)
	# scheduleView_SinglePerson(weekly_schedule,employees[0])