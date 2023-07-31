#팩토리얼
def factorial(num):
    if num == 0:
        return 1
    return num*factorial(num-1)

def main():
    print(factorial(5)) # should return 120

if __name__ == "__main__":
    main()