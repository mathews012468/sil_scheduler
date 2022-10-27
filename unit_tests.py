import main

#test shifts remaining
#inputs: Employee, schedule
#Employee: name, max_shifts, availability
#Employee.name: str
#Employee.max_shifts: int (nonnegative number)
#Employee.availability: dict Weekday(Enum): set(role names, which are strings)
#schedule: list(dict "role": Role, "employee": Employee)

def test1():
    """
    return True if test passes
    """
    availability1 = {
        main.Weekday.MONDAY: {"aux", "lunch", "back"}
    }
    employee1 = main.Employee(name="Sil", max_shifts=5, availability=availability1)
    employee2 = main.Employee(name="Ashlynn", max_shifts=7, availability=availability1)
    schedule = [
        {
            "role": main.Role(name="aux", day=main.Weekday.MONDAY),
            "employee": employee1
        },
        {
            "role": main.Role(name="lunch", day=main.Weekday.MONDAY),
            "employee": employee2
        }
    ]

    return employee1.shiftsRemaining(schedule) == 4

if __name__ == "__main__":
    #run all tests
    test1()