def selectionSort(arr):                    #TAKES ARRAY AS A INPUT

    for i in range(len(arr)):              #LOOPS THROUGH THE ARRRAY FROM FIRST ELEMENT TO LAST ELEMENT THROUGH VAR I

        min = float('-inf')                 # INITIALIZES MIN AS NEGSTIVE INFINITY

        for j in range(i + 1, len(arr)):       #ENTERS THE INNER LOOP AND ITERATE FROM I+1 TO LAST ELEMENT

            if arr[i] > arr[j]:                      #compares THE ELEMENT AT INDEX I AND J 

                arr[i],arr[j] = arr[j], arr[i]        # IF SMALLER FOUND THEN IT SWAPS THE ELEMENTS
                                                    #INNER LOOP CONTINUES TILL IT GETS MINM ELEMENT FOR THAT INDEX




    return arr                                       

    
print(selectionSort([89,56,45,34,65,76]))



def greedy_selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Find the minimum element in the remaining unsorted part of the array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the minimum element with the current element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Example usage
arr = [5, 3, 8, 2, 1, 7]
sorted_arr = greedy_selection_sort(arr)
print(sorted_arr)