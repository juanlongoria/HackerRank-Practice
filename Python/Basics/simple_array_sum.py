def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':
    ar_count = int(input("Enter number of elements: ").strip())
    ar = list(map(int, input("Enter numbers separated by space: ").rstrip().split()))
    result = simpleArraySum(ar)
    print("Sum:", result)
