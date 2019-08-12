"""
def insertion(lst, low, high) :
    for i in range(low+1, high+1) :
        tmp = lst[i]
        while lst[i-1] > tmp and i > low:
            lst[i] = lst[i-1]
            i -= 1
            lst[i] = tmp

lst = [ 1, 2, 3, 4, 5]
insertion(lst,0,4)
print(lst)

def selection_sort(lst, low, high) :
    for i in range(low, high) :
        min = i
        for j in range(i, high+1) :
            if lst[min] > lst[j] : min = j
            lst[min], lst[i] = lst[i], lst[min]

lst = [ 7, 4, 6, 8, 4, 2]
selection_sort(lst, 0, 5)
print(lst)


def quick(lst, low, high) :
    if low >= high : return

    length = len(lst)
    pivot = lst[low]

    j = low
    for i in range(low+1, high+1) :
        if lst[i] < pivot :
            j += 1

            lst[i], lst[j] = lst[j], lst[i]
            lst[j], lst[low] = lst[low], lst[j]

        quick(lst, low, j-1)
        quick(lst, j+1, high)

lst = [ 5, 3, 9, 8, 1]
quick(lst, 0, 4)
print(lst)
"""

data = 'aaaaabbbbbbbcccccccceeeessssdddd'
encoded = ''

count = 1
for i in range(1, len(data)):
    if data[i] == data[i - 1]:
        count += 1
    else:
        encoded += data[i-1] + str(count)
        count = 1

    if i == len(data) - 1:
        encoded += data[i] + str(count)