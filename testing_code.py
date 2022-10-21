import main
import ast

def extract_data(file_line):
    return line.split("-")[1].strip()

#load input file
with open("testing/input/employee1.txt") as f:
    employees = []
    while line := f.readline():
        if line.startswith("Employee"):
            name = extract_data(line)

            #max shifts is on next line after colon
            line = f.readline()
            max_shifts = extract_data(line)

            week_availability = []
            for _ in range(7):
                line = f.readline()
                availability_list_str = extract_data(line)
                #turn the availability list (str) into an actual list
                #not using json.loads because it doesn't work well with
                #lists of strings
                availability_list = ast.literal_eval(availability_list_str)
                week_availability.append(availability_list)
            
            employees.append([name,max_shifts,availability_list])

with open("testing/input/role1.txt") as f:
    roles = []
    while line := f.readline():
        if line.startswith("Day"):
            day = extract_data(line)

            line = f.readline()
            role = extract_data(line)

            line = f.readline()
            calltime = extract_data(line)

            roles.append([day, role, calltime])

role_objs = []
for role in roles:
    role_name = role[1]
    day = role[0]
    calltime = role[2]

    new_role = main.Role(name=role_name, day=day)
    role_objs.append(new_role)

print(role_objs)
print(employees)
print(f'roles list:{roles}\n')