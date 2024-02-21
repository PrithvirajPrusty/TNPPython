days = int(input("Enter Days:"))
years = days // 365
months = (days-years*365) // 30
days = days - years*365 - months*30
print(f"Years: {years}")
print(f"Months:{months}")
print(f"Days:{days}")