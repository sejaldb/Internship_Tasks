from solutions import (
    frequency_of_word, frequency_of_char, single_char, isAnagram,
    first_repeating_char, zeroes_at_end, second_highest_distinct, remove_dup,
    missing_num, two_sum, near_zero, common,
    rotate_right, max_sum, pairs
)
print("Q1:", frequency_of_word("python is easy and python is powerful"))
print("Q1 additional:", frequency_of_word("hi hi bye"))

print("Q2:", frequency_of_char("banana"))
print("Q2 additional:", frequency_of_char("apple"))

print("Q3:", single_char("swiss"))
print("Q3 additional:", single_char("aabb"))

print("Q4:", isAnagram("listen", "silent"))
print("Q4 additional:", isAnagram("hello", "world"))

print("Q5:", first_repeating_char("programming"))
print("Q5 additional:", first_repeating_char("abcda"))

print("Q6:", zeroes_at_end([0, 3, 0, 1, 2, 0, 4]))
print("Q6 additional:", zeroes_at_end([1, 0, 2]))

print("Q7:", second_highest_distinct([10, 20, 40, 30, 40, 20]))
print("Q7 additional:", second_highest_distinct([5, 5, 5]))

print("Q8:", remove_dup([4, 2, 4, 5, 2, 7, 5]))
print("Q8 additional:", remove_dup([1, 1, 2, 3, 2]))

print("Q9:", missing_num([1, 2, 4, 5, 6], 6))
print("Q9 additional:", missing_num([1, 3, 4], 4))

print("Q10:", two_sum([2, 7, 11, 15], 9))
print("Q10 additional:", two_sum([3, 2, 4], 6))

print("Q11:", near_zero([-8, -3, 2, 5, -2]))
print("Q11 additional:", near_zero([-1, 1, 4]))

print("Q12:", common([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print("Q12 additional:", common([2, 2, 3, 1], [1, 2]))

print("Q13:", rotate_right([1, 2, 3, 4, 5], 2))
print("Q13 additional:", rotate_right([1, 2, 3], 0))

print("Q14:", max_sum([4, 7, 2, 9, 5]))
print("Q14 additional:", max_sum([-3, -1, -5]))

print("Q15:", pairs([2, 4, 3, 5, 7, 8, 1], 9))
print("Q15 additional:", pairs([1, 2, 3, 4], 20))

