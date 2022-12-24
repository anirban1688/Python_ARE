thisdict = {
  "pongal": [250,30],
  "upma": [350,35],
  "idly": [500,16],
  "dosa": [400,20]
}

try:
    while True:
      str = input('What item do you prefer?')
      ####### searching through a dictionary
      ####### option 1: get
      x=thisdict.get(str)
      print(x)
      ####### option 2: string search
      if str in thisdict:
        l=thisdict[str]
        print('price per plate is: ',l[1])
        num=int(input('item quantity?'))
        ##### updating a dictionary
        up_dict = {str: [l[0]-num,l[1]]}
        thisdict.update(up_dict)
        print(thisdict)
      else:
        print('item not presently available, will be updated when available')
        thisdict[str]=[100, 40]
        #print(thisdict)
except KeyboardInterrupt:
    pass

