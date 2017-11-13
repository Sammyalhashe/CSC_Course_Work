# Implementation of Quick Sort in Python
# nlog(n) best case; n^2 worst case
from random import random

def Quick_Sort(array):
    quicksort(array,0,len(array)-1)

def quicksort(array,left,right):
    if(left>=right):`
        return
    pivot = array(int(random()*len(array)))
    index = partition(array,left,right,pivot)
    quicksort(array,left,index-1)
    quicksort(array,index,right)

def partition(array,left,right,pivot):
    while(left<=right):
        while(array[left]<pivot):
            left+=1
        while(array[right]>pivot):
            right-=1
        if(left<=right):
            swap(array,left,right)
            left+=1
            right-=1
    return left #index of the partition in array

def swap(array,left,right):
    array[left],array[right] = array[right],array[left]



