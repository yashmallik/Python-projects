def pascal_traingle(nums):

    traingle = [[1]]
    for i in range(nums-1):
        temp_list = [1]
        for j in range(i):
            temp_list.append(traingle[i][j] + traingle[i][j+1])
        temp_list.append(1)
        traingle.append(temp_list)
    return traingle


print(pascal_traingle(10)
      )
