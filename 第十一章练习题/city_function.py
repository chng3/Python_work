# 11-1 城市和国家
"""城市和国家的函数收集"""

def city_country(city, country, population=0):
	"""返回城市名和国家名的字符串"""
	if population:
		return(city.title() + ', ' + country.title() + ' - population ' 
		+ str(population))
	else:
		return(city.title() + ', ' + country.title())
