def recu(d):
    if(d < 1):
        return 0
    recu(d-1)
    print("Day", d)
    
def ft_count_harvest_recursive():
    days = input("Days until harvest:")
    recu(int(days))
    print("Harvest time!")
