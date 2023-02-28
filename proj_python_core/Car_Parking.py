cars=[5,2,8,14,10]
k=3
def car_covers(l,k):
    sorted_cars=sorted(cars)
    print(sorted_cars)
    min_cover_len =99999

    for i in range(len(sorted_cars)-k+1):

        tmp=sorted_cars[i+k-1]-sorted_cars[i]
        # print("tmp-->",tmp)
        if(tmp<min_cover_len):
            min_cover_len=tmp
    return ("minimum length of cover is --->",min_cover_len)

print(car_covers(cars,k))