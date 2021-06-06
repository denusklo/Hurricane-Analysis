# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def damages_conversion(damages):
    conversion = {"M": 1000000,
                  "B": 1000000000}

    for i in range(len(damages)):
        for j in range(len(conversion)):
            if damages[i][-1] in list(conversion.items())[j]:
                damages[i] = str(float(damages[i].replace(damages[i][-1], "")) * (list(conversion.items())[j][1]))
    return damages
            
updated_damage = damages_conversion(damages)

# write your construct hurricane dictionary function here:
def create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricane_dict = {}
    for i in range(len(names)):
        hurricane_dict[names[i]] = {'Name':names[i], 'Month':months[i], 
                                    'Year':years[i], 
                                    'Max Sustained Wind':max_sustained_winds[i], 
                                    'Areas Affected':areas_affected[i], 'Damage':damages[i], 
                                    'Deaths':deaths[i]}
    return hurricane_dict
hurricane_dict = create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)

# write your construct hurricane by year dictionary function here:
def hurricane_by_year(year):
    hurricane_by_year_list = []
    for i in range(len(names)):
        if hurricane_dict[list(hurricane_dict.keys())[i]].get("Year") == year:
            hurricane_by_year_list.append(hurricane_dict[list(hurricane_dict.keys())[i]])
    return hurricane_by_year_list
        
hurricane_by_year(1932)

# all unique areas:
areas = []
for i in range(len(names)):
    areas += (hurricane_dict.get(list(hurricane_dict.keys())[i]).get("Areas Affected"))
areas = np.unique(areas)

# The counts of area appeared:
area_count = {}
for i in range(len(areas)):
    area_count[areas[i]] = 0
    for j in range(len(names)):
        if areas[i] in hurricane_dict.get(list(hurricane_dict.keys())[j]).get("Areas Affected"):
            area_count[areas[i]] += 1

# write your count affected areas function here:
def count_affected_areas(area):
    area_count = {area:0}
    for i in range(len(names)):
        if area in hurricane_dict.get(list(hurricane_dict.keys())[i]).get("Areas Affected"):
            area_count[area] += 1
    return area_count

count_affected_areas("Yucatn Peninsula")

# write your find most affected area function here:
max_area = "Central America"
max_area_count = 0

def find_most_affected_area(max_area, max_area_count):
    for area in areas:
        if area_count.get(area) > max_area_count:
            max_area_count = area_count.get(area)
            max_area = area
    return max_area, max_area_count

find_most_affected_area(max_area, max_area_count)

# write your greatest number of deaths function here:
death_max_hurricane = "Cuba I"
death_max_number = 0

def greatest_number_of_deaths(death_max_hurricane, death_max_number):
    for i in range(len(names)):
        if hurricane_dict.get(names[i]).get("Deaths") > death_max_number:
            death_max_hurricane = names[i]
            death_max_number = hurricane_dict.get(names[i]).get("Deaths")
    return death_max_hurricane, death_max_number

greatest_number_of_deaths(death_max_hurricane, death_max_number)

# write your catgeorize by mortality function here:
def catgeorize_by_mortality(hurricane_dict):
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}

    hurricane_mortality_rating = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for cane in hurricane_dict:
        num_death = hurricane_dict[cane]["Deaths"]
        if num_death == mortality_scale[0]:
            hurricane_mortality_rating[0].append(hurricane_dict[cane])
        elif num_death <= mortality_scale[1] and num_death > mortality_scale[0]:
            hurricane_mortality_rating[1].append(hurricane_dict[cane])
        elif num_death <= mortality_scale[2] and num_death > mortality_scale[1]:
            hurricane_mortality_rating[2].append(hurricane_dict[cane])
        elif num_death <= mortality_scale[3] and num_death > mortality_scale[2]:
            hurricane_mortality_rating[3].append(hurricane_dict[cane])
        elif num_death <= mortality_scale[4] and num_death > mortality_scale[3]:
            hurricane_mortality_rating[4].append(hurricane_dict[cane])
        elif num_death > mortality_scale[4]:
            hurricane_mortality_rating[5].append(hurricane_dict[cane])
    return hurricane_mortality_rating

hurricane_by_year = catgeorize_by_mortality(hurricane_dict)
hurricane_by_year[1]


# write your greatest damage function here:
def greatest_damage(hurricane_dict):
    max_damage_hurricane = ""
    max_cost = 0
    for i in range(len(hurricane_dict)):
        if len(hurricane_dict.get(names[i]).get("Damage")) != 20:
            if max_cost < float(hurricane_dict.get(names[i]).get("Damage")):
                max_cost = float(hurricane_dict.get(names[i]).get("Damage"))
                max_damage_hurricane = names[i]
                max_cost,max_damage_hurricane
    return max_cost,max_damage_hurricane
        
max_cost, max_damage_hurricane = greatest_damage(hurricane_dict)
print(max_cost, max_damage_hurricane)






# write your catgeorize by damage function here:
def catgeorize_by_damage(hurricane_dict):
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}

    hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for cane in hurricane_dict:
        damage = hurricane_dict[cane]['Damage']
        if len(damage) == 20:
            hurricanes_by_damage[0].append(hurricane_dict[cane])
        elif float(damage) > damage_scale[0] and float(damage) <= damage_scale[1]:
            hurricanes_by_damage[1].append(hurricane_dict[cane])
        elif float(damage) > damage_scale[1] and float(damage) <= damage_scale[2]:
            hurricanes_by_damage[2].append(hurricane_dict[cane])
        elif float(damage) > damage_scale[2] and float(damage) <= damage_scale[3]:
            hurricanes_by_damage[3].append(hurricane_dict[cane])
        elif float(damage) > damage_scale[3] and float(damage) <= damage_scale[4]:
            hurricanes_by_damage[4].append(hurricane_dict[cane])
        elif float(damage) > damage_scale[4]:
            hurricanes_by_damage[5].append(hurricane_dict[cane])
    return hurricanes_by_damage

print(catgeorize_by_damage(hurricane_dict)[0])
