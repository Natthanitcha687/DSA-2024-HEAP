import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, val):
        heapq.heappush(self.heap, -val)  # ใช้ค่าเชิงลบเพื่อจำลอง Max Heap
    
    def pop(self):
        return -heapq.heappop(self.heap)  # คืนค่ากลับเป็นบวก
    
    def peek(self):
        return -self.heap[0] if self.heap else None
    
    def get_heap(self):
        return sorted([-val for val in self.heap], reverse=True)  # แสดงค่าเรียงลำดับเป็น Max Heap

# สร้าง Max Heap
max_heap = MaxHeap()
values = [5, 3, 8, 1, 2, 7, 6, 4]

# แทรกค่าลงใน Heap
for value in values:
    max_heap.push(value)

# แสดงผล Max Heap ที่ได้
print("Max Heap:", max_heap.get_heap())

for i in range(3):
    removed = max_heap.pop()
    print(f"After removing {removed}:", max_heap.get_heap())