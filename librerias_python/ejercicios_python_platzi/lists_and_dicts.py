def run():

    my_list = [1, "hello", 4.5, True]
    my_dist = {"firstname": "Luis", "lastname": "Rojas"}

    my_super_list = [
        {"firstname": "Luis", "lastname": "Rojas"},
        {"firstname": "Felipe", "lastname": "Andrade"},
        {"firstname": "Andres", "lastname": "Gomez"},
        {"firstname": "Otto", "lastname": "Bismark"}
    ]

    my_super_dict = {
        "natural_numbers": [1,2,3,4,5],
        "integer_nums": [-2,-1,0,1,2],
        "floating_nums": [1.3,1.5,6.7,7.8]
    }

    for key, value in my_super_dict.items():
        print(key, "-", value)

    for n in my_super_list:
        print(n)

if __name__ == "__main__":
    run()