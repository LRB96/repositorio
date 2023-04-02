def remove_duplicates(some_list):
    return list(set(some_list))

def run():
    list = [1,1,2,2,4,5,5,6]
    print(remove_duplicates(list))

if __name__ == "__main__":
    run()

