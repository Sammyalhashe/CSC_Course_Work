class Heap(object):
    """Min Heap:

    Binary Tree with following properties:
    1) Parent is always less in value than children
    2) has height of log(N) (base 2)
    Has a heap that, by convention, has a initialization of [0]
    Also stores a current_size that is initialized at 0
    """
    

    def helloWorld(self):
        print("Hello World")

    def __init__(self):
        """[summary]

        [description]
        """
        super(Heap, self).__init__()  # for multi-inheritance
        self.heap = [0]
        self.current_size = 0

    def insert(self, value):
        """[inserts a value into the heap]

        [appends at the end and then restores the heap property by comaring parent and child]

        Arguments:
            value {int} -- [value to be inserted in heap]
        """
        self.heap.append(value)
        self.current_size += 1
        self.restoreHeap(self.current_size)

    def swap(self, i1, i2):
        """[swaps the elements of the heap]

        [at indices i1 and i2]

        Arguments:
            i1 {int} -- [index of first element]
            i2 {int} -- [index of second element]
        """
        temp = self.heap[i1]
        self.heap[i1] = self.heap[i2]
        self.heap[i2] = temp

    def restoreHeap(self, size):
        """
        restores min heap property (use only for insert)
        """
        while (size // 2 > 0):
            if(self.heap[size // 2] > self.heap[size]):
                self.swap(size, size // 2)
                size = size // 2
            else:
                break

    def bubbleUp(self, index):
        """[Used for deleting arbitrary value]

        [
        When deleting, we swap last value (biggest in min heap) with the value being deleted.
        Use this to bring the largest to the top. The next function would then restore its rightful place in the heap
        ]

        Arguments:
            index {int} -- [index where you want the value bubbled up]
        """
        while index // 2 > 0:
            if(self.heap[index // 2] < self.heap[index]):
                self.swap(index, index // 2)
                index = index // 2
            else:
                break

    def deleteMin(self):
        """[deletes minimum element from the heap -> the root]

        [replaces it with the last element, then restores heap property]

        Returns:
            [int] -- [value deleted from heap]
        """
        return_val = self.heap[1]
        self.heap[1] = self.heap[self.current_size]
        self.current_size -= 1
        self.heap.pop()
        self.bubbleDown(1)
        return return_val

    def deleteVal(self, index, key):
        """[summary]

        [description]

        Arguments:
            index {[type]} -- [description]
            key {[type]} -- [description]

        Returns:
            [int] -- [value being deleted, else if not in heap -1]
        """
        i = 1
        while i < self.current_size:
            if key > self.heap[i]:
                i = 2 * i + 1
            elif key < self.heap[i]:
                i = 2 * i
            else:
                self.swap(i, self.current_size)
                self.current_size -= 1
                ret = self.heap.pop()
                self.bubbleUp(i)
                self.bubbleDown(1)
                return ret
        print("value not here")
        return -1

    def bubbleDown(self, i):
        """[restores min heap property by 'bubbling down' larger elements]

        [
        Compares the smallest child to the current parent until the parent is the smallest
        There is a recursive version below also
        ]

        Arguments:
            i {int} -- [index to start bubbling down]
        """
        while (i * 2 <= self.current_size):
            mc = self.getSmallestChild(i)
            if(self.heap[mc] < self.heap[i]):
                self.swap(i, mc)
                i = mc
            else:
                break

    def getSmallestChild(self, i):
        """[gets the smallest child of the parent node]

        [
        The function where this function is actually called i makes sure that 2*i < current_size
        so this function only considers the case until 2*i + 1 <  current_size.
        Basically compares the parent with child nodes and finds the smallest one of the three
        ]

        Arguments:
            i {int} -- [index of parent node]

        Returns:
            number -- [index of smallest of the three -> could be parent]
        """
        # don't have to worry about 2*i being larger as this function wouldn't
        # be called
        if(2 * i + 1 > self.current_size):
            return 2 * i
        else:
            smallest = self.heap[2 * i]
            if(self.heap[2 * i + 1] < smallest):
                smallest = self.heap[2 * i + 1]
            return smallest

    def buildHeap(self, array):
        """
        @brief      Builds a heap.

        @param      self   The object
        @param      array  The array

        @return     The heap.
        """
        index = len(array) // 2
        self.current_size = len(array)
        self.heap = [0] + array
        while (index > 0):
            self.bubbleDown(index)
            index -= 1

    def satisfyMinHeapProperty(self, index, current_size):
        """
        @brief      recursive func satisfying min heap property

        @param      self          The object
        @param      index         The index
        @param      current_size  The current size

        @return     { no return val; alters self.heap }
        """
        LC = 2 * index
        RC = 2 * index + 1
        smallest = index
        if(LC <= current_size and self.heap[LC] < self.heap[index]):
            smallest = LC
        if(RC <= current_size and self.heap[RC] < self.heap[smallest]):
            smallest = RC
        if smallest != index:
            self.swap(index, smallest)
            self.satisfyMinHeapProperty(smallest, current_size)

    def HeapSort(self, reverse=True):
        """
        @brief      { function_description }

        @param      self     The object
        @param      reverse  If true sorted in descending order

        @return     { sorted array }
        """
        # array to be returned
        sorted_arr = []
        # defined in constructor for heap
        current_size = self.current_size
        while current_size != 0:
            self.swap(1, current_size)
            sorted_arr.append(self.heap[current_size])
            current_size -= 1
            self.satisfyMinHeapProperty(1, current_size)
        # restore the object heap
        self.buildHeap(sorted_arr)
        return (sorted_arr if reverse else sorted_arr[::-1])


if __name__ == '__main__':
    """
    main block to execute tests
    """
    test = [1, 5, 3, 4, 6, 7, 5, 3]
    print(test)
    Heap = Heap()
    Heap.buildHeap(test)
    print(Heap.heap)
    sorted_arr = Heap.HeapSort()
    print(sorted_arr)
