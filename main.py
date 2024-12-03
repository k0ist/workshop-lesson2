def find_max(a):
    return max(a)


def main():
    length = int(input("Enter the length of your array: "))
    a = [0] * length
    for i in range(length):
        a[i] = int(input())
    print("Maximum of array is", find_max(a))


main()