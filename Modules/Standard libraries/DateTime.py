import datetime
import locale

dt = datetime.datetime.now() #Gets the current date and time
print(dt)
print(dt.year)          #gets the year
print(dt.month)         #gets the month
print(dt.day)           #gets the day
print(dt.hour)          #gets the hour 
print(dt.minute)        #gets the minute
print(dt.second)        #gets the second
print(dt.microsecond)   #gets the microseconds

print(f"{dt.hour}:{dt.minute}:{dt.second}") #printing with format
print(f"{dt.day}/{dt.month}/{dt.year}")     #printing with format

dt = datetime.datetime(2001, 7, 18) #putting a given date
print(dt)
print(dt.replace(year= 3000))       #replaces a value just for a moment
print(dt)                           #back to year 2001
dt = dt.replace(year= 3000)         #saving the replacement
print(dt)

dt = datetime.datetime.now()
print(dt.isoformat()) #One way to format date like this -> 2022-07-25T20:33:09.172026

print(dt.strftime("%A %d %B %Y %I:%M")) #Formating using codes

locale.setlocale(locale.LC_ALL, "es-mx") #Changing the language to Spanish
print(dt.strftime("%A %d de %B del %Y - %I:%M %p")) #Formating using codes

dt = datetime.datetime.now()
t = datetime.timedelta(days= 14, hours= 6, seconds= 5800) #Setting a time value

next_two_weeks = dt + t #sums time
print(next_two_weeks)

two_weeks_ago = dt - t #decrease time
print(two_weeks_ago)

"""
Codes for formatting time

%a -> Weekday as locale`s abbreviated name
%A -> Weekday as locale`s full name 
%w -> Weekday as a decimal number, where 0 is Sunday and 6 is Saturday
%d -> Day of the month as a zero-padded decimal number
%b -> Month as locale`s abbreviated name
%B -> Month as locale`s full name
%m -> Month as a zero-padded decimal number
%y -> Year without century as a zero-padded decimal number
%Y -> Year with century as a decimal number
%H -> Hour (24-hour clock) as a zero-padded decimal number
%I -> Hour (12-hour clock) as a zero-padded decimal number
%p -> Locale`s equivalent of either AM or PM
%M -> Minute as a zero-padded decimal number
%S -> Second as a zero-padded decimal number
%Z -> Time zone name (empty string if the object is naive).

Codes for localization:
https://www.science.co.il/language/Locale-codes.php
There are a lot of codes, so I put a URL that has them all lmao
"""