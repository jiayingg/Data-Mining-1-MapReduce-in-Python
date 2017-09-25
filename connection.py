import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: first person
    # value: second person
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)
    mr.emit_intermediate(value, key)

def reducer(key, list_of_values):
    # key: a person
    # value: all connections with this person
    n = len(list_of_values)
    # If there are at least two people connected with this person
    if n > 1:
        for i in range(n-1):
            for j in range(i+1,n):
                ordered = []
                ordered.extend((list_of_values[i],list_of_values[j]))
                # Output in alphabetic order
                mr.emit((sorted(ordered)[0],sorted(ordered)[1],key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)