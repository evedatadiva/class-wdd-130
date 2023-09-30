#datedata
from datetime import datetime
date = datetime.now()
print ("The current dat of today is:" + str (date))  #aqui arroja la fecha como tal

#today y yesterday:

from datetime import datetime, timedelta
today = datetime.now ()
print ("today is" + str (today))

#timedelta is used to define a period of time: 

one_day = timedelta (days=1)
yesterday = today - one_day 

print ("yesterday was" + str (yesterday))
########################################################################
from datetime import datetime
current_date= datetime.now()

print("day:" + str (current_date.day))
print ("month:" + str (current_date.month))
print ("year: " + str (current_date.year))

#######################################################################

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Use an f-string to print only the date
# part of the current date and time.
print(f"{current_date_and_time:%Y-%m-%d}")
#answer:2023-09-26







