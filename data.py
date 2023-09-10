# Question 1: Check for balanced parentheses, curly braces, and square brackets
def is_balanced(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != brackets[char]:
                return False

    return not stack

# Question 2: Remove duplicates from a sequence while maintaining order
def remove_duplicates(sequence):
    seen = set()
    result = []

    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

# Question 3: Count word frequency in a sentence (case-insensitive, ignore punctuation)
import re
from collections import Counter

def word_frequency(sentence):
    words = re.findall(r'\w+', sentence.lower())
    return dict(Counter(words))

# Testing the functions
if __name__ == "__main__":
    expression1 = "([]{})"
    expression2 = "([)]"
    print(is_balanced(expression1)) 
    print(is_balanced(expression2))  

    input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
    result = remove_duplicates(input_sequence)
    print(result)  # Output: [2, 3, 4, 5, 6, 7]

    sentence = "This is a test sentence. This sentence is a test."
    result = word_frequency(sentence)
    print(result)
