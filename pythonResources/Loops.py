### FOR LOOP used for iterating over a sequence (examples)
  #Find the number of player named "Jordan"
player_name_all = []
for player in players_list:
    player_name = player.get("firstName")
    player_name_all.append(player_name)
name_jordan = player_name_all.count("Jordan")
print(name_jordan)

  #Find players with jersey number 23
for player in players_list:
    jersey_no = player.get("leagues").get("standard").get("jersey")
    if jersey_no == "23":
        print(player.get("firstName"))
        print(player.get("lastName"))
        
        
   
###  WHILE LOOP repeats a block of code as long as a condition is True.
  #Counting to 10
current_number = 1
while current_number <= 10:
  print(current_number)
  current_number += 1
  
  #Removing all cats from a list of pets
pets = ['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
  pets.remove('cat')
print(pets)

  
