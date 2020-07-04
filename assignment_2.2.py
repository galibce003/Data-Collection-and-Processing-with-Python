#Add fruit before each item
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
map_testing = map(lambda x: "Fruit: "+x, lst_check)



#Create a list of countries
#That starts with "B"
countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
b_countries = filter(lambda x : "B" in x, countries)




#Create a list of first names
people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
first_names = [y for (x,y) in people]




#Use list comprehension to create a list called lst2 that doubles each element in the list, lst.
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
lst2 = [x*2 for x in lst]
print(lst2)




#Below, we have provided a list of tuples that contain students’ names and their final grades in PYTHON 101. Using list comprehension, create a new list passed that contains the names of students who passed the class (had a final grade of 70 or greater).
students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]
passed = [x for (x,y) in students if y>=70]





#Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the variable opposites if they are both longer than 3 characters each.
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

l = zip(l1,l2)
opposites = list(filter(lambda s: len(s[0])>3 and len(s[1])>3, l))






#Below, we have provided a species list and a population list. Use zip to combine these lists into one list of tuples called pop_info. From this list, create a new list called endangered that contains the names of species whose populations are below 2500.

species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]

pop_info = list(zip(species, population))
endangered = [x1 for (x1, x2) in pop_info if x2<2500]
print(endangered)
