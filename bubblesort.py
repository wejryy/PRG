def bubblesort(cisla):
    n = len(cisla)
    for i in range(0, n - 1):
        swapped = False
        for j in range(0, n-i-1):
            if cisla[j] > cisla[j + 1]:
                swapped = True
                cisla[j], cisla[j + 1] = cisla[j + 1], cisla[j]
                if not swapped:
                    return
                
cisla= [64,20,50,6074,9,5,69,54,25897,0,3684,674]

bubblesort(cisla)

for i in range(len(cisla)):
    print("% d" % cisla[i], end="")

        
