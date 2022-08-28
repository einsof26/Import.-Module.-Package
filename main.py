from accounting.db.people import get_employees
from accounting.salary import calculate_salary
from datetime import datetime

def main():
    get_employees()
    calculate_salary()
    print(f'We are in  {datetime.now() }')



if __name__ == '__main__':
    main()
