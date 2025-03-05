
## '''write a program that input a number 'n' and displays the letter 's' from to 1 to n number of times,
# in a particulate style.Give a relevant messages while taking input and displaying output Ex, if the number is 4, then the output should be
#     : s
#       ss
#       sss
#       ssss
# '''

#input from the user
n = int(input("Enter a number: "))
# Loop to print 'S' in a staircase pattern
for i in range(1, n + 1):
# Print 's' i times
    print("s" * i)
# Print 's' i times


