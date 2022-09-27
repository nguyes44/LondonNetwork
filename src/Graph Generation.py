
'''

THIS FILE IS A PLACE FOR OLD CODE RELATED TO GRAPH GENERATION

'''


##


adj_list = {}
mylist = []
def add_station(station): #equivalent to adding nodes into existence
  if station not in mylist:
    mylist.append(station)
  else:
    print("Station ",station.get_name()," already exists!")
 
def add_line(connection): #equivalent to adding edges into existence
  temp = []
  connectionInfo = connection.get_information()
  station1 = connection.get_station1()
  station2 = connection.get_station2()


  if any(node is station1 for node in mylist) and any(node is station2 for node in mylist):
      
      if not any(node is station1 for node in adj_list):
        temp.append([station2,connectionInfo])
        adj_list[station1] = temp
      
      elif any(node is station1 for node in adj_list):
        temp.extend(adj_list[station1])
        temp.append([station2,connectionInfo])
        adj_list[station1] = temp
  
  else:
    print("Stations don't exist!")

  # if station1 in mylist and station2 in mylist: #checking if two stations are valid
  #   if station1 not in adj_list:                #key doesnt exist yet
  #     temp.append([station2,connectionInfo])
  #     adj_list[station1] = temp

  
   
    # elif station1 in adj_list:
    #   temp.extend(adj_list[station1])
    #   temp.append([station2,connectionInfo])
    #   adj_list[station1] = temp
       
  
 
def graph():
    for node in adj_list:
      tempNodePrint = node.get_id()
      tempList = []
      for i in adj_list[node]:
        tempList.append([i[0].get_id(), i[1].get_name()])
      
      print(tempNodePrint, " ---> ", tempList)

        # print(node.get_name(), " ---> ", [i for i in adj_list[node]])


# for station in stations.values():
#     add_station(station)

# for connection in connections:
#     add_line(connection)

# station11 = add_station(Station(11,51.5226,-0.1571,"Baker Street","Baker<br />Street",1,5,0))
# station163 = add_station(Station(163,51.5225,-0.1631,"Marylebone",NULL,1,1,1))
# station212 = add_station(Station(212,51.5234,-0.1466,"Regent's Park","Regent's<br />Park",1,1,0))
# line1 = Line(1,"Bakerloo Line","AE6017",NULL)

# add_line(station11, station163, line1, 1)
# add_line(station11, station212, line1, 2)

graph()
# pprint.pprint(adj_list)