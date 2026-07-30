def temperature_value(celsius):
   
    fahrenheit = celsius * 9 / 5 + 32

    celsius = fahrenheit - 32 * 5 / 9


    threshold = 27

    if celsius < threshold:

        return "Cold advisory"
    else:

        return "Heat alert"




celsius = float(input("Enter celsius:"))
#fahrenheit = float(input("Enter fahrenheit:"))
print(temperature_value(celsius))
