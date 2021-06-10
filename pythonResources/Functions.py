### Simple function
def shout():
    shout_word = "congratulations" + "!!!"
    print(shout_word)
shout()


### Function with multiple parameters
# 
def shout(word1, word2):
    shout1 = word1 + "!!!"
    shout2 = word2 + "!!!"
    new_shout = shout1 + shout2
    return new_shout
yell = shout("congratulations", "you")
print(yell)


### Nested Function
def echo(n):
    def inner_echo(word1):
        echo_word = word1 * n
        return echo_word
    return inner_echo
twice = echo(2)
thrice = echo(3)
print(twice('hello'), thrice('hello'))


### Function with multiple default arguments
def shout_echo(word1, echo = 1, intense = False):
    echo_word = word1 * echo
    if intense is True:
        echo_word_new = echo_word.upper() + '!!!'
    else:
        echo_word_new = echo_word + '!!!'
    return echo_word_new
with_big_echo = shout_echo("Hey", echo=5, intense=True)
big_no_echo = shout_echo("Hey", intense=True)
print(with_big_echo)
print(big_no_echo)


### *args Function
def gibberish(*args):
    hodgepodge = ""
    for word in args:
        hodgepodge += word
    return hodgepodge
one_word = gibberish("luke")
many_words = gibberish("luke", "leia", "han", "obi", "darth")
print(one_word)
print(many_words)


### **kwargs Function
def report_status(**kwargs):
    """Print out the status of a movie character."""
    print("\nBEGIN: REPORT\n")
    for key, value in kwargs.items():
        print(key + ": " + value)
    print("\nEND REPORT")
report_status(name="luke",affiliation="jedi",status="missing")
report_status(name="anakin", affiliation="sith lord", status="deceased")
