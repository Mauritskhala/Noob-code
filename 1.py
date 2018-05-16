#something used to record and refer to names

def init(data):
  data['first']={}
  data['middle']={}
  data['last']={}
  
def lookup(data,label,name):
  return data[label].get(name)

def store(data,*fullnames):
  for fullname in fullnames:
    names = fullname.split()
    if len(names) == 2: names.insert(1,'')
    labels = 'first','middle','last'
    for label,name in zip(labels,names):
      people = lookup(data,label,name)
      if people:
        people.append(fullname)
      else:
        data[label][name]=[fullname]
