import heapq  # เพิ่มการ import heapq

class Patient:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority  # ระดับความรุนแรง 1-5 (1 = ฉุกเฉินมาก)

    def __lt__(self, other):  
        return self.priority < other.priority  # ใช้เปรียบเทียบ priority ใน Min Heap

class ERQueue:
    def __init__(self):
        self.queue = []  # ใช้เป็น Min Heap

    def add_patient(self, patient):
        heapq.heappush(self.queue, patient)  # เพิ่มผู้ป่วยเข้า Min Heap

    def treat_next_patient(self):
        if self.queue:
            return heapq.heappop(self.queue)  # นำผู้ป่วยที่มี priority ต่ำสุดออกจากคิว
        return None

# ตัวอย่างการใช้งาน
er = ERQueue()
er.add_patient(Patient("คนไข้ A", 1))  # หัวใจวาย
er.add_patient(Patient("คนไข้ B", 3))  # ปวดท้อง
er.add_patient(Patient("คนไข้ C", 2))  # กระดูกหัก

# รักษาผู้ป่วยที่ priority สูงสุด (ค่าต่ำสุด)
next_patient = er.treat_next_patient()
print(f"รักษาคนไข้: {next_patient.name}")