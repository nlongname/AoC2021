from ast import literal_eval

with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    f.close

scanner_limits = [i for i,line in enumerate(data) if line.startswith('---')]
scanner_limits.append(len(data)+1)
data = [data[scanner_limits[i]+1:scanner_limits[i+1]-1] for i in range(len(scanner_limits)-1)]
data = [[literal_eval(p) for p in line] for line in data]

def generalized_distance(a:tuple,b:tuple) -> tuple:
    if len(a) != len(b):
        raise ValueError("Points must have the same dimensions")
    vector = [a[i]-b[i] for i in range(len(a))]
    pseudovector = set([abs(c) for c in vector])
    return vector, pseudovector #vector for transformations, pseudovector for matching



crossover = [None,None]
while crossover.count([]) < len(crossover)-1:
    #one "vector" between each pair of points in each scanner
    #chirality could technically cause false positives, but hopefully we can ignore that
    records = []
    vectors = []
    for scanner in data:
        scanner_records = {}
        scanner_vectors = []
        for i in range(len(scanner)):
            for j in range(len(scanner[i+1:])):
                vector, pseudovector = generalized_distance(scanner[i],scanner[i+j+1])
                pseudovector = tuple(sorted(pseudovector))
                scanner_vectors.append(pseudovector)
                scanner_records[tuple(pseudovector)]=(vector, (i,i+j+1))
        vectors.append(scanner_vectors)
        records.append(scanner_records)
    crossover = [[v for v in vectors[0] if v in vectors[i]] for i in range(len(vectors))]
    to_add = []
    for i,c in enumerate(crossover):
        if len(c) >= 66 and i != 0:
            first_vector = tuple(sorted(tuple(c[0])))
            zero_vector = records[0][first_vector][0]
            zero_points = [data[0][n] for n in records[0][first_vector][1]]
            other_vector = records[i][first_vector][0]
            other_points = [data[i][n] for n in records[i][first_vector][1]]
            axis_map = {}
            signs = [0,0,0]
            for j in range(3):
                if zero_vector[j] in other_vector:
                    axis_map[j] = other_vector.index(zero_vector[j])
                    signs[j] = 1
                else:
                    axis_map[j] = other_vector.index(-1*zero_vector[j])
                    signs[j] = -1
            minus_candidates = []
            plus_candidates = []
            for a in zero_points:
                for b in other_points:
                    b_zero = [b[axis_map[i]]*signs[i] for i in range(3)]
                    minus_candidates.append(tuple(a[k]-b_zero[k] for k in range(3)))
                    plus_candidates.append(tuple(a[k]+b_zero[k] for k in range(3)))
            minus_candidates = list(set([sc for sc in minus_candidates if minus_candidates.count(sc) > 1]))
            plus_candidates = list(set([sc for sc in plus_candidates if plus_candidates.count(sc) > 1]))
            second_vector = tuple(sorted(tuple(c[1])))
            zero_check_vector = records[0][second_vector][0]
            zero_check_points = [data[0][n] for n in records[0][second_vector][1]]
            other_check_vector = records[i][second_vector][0]
            other_check_points = [data[i][n] for n in records[i][second_vector][1]]
            for a in zero_check_points:
                for b in other_check_points:
                    b_zero = [b[axis_map[i]]*signs[i] for i in range(3)]
                    minus_candidates.append(tuple(a[k]-b_zero[k] for k in range(3)))
                    plus_candidates.append(tuple(a[k]+b_zero[k] for k in range(3)))
            best_minus = max(minus_candidates, key=lambda sc: minus_candidates.count(sc))
            best_plus = max(plus_candidates, key=lambda sc: plus_candidates.count(sc))
            if minus_candidates.count(best_minus) > plus_candidates.count(best_plus):
                minus = True
                scanner_location = best_minus
            else:
                minus = False
                scanner_location = best_plus
            print(i, scanner_location)
            if minus: #this is what we expect, our map is correct
                mapped_points = [tuple(p[axis_map[i]]*signs[i] + scanner_location[i] for i in range(3)) for p in data[i]]
            else:
                mapped_points = [tuple(p[axis_map[i]]*(-1)*signs[i] + scanner_location[i] for i in range(3)) for p in data[i]]
            to_add += mapped_points
            data[i] = []
    data[0] = list(set(data[0]+to_add))
    #print([len(d) for d in data])
print(len(data[0]))
