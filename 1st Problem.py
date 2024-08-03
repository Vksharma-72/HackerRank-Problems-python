# Task
# Given an integer,n, perform the following conditional actions:
#
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5 , print Not Weird
# If n is even and in the inclusive range of 6 to 20b , print Weird
# If n is even and greater than 20 , print Not Weird

if __name__ == '__main__':
    n = int(input().strip())
    odd_even = n % 2
    if odd_even == 1:
        print("Weird")
    elif odd_even == 0 and 2 < n < 5:
        print("Not Weird")
    elif odd_even == 0 and 6 < n < 20:
        print("Weird")
    elif odd_even == 0 and 20 <= n:
        print("Not Weird")
