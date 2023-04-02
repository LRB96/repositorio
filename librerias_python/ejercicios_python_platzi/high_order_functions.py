from functools import reduce



def run():
    # my_list = range(1,6)
    # squares = [i**2 for i in my_list]
    # print(squares)
    
    # squares2 = list(map(lambda x: x**2, my_list))
    # print(squares2)

    my_list2 = [2,2,2,2,2]
    all_multiplied = reduce(lambda a,b: a * b, my_list2)
    print(all_multiplied)



if __name__ == "__main__":
    run()