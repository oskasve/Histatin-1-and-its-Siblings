# This function creates data sets which are ready to be used for a contour plot
def contour_plotter(X, Y, Z):
    import numpy as np
    points = [] # Defines points to be used for the plot as well as minimum and maximum values
    max_x = min_x = 0
    max_y = min_y = 0
    max_z = min_z = 0
    for x, y, z in zip(X, Y, Z):
        point = []
        point.append(int(x))
        if int(x) > max_x:
            max_x = int(x)
        elif int(x) < min_x:
            min_x = int(x)
        point.append(int(y))
        if int(y) > max_y:
            max_y = int(y)
        elif int(y) < min_y:
            min_y = int(y)
        point.append(int(z))
        if int(z) > max_z:
            max_z = int(z)
        elif int(z) < min_z:
            min_z = int(z)
        points.append(point)

    xx = np.expand_dims(np.arange(min_x, max_x), axis=0) # Creates arrays
    yy = np.expand_dims(np.arange(min_y, max_y), axis=1) 
    XX, YY = np.meshgrid(xx, yy)
    Z = np.zeros(XX.shape)
    
    counter1 = 0 # Fills the Z array
    for x1, y1, z1 in zip(XX, YY, Z):
        counter2 = 0
        for x2, y2, z2 in zip(x1, y1, z1):
            for point in points:
                if point[0] == x2 and point[1] == y2:
                    Z[counter1, counter2] = point[2]
            counter2 += 1
        counter1 += 1
    return XX, YY, Z

