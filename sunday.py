

# check leap yr
def leap(year):
	if year % 4 == 0 and year % 100 != 0:
	    return True
 	elif year % 400 == 0:
	    return True
	elif year % 100 ==0:
	    return False
	else:
	    return False

# return the days count in month
def daysInMonth(month,year):
	if month==4 or month==9 or month==6 or month==11:
		return 30
		# for feb, 
	elif month==2:
		if (leap(year)):
			return 29
		else:
			return 28
	else:
		return 30

# function to return the no of sundays
def total_sunday_count(daysInMonth):
	total_days=0
	sundayCount = 0
	first_days = []
	for year in range(1901, 2001):
		for month in range(1,13):
			if year != 1900:
				first_days.append(total_days)
			total_days+=daysInMonth(month,year)


	sundays= list(filter(lambda x:x%7==0, first_days))
	return len(sundays)


total_sunday_count(daysInMonth)


