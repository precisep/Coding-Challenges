def time_conversion(hours):
	''' Function converts hours to hours and minutes '''

	if hours >= 60:
		return print(str(round(hours / 60)),"hours",str(hours % 60),"minutes")
	else: 
		return print(str(0),"hours",str(hours % 60),"minutes")
