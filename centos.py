from music21 import *

al-istihlal = [stream.Stream() for i in range(15)]

#Centones Finales
al-istihlal[0].append(note.Note('A3'))
al-istihlal[0].append(note.Note('B3'))
al-istihlal[0].append(note.Note('C4'))

al-istihlal[1].append(note.Note('D4'))
al-istihlal[1].append(note.Note('C4'))

al-istihlal[2].append(note.Note('F4'))
al-istihlal[2].append(note.Note('E4'))
al-istihlal[2].append(note.Note('D4'))
al-istihlal[2].append(note.Note('C4'))

#Centones
al-istihlal[3].append(note.Note('E4'))
al-istihlal[3].append(note.Note('F4'))
al-istihlal[3].append(note.Note('G4'))

al-istihlal[4].append(note.Note('G4'))
al-istihlal[4].append(note.Note('F4'))
al-istihlal[4].append(note.Note('E4'))

al-istihlal[5].append(note.Note('C4'))
al-istihlal[5].append(note.Note('B3'))
al-istihlal[5].append(note.Note('A3'))
al-istihlal[5].append(note.Note('C4'))
