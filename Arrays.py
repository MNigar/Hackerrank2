import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    a = numpy.array(arr,float)
    arr1=numpy.flipud(a)
    return arr1
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
