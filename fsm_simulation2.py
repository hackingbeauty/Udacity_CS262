edges = {(1,'q') : 1}

accepting = [1]

def fsmsim(string,current,edges,accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        if(current,letter) in edges:
            destination = edges[(current,letter)]
            remaining_string = string[1:]
            return fsmsim(remaining_string,destination,edges,accepting)
        else:
            # fall off the FSM
            return False

print fsmsim("",1,edges,accepting) # should return True

print fsmsim("q",1,edges,accepting) # should return True

print fsmsim("qqqqqqqqqqqqqq",1,edges,accepting) # should return True

print fsmsim("",1,edges,accepting) # should return True

print fsmsim("qqqqqqAqqqqqq",1,edges,accepting) # should return False

