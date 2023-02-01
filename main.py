def flat_list(l):
    # input nested list is stored in l
    # Insert Code below
    sdl=[]
    for i in range(len(l)):
        for j in range(len(l[i])):
            sdl.append(l[i][j])
    
    # Insert Code Above
    # Return single-dimension list.
    return sdl
