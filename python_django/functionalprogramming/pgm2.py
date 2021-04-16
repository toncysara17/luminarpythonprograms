isldata=[
{"team":"mumbai","mp":20,"won":12,"drawn":4,"los":4,"pts":40},
{"team":"atk","mp":20,"won":12,"drawn":4,"los":4,"pts":40},
{"team":"ne","mp":28,"won":9,"drawn":9,"los":3,"pts":33},
{"team":"fcg","mp":20,"won":10,"drawn":10,"los":3,"pts":31},
{"team":"hybd","mp":20,"won":6,"drawn":11,"los":3,"pts":29},


]

#no of teams
teamno=len(isldata)
print(teamno)
#team name
#map
team_name=list(map(lambda data:data["team"],isldata))
print(team_name)
#highest point
points=max(list(map(lambda data:data["pts"],isldata)))
print(points)
#highest point team
hghpt=list(filter(lambda team:team["pts"]==points,isldata))
#print(hghpt)

#highest team name
hptname=list(map(lambda team:team["team"],hghpt ))
print(hptname)





