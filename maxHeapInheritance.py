from Heap import Heap


class maxHeap(Heap):
    """Max Heap:

    Binary Tree with following properties:
    1) Parent is always greater in value than children
    2) has height of log(N) (base 2)
    Has a heap that, by convention, has a initialization of [0]
    Also stores a current_size that is initialized at 0
    """

    def __init__(self, key=None):
        """constructor for heap

        Initializes the heap with [0] and the current_size at 0
        Also initializes the key() function for accessing the value for
        which the heap is built

        Keyword Arguments:
            key {function reference} -- functions accesses the value for which the heap is built. If it's None, then it looks at the array value itself. If the array holds objects with values inside, teh function should access those values within the object (default: {None})
        """
        super().__init__(key)  # for multi-inheritance

    @property
    def key(self):
        """key getter

        Returns:
            function -- [function that gives the basis for heap building]
        """
        return self._key

    @key.setter
    def key(self, key):
        """key settter

        [if the key is None, we make it the identity function, else we give it the passed function]

        Decorators:
            key.setter

        Arguments:
            key {[function]} -- [function that gives the basis for heap building]
        """
        if key is None:
            self._key = lambda x: x  # identity function
        else:
            self._key = key

    def insert(self, value):
        """[inserts a value into the heap]

        [appends at the end and then restores the heap property by comaring parent and child]

        Arguments:
            value {int/object} -- [value/object to be inserted in heap array]
        """
        self.heap.append(value)
        self.current_size += 1
        self.restoreHeap(self.current_size)

    # def swap(self, i1, i2):
    #     [swaps the elements of the heap]

    #     [at indices i1 and i2]

    #     Arguments:
    #         i1 {int} -- [index of first element]
    #         i2 {int} -- [index of second element]

    #     temp = self.heap[i1]
    #     self.heap[i1] = self.heap[i2]
    #     self.heap[i2] = temp

    def restoreHeap(self, size):
        """
        restores min heap property (use only for insert)
        """
        while (size // 2 > 0):
            if(self.key(self.heap[size // 2]) < self.key(self.heap[size])):
                self.swap(size, size // 2)
                size = size // 2
            else:
                break

                def deleteVal(self, val):
        """deletes an arbitrary value in heap (if it's there)

        Swaps the last value in heap with the value to be deleted
        Pops the heap and reduces its size
        If the value now in the place of the deleted value has a value less than
        its parent, bubble the index up, else bubbleDown

        Arguments:
            val {int} -- value to be deleted
        """

        for i in range(1, self.current_size + 1):
            if self.heap[i] == val:
                index = i
                break
        try:
            if index != self.current_size + 1:
                self.swap(index, self.current_size)
                self.current_size -= 1
                self.heap.pop()
                if self.heap[index] > self.heap[index // 2]:
                    self.bubbleUp(index)
                else:
                    self.bubbleDown(index)
            else:
                self.current_size -= 1
                self.heap.pop()

        except NameError as e:
            print("Value not in heap, NameError:", e)

    def bubbleUp(self, index):
        """[Used for deleting arbitrary value]

        [
        When deleting, we swap last value (one of smallest in min heap) with the value being deleted.
        Use this to bring the largest to the top. The next function would then restore its rightful place in the heap
        ]

        Arguments:
            index {int} -- [index where you want the value bubbled up]
        """
        while index // 2 > 0:
            if(self.key(self.heap[index // 2]) < self.key(self.heap[index])):
                self.swap(index, index // 2)
                index = index // 2
            else:
                break

    def deleteMax(self):
        """[deletes minimum element from the heap -> the root]

        [replaces it with the last element, then restores heap property]

        Returns:
            [int] -- [value deleted from heap]
        """
        return_val = self.key(self.heap[1])
        self.heap[1] = self.heap[self.current_size]
        self.current_size -= 1
        self.heap.pop()
        self.bubbleDown(1)
        return return_val

    def bubbleDown(self, i):
        """[restores max heap property by 'bubbling down' larger elements]

        [
        Compares the smallest child to the current parent until the parent is the smallest
        There is a recursive version below also
        ]

        Arguments:
            i {int} -- [index to start bubbling down]
        """
        while (i * 2 <= self.current_size):
            lc = self.getLargestChild(i)
            if(self.key(self.heap[lc]) > self.key(self.heap[i])):
                self.swap(i, lc)
                i = lc
            else:
                break

    def getLargestChild(self, i):
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
            largest = 2 * i
            if(self.key(self.heap[2 * i + 1]) > self.key(self.heap[largest])):
                largest = 2 * i + 1
            return largest

    def buildHeap(self, array, key=None):
        """
        @brief      Builds a heap.

        @param      self   The object
        @param      array  The array

        @return     The heap.
        """
        self.key = key
        index = len(array) // 2
        self.current_size = len(array)
        self.heap = [0] + array
        while (index > 0):
            self.bubbleDown(index)
            index -= 1

    def satisfyMaxHeapProperty(self, index, current_size):
        """
        @brief      recursive func satisfying min heap property

        @param      self          The object
        @param      index         The index
        @param      current_size  The current size

        @return     { no return val; alters self.heap }
        """
        LC = 2 * index
        RC = 2 * index + 1
        largest = index
        if(LC <= current_size and self.key(self.heap[LC]) > self.key(self.heap[index])):
            largest = LC
        if(RC <= current_size and self.key(self.heap[RC]) > self.key(self.heap[largest])):
            largest = RC
        if largest != index:
            self.swap(index, largest)
            self.satisfyMaxHeapProperty(largest, current_size)

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
            self.satisfyMaxHeapProperty(1, current_size)
        # restore the object heap
        self.buildHeap(sorted_arr)
        return (sorted_arr if reverse else sorted_arr[::-1])

    def reconstructHeap(self, key):
        self.key = key
        self.buildHeap(self.heap[1:])  # ingoring the 0 at front


if __name__ == '__main__':
    """
    main block to execute tests
    """
    test = [1, 5, 3, 4, 6, 7, 5, 3]
    print(test)
    Heap = maxHeap()
    Heap.buildHeap(test)
    print(Heap.heap)
    sorted_arr = Heap.HeapSort()
    print(sorted_arr)
    print(Heap.key)
