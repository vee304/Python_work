
def pali(i, arr):
    n = len(arr)
    while i >= n//2:

        if arr[i] != arr[n-i-1]:
            return print("it's not a palindrome")
        pali(i+1, arr)
    return print("It's Palindrome")

word = "DETARTRATED"
arr = list(word)

pali(0, arr)