import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: not in use, just put 1
    # value: list of X and X square
    mr.emit_intermediate(1, [record, [x**2 for x in record]])

def reducer(key, list_of_values):
    # Reducer calculate everything: E(X^2), E(X)^2
    exp=[]    # for E(X)^2
    exp2=[]   # for E(X^2)
    for i in range(len(list_of_values)):
        for j in range(len(list_of_values[i][0])):
            exp.append(list_of_values[i][0][j])
        for j in range(len(list_of_values[i][1])):
            exp2.append(list_of_values[i][1][j])
    mr.emit(sum(exp2)/float(len(exp2))-(sum(exp)/float(len(exp)))**2)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)