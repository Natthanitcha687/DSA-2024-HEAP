import heapq

def insert_to_max_heap(heap, value):
    # ใช้ heapq แต่ต้องเก็บค่าติดลบเพื่อจำลอง Max Heap
    heapq.heappush(heap, -value)

def is_max_heap(arr):
    n = len(arr)
    for i in range(n // 2):  # ตรวจสอบเฉพาะ parent nodes
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            return False
        if right < n and arr[i] < arr[right]:
            return False
    return True

# ทดสอบแทรกค่าใน Max Heap
values = [5, 3, 8, 1, 2, 7, 6, 4]
max_heap = []
for value in values:
    insert_to_max_heap(max_heap, value)

# แปลงกลับเป็นค่าบวกเพื่อแสดงค่า Max Heap ที่แท้จริง
max_heap = [-x for x in max_heap]
print("Max Heap:", max_heap)

# ทดสอบฟังก์ชัน is_max_heap
print("Is max heap?", is_max_heap(max_heap))
