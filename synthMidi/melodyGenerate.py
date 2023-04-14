import random
notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
#list of scales
#major scale
major = [0,2,4,5,7,9,11]
#minor scale
minor = [0,2,3,5,7,8,10]

#    whole, whole, half, whole, whole, whole, half
#    2,     2,     1,    2,     2,     2,     1

def rotate(l, n):
    return l[n:] + l[:n]

def GenerateScale(scale, root):
    #get the index of the root note
    rootIndex = notes.index(root)
    #rotate the scale to the root note
    rotatedScale = rotate(notes, rootIndex)
    notesInScale = []
    for interval in scale:
        notesInScale.append(rotatedScale[interval])
    return notesInScale



def GenerateMelodyWithRests(scale, root, length):
    scale = GenerateScale(scale, root)
    melody = []
    for i in range(length):
        note = random.choice(scale)
        melody.append(note)
        #add a rest 25% of the time
        if random.randint(0,3) == 0:
            melody.append("rest")
    return melody

