# list of countries
countries = ["Australia", "USA", "France"]
# add a country at the end
countries.append("Spain")
# remove by index
del(countries[2])
# add a country in the middle
countries.insert(2, "Japan")

# set of countries
countries2 = {"Portugal", "Singapore", "Greece"}
# add a country at the end
countries2.update(["Russia"])
# cannot remove by index since sets can't use indexing
# cannot add to the middle of the set since order isn't guaranteed