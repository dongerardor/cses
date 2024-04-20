def solution(arr, N, X):
    d = {}
    bandera = True

    for i in range(N):
        if bandera:
            if X - arr[i] in d:
                print(d[X - arr[i]] + 1, i + 1)
                bandera = False
            d[arr[i]] = i
    if bandera:
        print("IMPOSSIBLE")

lengh, total = map(int, input().split())
values = list(map(int, input().split()))

solution(values, lengh, total)


def solve(arr, N, X):
    # Create an empty dictionary to store the index of elements
    # as keys and their corresponding positions as values
    m1 = {}
    # Initialize a flag to track if a pair is found
    flag = True

    # Iterate through the array
    for i in range(N):
        # Check if the flag is still True
        if flag:
            # If the complement of the current element (X - arr[i])
            # exists in the dictionary, it means a pair is found
            if X - arr[i] in m1:
                # Print the indices of the pair
                print(m1[X - arr[i]] + 1, i + 1)
                # Set the flag to False to indicate that a pair is found
                flag = False
            # Store the current element and its index in the dictionary
            m1[arr[i]] = i
    # If no pair is found, print "IMPOSSIBLE"
    if flag:
        print("IMPOSSIBLE")
