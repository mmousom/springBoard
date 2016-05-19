cities = {'CA':'Sacramento' , 'TX:Austin','OH:Columbus'}
cities['NY'] = 'New York'
cities['NC'] = 'Charlotte'

print 'Lets print cities in many ways'
print 'The major city of \'CA\' is : ' , cities['CA']

find_city(themap,state):
    if state in themap :
        return themap[state]
    else :
        return "Not found"

cities['_find']=find_city

print "lets print city this way"
while True:
    state = raw_input("Enter the state name ? Press enter to quit.. \n>")
    if not state:
        break
    cities_found = cities_find['_find'](themap,state)
    
