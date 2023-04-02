def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(13)

if __name__ == "__main__":
    fibonacci(13)