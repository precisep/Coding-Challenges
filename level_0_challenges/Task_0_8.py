def time_conversion(hours):

	if hours >= 60:
		return print(str(round(hours / 60)),"hour",",",str(hours % 60),"minutes")
	else: 
		return print(str(0),"hour",",",str(hours % 60),"minutes")
