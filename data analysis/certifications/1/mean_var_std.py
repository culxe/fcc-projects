import numpy as np

def calculate(list):
    if (len(list) != 9):
        raise ValueError("List must contain nine numbers.")

    list_3x3=np.array(list)
    list_3x3=list_3x3.reshape(3,3)

    # mean
    mean1= np.mean(list_3x3, axis=0)
    mean2= np.mean(list_3x3, axis=1)
    mean3= np.mean(list_3x3)

    #variance
    var1= np.var(list_3x3, axis=0)
    var2= np.var(list_3x3, axis=1)
    var3= np.var(list_3x3)

    #standart deviation
    std1=np.std(list_3x3, axis=0)
    std2=np.std(list_3x3, axis=1)
    std3=np.std(list_3x3)

    # max
    max1= np.max(list_3x3, axis=0)
    max2= np.max(list_3x3, axis=1)
    max3= np.max(list_3x3)

    # min
    min1= np.min(list_3x3, axis=0)
    min2= np.min(list_3x3, axis=1)
    min3= np.min(list_3x3)

    # sum
    sum1= np.sum(list_3x3, axis=0)
    sum2= np.sum(list_3x3, axis=1)
    sum3= np.sum(list_3x3)


    calculations={
      'mean': [mean1.tolist(), mean2.tolist(), mean3], 
      'variance': [var1.tolist(), var2.tolist(), var3],
      'standard deviation': [std1.tolist(), std2.tolist(), std3],
      'max': [max1.tolist(), max2.tolist(), max3],
      'min': [min1.tolist(), min2.tolist(), min3],
      'sum': [sum1.tolist(), sum2.tolist(), sum3]
    }


    return calculations