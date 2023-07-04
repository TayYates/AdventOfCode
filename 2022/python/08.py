import numpy as np

field = np.array([list(x.strip()) for x in open("../data/08.txt")], int)
#print(field)

visible = np.zeros_like(field)
beauty = np.ones_like(field)

# run each cardinal direction once, flipping the field between them
for flip in range(4):
    for x,y in np.ndindex(field.shape):   
        lower = [tree < field[x,y] for tree in field[x,y+1:]]

        visible[x,y] = visible[x,y] | all(lower)
        beauty[x,y] *= next((i+1 for i,tree in enumerate(lower) if ~tree), len(lower))

    # flip operation
    field, visible, beauty = map(np.rot90, [field, visible, beauty])

#print(visible)
#print(beauty)
# part 1 answer
print(visible.sum())
# part 2 answer
print(beauty.max())