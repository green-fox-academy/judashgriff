# Create a PostIt class that has
# a background_color
# a text on it
# a text_color
# Create a few example post-it objects:
# an orange with blue text: "Idea 1"
# a pink with black text: "Awesome"
# a yellow with green text: "Superb!"

class PostIt(object):
    def __init__(self, bg, text, text_color):
        self.background = bg
        self.text = text
        self.text_color = text_color


    

first = PostIt('orange', "Idea 1", 'blue')
second = PostIt('pink', "Awesome", 'black')
third = PostIt('yellow', "Superb", 'green')

print(first.background, first.text_color, first.text, second.background, second.text_color, second.text, third.background, third.text_color, third.text)