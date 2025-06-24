def longest_palindromic_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if word == word[::-1] and len(word) > len(longest):
            longest = word
    return longest if longest else "NO PALINDROME"

# Read input and print output
sentence = input().strip()
print(longest_palindromic_word(sentence))
