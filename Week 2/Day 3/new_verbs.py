# Create a function called 'create_new_verbs()' which takes a list of verbs and a string as parameters
# The string shouldf be a preverb
# The function appends every verb to the preverb and returns the list of the new verbs


verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
preverb = "be"

def create_new_verbs(verbs):
    for i in range(len(verbs)):
        verbs[i] = preverb + verbs[i]
    return verbs

new_verbs = create_new_verbs(verbs)
print (new_verbs)