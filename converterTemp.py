def converter(celsius):
    msg_1 = " degrees Celsius are "
    msg_2 = " degrees Farenheit."
    farenheit = (celsius * 9/5) + 32
    return str(celsius) + msg_1 + str(farenheit) + msg_2

user_input = input( "Enter a themperature in Celsius: ")
farenheit_result = converter(float(user_input))

if (float(user_input)) > 38:
    print("Its realllly hot!")

print (farenheit_result)


# I am adding some comments here so that I can track them