
TEXT = """
The Motorcycle World Championships was introduced in 1949. In 1950, the FIA responded with the first ever official World Championship for Drivers. The championship series, to be held across six of the 'major'
Grands Prix of Europe plus the Indianapolis 500, was in effect a formalization of what had already been developing in Grand Prix racing during
the previous years. Italian teams of Alfa Romeo, Ferrari, and Maserati were best positioned to dominate the early years. Other national
manufacturers – such as the French manufacturer Talbot or the British BRM – competed, although less successfully. A number of private cars
also took part in local races. The Italian and German factory teams in those days often employed 2 to 3 drivers whose nationality was the
same as the team's and at least 1 foreign driver; for example the Alfa Romeo team in 1950 consisted of Italian drivers Giuseppe Farina, Luigi
Fagioli and Piero Taruffi; and Argentine driver Juan Manuel Fangio.
"""


def parse_text(text_to_parse):
    """
    Function to load a file and the words indvidually while cleaning them up.

    This is shared with all students along with any data files to use
    """
    return_words = []

    # Now parse out each word
    words = text_to_parse.split(' ')
    for word in words:
        word = word.replace(',', '')
        word = word.replace('\n', '')
        word = word.replace('.', '')
        word = word.replace('(', '')
        word = word.replace(')', '')
        word = word.replace('"', '')
        word = word.replace("'", '')
        word = word.replace("[", '')
        word = word.replace("]", '')
        word = word.strip()
        if len(word):
            return_words.append(word.lower())

    return return_words


"""
Student fills in the code below.

stats - Dictionary to hold results
parsed_words - Individual words pulled from a text file
"""
stats = {}
parsed_words = parse_text(TEXT)

for word in parsed_words:
    # Student program here to count words.
    pass