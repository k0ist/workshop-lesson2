def find_min(a):
    return min(a)


def main():
    length = int(input("Enter the length of your array: "))
    a = [0] * length
    for i in range(length):
        a[i] = int(input())
    print("Minimum of array is", find_max(a))


main()