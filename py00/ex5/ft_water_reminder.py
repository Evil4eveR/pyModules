def ft_water_reminder():
    p = input("Days since last watering:")
    if(int(p) > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
