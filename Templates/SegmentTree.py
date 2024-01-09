from math import ceil, log2
class SegmentTree:
    def __init__(self, input_array, func=lambda x,y : x + y) -> None:
        self.input_array = input_array
        self.n = len(self.input_array)
        self.height = ceil(log2(self.n))
        self.n_nodes = 2 ** (self.height + 1) - 1
        self.segment_array = [None] * self.n_nodes
        self.func = func
        self.INF = 10 ** 20
        self.build()

    def _build_segment_tree(self, left, right, index):
        # leaf node case
        if left > right:
            return
        
        if left == right:
            self.segment_array[index] = self.input_array[left]
            return
        
        mid = (left + right) // 2
        self._build_segment_tree(left, mid, 2*index + 1)
        self._build_segment_tree(mid + 1, right, 2*index + 2)

        self.segment_array[index] = self.func(self.segment_array[2*index + 1], self.segment_array[2*index + 2])
        return

    def build(self):
        left = 0
        right = self.n - 1
        index = 0
        self._build_segment_tree(left, right, index)

    def _search(self, ql, qr, left, right, index):
        # leaf node case
        if left > right or ql > right or qr < left:
            return -self.INF
        
        if ql <= left and right <= qr:
            return self.segment_array[index]        
        
        mid = (left + right) // 2
        left_val = self._search(ql, qr, left, mid, 2 * index + 1)
        right_val = self._search(ql, qr, mid + 1, right, 2 * index + 2)

        return self.func(left_val, right_val)

    def query(self, ql, qr):
        left = 0
        right = self.n - 1
        index = 0

        return self._search(ql, qr, left, right, index)



temp = [1,3,-1,-3,5,3,6,7]
n = len(temp)
func = lambda x,y: x if x > y else y

seg = SegmentTree(temp, func)

print(seg.segment_array)
k = 3
for i in range(0, n - k + 1):
    print(seg.query(i,i + k - 1))