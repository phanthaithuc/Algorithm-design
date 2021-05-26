#
#
# The most prestigious sports club in one city has exactly N members.
# Each of its members is strong and beautiful.
# precisely, i-th member of this club (members being numbered by the time they entered the club) has strength Si and beauty Bi .
# Since this is a very prestigious club, its members are very rich and therefore extraordinary people, so they often extremely hate each other.
# Strictly speaking, i-th member of the club Mr X hates j-th member of the club Mr Y if Si ≤ Sj and Bi ≥ Bj or if Si ≥ Sj and Bi ≤ Bj (if both properties of Mr X are greater then corresponding properties of Mr Y, he doesn't even notice him, on the other hand, if both of his properties are less, he respects Mr Y very much).
#
# To celebrate a new 2003 year, the administration of the club is planning to organize a party.
# However they are afraid that if two people who hate each other would simultaneouly attend the party, after a drink or two they would start a fight. So no two people who hate each other should be invited. On the other hand, to keep the club presti≥ at the apropriate level, administration wants to invite as many people as possible.
#
# Being the only one among administration who is not afraid of touching a computer, you are to write a program which would find out whom to invite to the party.
#
# Input
#
# The first line of the input file contains integer N — the number of members of the club. ( 2 ≤ N ≤ 100,000 ). Next N lines contain two numbers each — Si and Bi respectively ( 1 ≤ Si, Bi ≤ 109 ).
#
# Output
#
# On the first line of the output file print the maximum number of the people
# that can be invited to the party. On the second line output N integers — numbers of members to be invited in arbitrary order. If several solutions exist, output any one.


# Python3 implementation of the approach

# helper function which returns the sum
# of series (1^2 + 2^2 +...+ n^2)
def squareSeries(n):
    return (n * (n + 1) * (2 * n + 1)) // 6


# maxPeople function which returns
# appropriate value using Binary Search
# in O(logn)

def maxPeople(n):
    # Set the lower and higher values
    low = 0
    high = 1000000000000000
    while low <= high:

        # calculate the mid using
        # low and high

        mid = low + ((high - low) // 2)
        value = squareSeries(mid)

        # compare value with n
        if value <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    # return the ans
    return ans


if __name__ == '__main__':
    p = 14
    print(maxPeople(p))

# This code is contributed bu chaudhary_19
# (* Mayank Chaudhary)