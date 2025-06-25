from datetime import date
import re
import sys
import inflect
p = inflect.engine()

def main():
    d = input("Date of Birth: ")
    r = return_date(d)
    delta = date.today() - r
    minutes = delta.days * 24 * 60
    print(f"{p.number_to_words(minutes, andword="").capitalize()} minutes")

def return_date(dob):
    if matches := re.search(r'^(\d\d\d\d)-(\d\d)-(\d\d)$', dob):
        day = int(matches.group(3))
        month = int(matches.group(2))
        year = int(matches.group(1))
        return date(year, month, day)
    sys.exit("Invalid date")

if __name__ == "__main__":
    main()
