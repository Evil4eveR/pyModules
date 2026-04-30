import sys


def parse_parameters(parameters: list) -> dict:
    inventory = {}
    for par in parameters:
        if(":" not in par):
            print(f"Error - invalid parameter '{par}'")
            continue
        parts = par.split(":",1)
        key = parts[0]
        val = parts[1]
        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            inventory[key] = int(val)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
    return inventory


def main():
    arguments = sys.argv[1:]
    dic = parse_parameters(arguments)
    print(f"Got inventory: {dic}")
    print(f"Item list: {[item for item in dic.keys()]}")
    print(f"Total quantity of {len(dic.keys())} items: {sum(dic.values())}")
    for key,val in dic.items():
        print(f"Item {key} represents {round((val*100)/sum(dic.values()),1)}%")
    dic_min = list(dic.keys())[0]
    dic_max = list(dic.keys())[0]

    for key in dic.keys():
        if dic[key] < dic[dic_min]:
            dic_min = key
        if dic[key] > dic[dic_max]:
            dic_max = key
    print(f"Item most abundant: {dic_max} with quantity {max(dic.values())}")
    print(f"Item least abundant: {dic_min} with quantity {min(dic.values())}")
    dic.update({"magic_item": 1})
    print(f"Updated inventory: {dic}")
    # item_list = []
    # quantity_list = []
    # for x,y in dic.items():
    #     item_list.append(x)
    #     quantity_list.append(y)
    # print(f"Item list: {item_list}")
    # print(f"Total quantity of the {len(item_list)} items: {sum(quantity_list)}")
    # for key,val in dic.items():
    #     print(f"Item {key} represents {round((val*100)/sum(quantity_list),1)}%")
    # print(f"Item most abundant: {"dic[]"} with quantity {max(quantity_list)}")
    # print(f"Item least abundant: {"dic[]"} with quantity {min(quantity_list)}")
    # dic.update({"magic_item": int("1")})
    # print(f"Updated inventory: {dic}")
if __name__ == "__main__":
    main()
