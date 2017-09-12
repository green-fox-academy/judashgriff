# - Create a variable named `nimals`
#   with the following content: `["kuty", "macs", "cic"]`
# - Add all elements an `"a"` at the end

nimals = ["kuty", "macs", "cic"]

#new_list = ['%sa' % x for x in nimals]

#print (new_list)

animals = []

for i in nimals:
    animals.append (i + "a") 

print (animals)
