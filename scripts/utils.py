import re

def get_authors(authorLabelText):
    """ Takes the text label for authors as input, and transforms it to a text of authors
    """
    # remove 'By: '
    return authorLabelText[4:]

def get_length(lengthLabelText):
    """ Takes the text label for length as input, and transforms it to the length in minutes
    """
    # use regex to find the number of hours and minutes
    hrs_regex = '(\d+) h'
    mins_regex = '(\d+) m'

    # get # hours
    hrs = re.search(hrs_regex, lengthLabelText)
    if hrs:
        hrs = int(hrs.group(1))
    else:
        hrs = 0

    # get # mins
    mins = re.search(mins_regex, lengthLabelText)
    if mins:
        mins = int(mins.group(1))
    else:
        mins = 0

    # convert to minutes
    return hrs * 60 + mins

def get_date(dateLabelText):
    """ Takes the text label for release date as input, and transforms it to a date
    """
    # use regex to find the date
    date_regex = '(\d+)-(\d+)-(\d+)'
    mm = re.search(date_regex, dateLabelText).group(1)
    dd = re.search(date_regex, dateLabelText).group(2)
    yy = re.search(date_regex, dateLabelText).group(3)
    # convert to full year (20 if yy < 30 else 19)
    yy = int(yy)
    yy = yy + 2000 if yy < 30 else yy + 1900
    # convert to pandas default datetime format
    return f'{yy}-{mm}-{dd}'

def get_price(priceLabelText):
    """ Takes the text label for price as input, and transforms it to a price
    """
    # use regex to find the price
    price_regex = '\$(\d+\.\d+)'
    return float(re.search(price_regex, priceLabelText).group(1))

# test
print(get_authors('By: BTS, Myeongseok Kang, Anton Hur - translator, Slin Jung - translator, Clare Richards - translator'))
print(get_authors('By: BTS, Myeongseok Kang'))
print(get_authors('By: BTS'))

# print(get_length('Length: 11 hrs and 18 mins'))
# print(get_length('Length: 4 hrs'))
# print(get_length('Length: 3 mins'))
# print(get_length('Length: less than 1 minute'))
# print(get_length('Length: more than 20 hours'))

# print(get_date('Release date: 07-09-23'))
# print(get_date('Release date: 01-20-78'))

# print(get_price('Regular price: $25.51'))
