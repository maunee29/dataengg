
def salarysum(file,):

    # Initializing a dictionary to store the final sum of salaries by department name
    sumSalary_by_dept_name = {}

    # Split into lines
    lines = file.strip().split('\n')
    
    # Make the first row the headers for the "table" and rest the data
    header = lines[0].split(',')
    data = [line.split(',') for line in lines[1:]]

    # Calculate sum of salaries
    for line in data:
        dept_name = line[1].strip()
        salary = int(line[4].strip())

        if dept_name in sumSalary_by_dept_name:
            sumSalary_by_dept_name[dept_name] += salary
        else:
            sumSalary_by_dept_name[dept_name] = salary

    return sumSalary_by_dept_name


if __name__ == "__main__":

    inputFile = input("Enter file path: ")

    try:
        with open(inputFile, 'r') as files:
            file = files.read()

    # Call function to calculate sum
        sumSalary_by_dept_name = salarysum(file)

    # Display result
        print("Sum of salaries by department name: ")
        for dept_name, salary in sorted(sumSalary_by_dept_name.items()):
            print(f"{dept_name}: {salary}")

    except FileNotFoundError:
        print("Error! File not found")
