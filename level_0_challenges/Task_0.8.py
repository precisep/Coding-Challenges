def time_conversion(hours):
	''' Function converts hours to hours and minutes '''

	if hours >= 60:
		return str(round(hours / 60)),"hours",str(hours % 60),"minutes"
	else: 
		return str(0),"hours",str(hours % 60),"minutes"