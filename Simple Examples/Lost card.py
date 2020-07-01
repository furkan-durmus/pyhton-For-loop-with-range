# There was a set of cards with numbers from 1 to N. One of the card is now lost.
# Determine the number on that lost card given the numbers for the remaining cards.
# Given a number N, followed by N − 1 integers - representing the numbers on the remaining cards (distinct integers in the range from 1 to N).
# Find and print the number on the lost card.


lost=0
n=int(input())
sum=n * (n + 1) // 2

for i in range(n-1):
    lost+=int(input())
print(sum-lost) 