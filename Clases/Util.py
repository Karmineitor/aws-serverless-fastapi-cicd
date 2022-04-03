
def HolaMundo(nombre):
  print("Hola Mundo, soy " +  nombre)
def printLista(a):
  print(' '.join(a))
def printclass(classy):
  attrs = dump(classy)
  # {'kids': 0, 'name': 'Dog', 'color': 'Spotted', 'age': 10, 'legs': 2, 'smell': 'Alot'}
  # now dump this in some way or another
  print(', '.join("%s: %s" % item for item in attrs.items()))
def dump(obj):
    if hasattr(obj, '__dict__'): 
        return vars(obj) 
    else:
        return {attr: getattr(obj, attr, None) for attr in obj.__slots__} 
  
HolaMundo("Roelver")
aaa =["Geeks", "for", "Geeks"]
printLista(aaa)