'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count=0):
    # Look at the first and second letters in the word
    # IF they equal "th" together increase count, and remove those two elements
    # If not, then remove just that first element, and call the function again with the new shortened word
    # At the end, return the count
    if word == '':
        return count

    if len(word) >= 2 and (word[0] + word[1]) == 'th':
        return 0 + count_th(word[2:], count + 1)
    else:
        return count_th(word[1:], count)   

