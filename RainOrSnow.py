def getInput(Weather):
    while True:
        data = input(f"Enter (Yes/No) for {Weather}").lower()
        if data == 'yes' or data == 'no':
            return data

rain = getInput("Raining")
snow = getInput("Snowing")
if snow == "yes" or rain == "yes":
    print("True")