# Question6.A pangram is a sentence that contains all the letters of the English alphabet at
# least once,
# for example: The quick brown fox jumps over the lazy dog. Your task here is to
# write a
# function to check a sentence to see if it is a pangram or not.


def check_pangram():
    string1 =  "The quick brown fox jumps over the lazy dog1"
    alphabets = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    for i in string1:
        if i not in alphabets:
            print(f"{i} It IS NOT PANGRAM")
        else:
            print(f"{i} it is PANGRAM")


check_pangram()