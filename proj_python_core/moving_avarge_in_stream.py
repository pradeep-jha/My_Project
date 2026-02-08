class MovingAverage:
    def next(self,stream,size):
        n=len(stream)
        window_sum=0
        mov_avg=[]
        window=[]
        for i in range(n):
            window.append(stream[i])
            window_sum+=stream[i]
            print("window_sum"+str(window_sum))
            if len(window)<size:
                avg = window_sum / len(window)
                mov_avg.append(avg)
            elif len(window)>size:
                print(i)
                print(i-size)
                print(window)
                window_sum-=window[i-size]
                print("window_sum--" + str(window_sum))
                avg=window_sum/3
                mov_avg.append(avg)
            print("Mov avg final")
            print(mov_avg)
        return mov_avg
        pass

ma=MovingAverage()
print(ma.next([4,0,-4,8,12],3))