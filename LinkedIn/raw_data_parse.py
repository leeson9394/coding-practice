import sys, os

#file = "/var/log/message"
file = "message.txt"
    
def raw_data_parse(file):
    with open(file) as f:
        data = f.readlines()
        counter ={}
        for line in data:
            time=line.split(":")[0]+ ':'+ line.split(":")[1]
            if time in counter:
                counter[time] += 1
            else:
                counter[time] = 1
        
    print(counter)

#raw_data_parse(file)

#test
mydict = {
  "name": "Device", 
  "children": [ 
    {
      "name": "Networking", 
      "children": [
         { "name": "Router", "children": [] },
         { "name": "Switch" },
         { "name": "Firewall", "children": [] }
      ]
    },
    { 
      "name": "Computer",
      "children": []
    },
  ]
}

print(mydict["children"][0])


