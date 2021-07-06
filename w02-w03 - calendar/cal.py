"""
Lab 03 - Calendar
Design for a Calendar program similar to that of the 'cal' command in unix.
"""

import sys, datetime

"""
MAIN (called at bottom of file)
"""
def main():

    # GET Date ASSIGN return value of get_date()
    if len(sys.argv) > 1 and sys.argv[1] == "noprompt":
        Date.prompt_date_in_constructor = False
    
    date = Date() # handle all of these in date_obj constructor/member variables

    # DISPLAY display(Date)
    print(date)
    
    # run test cases
    print("Test Cases:")
    print(Date(1753, 1), '\n')
    print(Date(1753, 2), '\n')
    print(Date(1754, 1), '\n')
    print(Date(1756, 2), '\n')
    print(Date(1800, 2), '\n')
    print(Date(2000, 2), '\n')
    # # Month: "error", 0, 13, 11
    print(Date(1753, 0), '\n')
    print(Date(1753, 13), '\n')
    print(Date(1753, 11), '\n')
    # # Year: "error", -1, 1752, 2019
    print(Date(-1, 1), '\n')
    print(Date(1752, 1), '\n')
    print(Date(2019, 1), '\n')

"""
DEFINE
"""
DEBUG = False
def debug(text: str):
    if DEBUG: print("debug:", text)

"""
DATE CLASS
"""
class Date:
    """
    Initializer
    """
    def __init__(self,
        year_init:  int = datetime.date.today().year,
        month_init: int = datetime.date.today().month,
        day_init:   int = datetime.date.today().day):

        self.year   = year_init
        self.month  = month_init
        self.day    = day_init

        if self.prompt_date_in_constructor: self.prompt()

    """
    Prompt (Get Date)
    """
    def prompt(self): self.year, self.month = prompt_date()
    
    """
    Display
    """
    def __repr__(self):
        # throws error message if invalid instead of displaying date
        if validate_date(self.year, self.month, msg=True):

            # display calendar if valid
            return get_calendar(self.year, self.month, self.day)
        
        else: return get_calendar_header(self.year, self.month)
    
    """
    Class variables
    """
    NUMBER_DATE     = 0
    TEXT_DATE       = 1
    ND_MONTH_FIRST  = 2
    TD_MONTH_FIRST  = 3
    which_date      = NUMBER_DATE
    display_date_before_calendar = True

    prompt_date_in_constructor = True

    days_of_week = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }

    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }


"""
Custom Errors
""" 
class RangeError(Exception):
    def __init__(self, msg="Invalid Range."):
        super().__init__(msg)

"""
FUNCTIONS
"""
# display calendar
def display_calendar(year: int, month: int): print(get_calendar(year, month))

def get_calendar_header(year: int, month: int):
    header = ""
    if not validate_date(year, month):
        header = f"month/year: {month} {year}\n"
    else:
        header = f"{Date.months[month].upper()} {year}"
        header = f"{header:^20s}\n"
        for dow in Date.days_of_week.values():
            header += dow[:2].upper() + ' '
        header += "\n--------------------\n"
    return header

# get calendar (alternative: print(Date_obj) also works :)
def get_calendar(year: int, month: int, day: int = 1):

    # initialize information
    days_in_month = get_days_in_month(year, month)
    day_position = 0 # (0 == sunday, 6 == saturday...)

    # calculate offset/set offset str
    offset_str = ""
    for i in range(calculate_offset(year, month)):
        offset_str += '   ' # fill offset days ow with blank space
        day_position += 1 # update dow
        assert day_position < 7 # dow cannot be greater than 7 (6)

    # get days in month/set month str
    days = ""
    for i in range(days_in_month):
        make_today_bold = i + 1 == day and year == datetime.date.today().year
        if make_today_bold: days += "\033[1m"   # make today's date bold
        if make_today_bold: days += "\033[31m"   # make today's date red
        days += f"{str(i + 1):3}"               # send day + spaces to output
        if make_today_bold: days += "\033[0m"   # clear bold text
        
        # (update dow)
        day_position += 1
        if day_position >= 7: days += '\n'
        day_position %= 7

    # return concatenated str
    return get_calendar_header(year, month) + offset_str + days
    
# get date (more ideal to use Date_obj.get())
def prompt_date():
    # GET year and month
    for i in range(10): # limit re-prompts to 10 times
        year, month = (1754, 1)

        try:
            """
            prompt
            """
            # prompt month
            month   = int(input("Month: "))

            # validate
            if not validate_date(year, month): raise RangeError

            # prompt year
            year    = int(input("Year: "))
            if year in range(0, 99): year += 2000 # if only two digits XX, year is 20XX

            # validate
            if not validate_date(year, month): raise RangeError

        # handle errors:
        except ValueError as error_msg:
            print(error_msg)
            if i < 10: print("Please enter the values again.")

        except RangeError as error_msg:
            print(error_msg, end=" ")
            if i < 10: print("Please enter the values again.")

        else: # on success: (else statement condition)
            return (year, month) # set values
    
    return (1753, 1)

# Get days in month
def get_days_in_month(year: int=1753, month: int=1):
    # debug("Getting days in month...", year)
    day = 30

    if   month in [1, 3, 5, 7, 8, 10, 12]:
        # debug("Month is any of [1, 3, 5, 7, 8, 10, 12]... days_in_month set to 31")
        day = 31

    elif month in [4, 6, 9, 11]:
        # debug("Month is any of [4, 6, 9, 11]... days_in_month set to 30")
        day = 30

    elif month == 2:
        # debug("Month is February...")
        if is_leap_year(year):  day = 29
        else:                   day = 28

    return day

# calculate offset
def calculate_offset(year: int, month: int):
    debug("Getting offset...")
    # offset = ((
    #   days passed in previous years +
    #   days passed in current year
    # ) % 7)

    offset = 0

    # offset from days passed in previous years
    for year_i in range(1754, year):
        offset += 365
        if is_leap_year(year_i): offset += 1

    # offset from days passed this year
    for month_i in range(month):
        offset += get_days_in_month(year, month_i)
    
    offset %= 7

    # return
    assert offset in range(0, 7)
    return offset

# is leap year
def is_leap_year(year: int):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: 
        return True
    return False # else

# validate date
def validate_date(year: int, month: int, msg=False):
    assert type(year) is int and type(month) is int
    if year < 1753:
        if msg: print("\033[31mYear in invalid range. Please ensure year is greater than 1752. \033[0m")
        return False
    if not month in range(1, 13):
        if msg: print("\033[31mMonth in invalid range. Must be an integer value between 1 and 12. \033[0m")
        return False
    return True

"""
RUN PROGRAM
"""
if __name__ == "__main__": main()
