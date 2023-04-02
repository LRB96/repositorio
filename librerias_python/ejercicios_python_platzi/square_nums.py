def run():
    
    squares = [i**2 for i in range(0,1000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(squares)
        
# def run():
#     for i in range(0, 101):
#         if i % 3 != 0:
#             print(str(i) + " al cuadrado es: " + str((i**2)))

if __name__ == "__main__":
    run()