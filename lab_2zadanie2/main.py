
def function(list = []):
    for x in list:
       x = x*2
       print(x)
    return list

def function2(list = []):
    list_2 = [ x*2 for x in list]
    print(list_2)
    return list_2



integers = [10,20,30]

function(integers)
function2(integers)