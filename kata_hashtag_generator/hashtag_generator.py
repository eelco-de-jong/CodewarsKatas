"""The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.
"""


def generate_hashtag(s):
    if 0 < len(s) <= 140:
        s = s.title().replace(' ', '')
        return '#{}'.format(s)
    else:
        return False


def test_empty():
    assert generate_hashtag('') == False


def test_single_word():
    assert generate_hashtag('Codewars') == '#Codewars'


def test_trailing_spaces():
    assert generate_hashtag('Codewars     ') == '#Codewars'


def test_should_remove_spaces():
    assert generate_hashtag('Codewars Is Nice') == '#CodewarsIsNice'


def test_should_capitalice():
    assert generate_hashtag('codewars is nice') == '#CodewarsIsNice'


def test_capitalize_only_first_letters():
    assert generate_hashtag('CodeWars is nice') == '#CodewarsIsNice'


def test_capitalize_single_letter_words():
    assert generate_hashtag('c i n') == '#CIN'


def test_remove_unnecessary_middle_spaces():
    assert generate_hashtag('codewars  is  nice') == '#CodewarsIsNice'


def test_assert_to_long():
    assert generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong') == False