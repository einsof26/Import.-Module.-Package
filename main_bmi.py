from py_bmi import bmi

def main():
    weight = input("Enter your weight in kg: ")
    height = input("Enter your height in m: ")
    print(bmi(weight, height))

if __name__ == '__main__':
    main()