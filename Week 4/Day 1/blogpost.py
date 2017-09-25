# Create a BlogPost class that has
# an author_name
# a title
# a text
# a publication_date
# Create a few blog post objects:
# "Lorem Ipsum" titled by John Doe posted at "2000.05.04."
# Lorem ipsum dolor sit amet.
# "Wait but why" titled by Tim Urban posted at "2010.10.10."
# A popular long-form, stick-figure-illustrated blog about almost everything.
# "One Engineer Is Trying to Get IBM to Reckon With Trump" titled by William Turton at "2017.03.28."
# Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention.
#  When I asked to take his picture outside one of IBM’s New York City offices, he told me that he
#   wasn’t really into the whole organizer profile thing.


class BlogPost(object):
    def __init__(self, name, title, text, date):
        self.author_name = name
        self.title = title
        self.text = text
        self.publication_date = date


lorem = BlogPost("John Doe", "Lorem Ipsum", "Lorem ipsum dolor sit amet.", "2000.05.04.")
wait_but_why = BlogPost("Tim Urban", "Wait but why", "A popular long-form, stick-figure-illustrated blog about almost everything.", "2010.10.10.")
engineer = BlogPost("William Turton", "One Engineer Is Trying to Get IBM to Reckon With Trump", "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing.", "2017.03.28.")

print(lorem.author_name, lorem.title, lorem.text, lorem.publication_date, wait_but_why.author_name, wait_but_why.title, wait_but_why.text, wait_but_why.publication_date, engineer.author_name, engineer.title, engineer.text, engineer.publication_date, )