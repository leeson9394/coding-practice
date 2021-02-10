# born death
# 1990 2010
# 1845 1903
# 1930 1964
# 1977 1999

# Question: what year has most population? 

def most_population(born_years, death_years):
        start_year = min(born_years)
        end_year = max(death_years)
        people_count = 0
        year_and_people = {}

        # save to dict
        for year in range(start_year, end_year):
            if year in born_years:
                people_count += 1
            if year in death_years:
                people_count -= 1
            
            year_and_people[year] = people_count

        # search in dict
        max_v=max(year_and_people.values())
        res = [k for k,v in year_and_people.items() if v == max_v]
        return res

born_years = [1845, 1750, 1846]
death_years = [1903, 1869, 1850]
res = most_population(born_years, death_years)
print(res)

# import operator
# year_and_people = {'1750': 1, '1751': 1, '1845': 2, '1846': 3, '1847':3, '1848':3, '1849':3, '1850': 2, '1851': 2, '1869':1, '1903': 0}
# year = max(year_and_people.items(), key=operator.itemgetter(1))
# print(year)