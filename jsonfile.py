import json
#data={}
#data["employees"]=[]
#data["employees"].append({"name":"sunil",
                         #"emid":101,
                         #"dob":"12/12/1996"})
#data["employees"].append({"name":"ram",
                          #"emid":103,
                          #"dob":26/1/1995})
#data["employees"].append({"name":"ravi",
                           #"emid":102,
                           #"dob":"31/6/1993"})
#file=open("json_write.json","w")
#json.dump(data,file)
#file.close()
collect=open("json_write.json","r")
read=json.load(collect)
#print(read)
#print(read["employees"])
for q in read["employees"]:
    #print(q)
    print(q["name"])
collect.close()