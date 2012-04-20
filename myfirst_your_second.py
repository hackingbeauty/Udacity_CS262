def myfirst_yoursecond(p,q):
    first_space_index = p.find(" ")
    first_word = p[0:first_space_index]
    
    second_space_index = q.find(" ")
    second_word = q[second_space_index+1:]

    if first_word == second_word:
        return True
    else:
        return False


myfirst_yoursecond("bell hooks","curer bell")


def myfirst_yoursecond_class_example(p,q):
    pindex = p.find(" ")
    qindex = q.find(" ")
    return p[0:pindex] == q[qindex+1:]

myfirst_yoursecond_class_example("bell hooks","curer bell")
