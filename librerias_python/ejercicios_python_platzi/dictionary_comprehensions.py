import math

def run():
    # my_dict = {i: i**3  for i in range(1,101) if i%3 != 0}
    # print(my_dict)

    my_dict2 = {i: round(math.sqrt(i), 4) for i in range(0,1001)}
    print(my_dict2)

if __name__ == "__main__":
    run()