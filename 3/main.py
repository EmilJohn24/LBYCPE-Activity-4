import string
def word_count_with_letter_counter(letter, paragraph):
    """
    Returns the letter count and word count
    """
    words = paragraph.split()
    counter = 0
    for word in words:
        if letter in word:
            counter += 1

    return counter, len(words)

def remove_punctuation(paragraph):
    paragraph_without_punct = " "
    for letter in paragraph:
        if letter not in string.punctuation:
            paragraph_without_punct += letter
    return paragraph_without_punct



paragraph = """

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!


"""

paragraph = remove_punctuation(paragraph)
print(paragraph)
e_count, word_count = word_with_letter_counter('e', paragraph)
print('Your text contains {0} words, of which {1}({2:.1f}%) contain an "e"'.format(
    word_count, e_count, 100 * e_count/word_count
))

