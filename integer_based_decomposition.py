# This function carries out integer-based decomposition
def int_decomp(data, file_path):
    import numpy as np
    frames = {} # Pairs frames and data points. Creates interval
    counter = 0
    for point in data: 
        frames.update({counter: int(point)})
        counter += 1
    pairs = frames.items()
    interval = range(int(np.sort(data)[0]), int(np.sort(data)[-1]))
    
    print('Please input filename') # Creates index file and distribution 
    name = input() 
    distribution = [] 
    with open(file_path + '/' + name + '.ndx', 'w') as file:
        for entry in interval:
            file.write('[ {} ]'.format(str(entry)) + '\n')
            counter = 0
            dist_count = 0
            for pair in pairs:
                if pair[1] == entry:
                    if counter == 6:
                        file.write('    ' + str(pair[0] + 1) + '\n')
                        counter = 0
                        dist_count += 1
                    else:
                        file.write('    ' + str(pair[0] + 1))
                        counter += 1
                        dist_count += 1
            file.write('\n')
            distribution.append(dist_count)

    with open(file_path + '/' + name + '_dist.dat', 'w') as file: # Creates distribution file
        for (i, d) in zip(interval, distribution):
            file.write(str(i) +  ' ' + str(d) + '\n')

