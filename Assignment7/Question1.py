# Q1.Write a version of a palindrome recognizer that also accepts phrase
# palindromes such as "Go hanga salami I'm a lasagna hog.", "Was it a rat I
# saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no
# basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a
# tired nude Maori","Rise to vote sir", or the exclamation "Dammit, I'm mad!".
# Note that
# punctuation, capitalization, and spacing are usually ignored.


x = input("Enter any name : ")
w = ""
for i in x:
    w = i + w

if (x == w):
    print("Yes It is a palindrome")
else:
    print("No It is not palindrome")

