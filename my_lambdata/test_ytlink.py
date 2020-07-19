from my_lambdata.ds_utilities import ytlink


print("Ready to create your link...")
print()
l = input("Please enter the link to the YouTube video: ")
h = int(input("Please enter the hour in the timemark: "))
m = int(input("Please enter the minutes in the timemark: "))
s = int(input("Please enter the seconds in the timemark: "))
print()

result = ytlink(l, h, m, s)
print(result)
print()
print()
