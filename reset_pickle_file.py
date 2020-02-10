#!/usr/bin/python3
# Matthew Buckmaster
# 1/27/2020

"""Create a default pickle file/reset pickle file"""

import pickle
#Title, Genre, Developer, Publisher, System, Realse Date, Rating, Single/Multi/Both, Price, Purchase Date, Notes
games = {1 :['Halo 3','FPS','Bungee','Microsoft','Xbox 360','2007','4','both','$30.00','Yes','1/15/2008','This game blows chunks'], 
         2 :['The Legend of Zelda: Ocarina of Time','Action-Adventure','Nintendo','Nintendo','Nintendo 64','1998','10','single','$50.00','Yes','11/21/2011','This game is a masterpiece'],
         3 :['The Legend of Zelda','FPS','Nintendo','Microsoft','Xbox 360','2007','10','both','$30.00','Yes','1/15/2008','This game blows chunks']}

data_file = open("game_lib.pickle", "wb")
pickle.dump(games, data_file)
data_file.close()
6