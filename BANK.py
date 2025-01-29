import heapq
from datetime import datetime
import time

class BankCustomer:
    queue_counter = 1  # ตัวนับหมายเลขคิว
    
    def __init__(self, service_type, is_premium=False):
        self.queue_number = BankCustomer.queue_counter
        BankCustomer.queue_counter += 1
        self.service_type = service_type
        self.is_premium = is_premium
        self.arrival_time = datetime.now()
        self.priority = self._calculate_priority()
    
    def _calculate_priority(self):
        priority = {
            'ฝาก-ถอน': 3,
            'ชำระค่าบริการ': 2,
            'เปิดบัญชี': 1,
            'สินเชื่อ': 0
        }
        base_priority = priority.get(self.service_type, 4)
        if self.is_premium:
            base_priority -= 0.5
        return base_priority
    
    def __lt__(self, other):
        if self.priority == other.priority:
            return self.arrival_time < other.arrival_time
        return self.priority < other.priority
    
class BankQueue:
    def __init__(self):
        self.queue = []
        self.waiting_count = 0
    
    def add_customer(self, customer):
        heapq.heappush(self.queue, customer)
        self.waiting_count += 1
        print(f"หมายเลขคิว: {customer.queue_number}")
        print(f"บริการ: {customer.service_type}")
        print(f"สถานะ: {'Premium' if customer.is_premium else 'ทั่วไป'}")
        print(f"จำนวนคิวรอ: {self.waiting_count}")
        print("-" * 30)
    
    def serve_next_customer(self):
        if not self.queue:
            print("ไม่มีลูกค้าในคิว")
            return None
        
        customer = heapq.heappop(self.queue)
        self.waiting_count -= 1
        wait_time = datetime.now() - customer.arrival_time
        print(f"\nเรียกหมายเลขคิว: {customer.queue_number}")
        print(f"บริการ: {customer.service_type}")
        print(f"เวลารอ: {wait_time.seconds} วินาที")
        print(f"จำนวนคิวรอ: {self.waiting_count}")
        print("-" * 30)
        return customer
    
    def display_queue(self):
        if not self.queue:
            print("ไม่มีลูกค้าในคิว")
            return
        
        print("\nรายการคิวที่รอ:")
        temp_queue = self.queue.copy()
        while temp_queue:
            customer = heapq.heappop(temp_queue)
            print(f"คิว {customer.queue_number} - {customer.service_type}")
        print("-" * 30)

# ตัวอย่างการใช้งาน
def demo_bank_queue():
    bank = BankQueue()
    customers = [
        BankCustomer("ฝาก-ถอน"),
        BankCustomer("สินเชื่อ", is_premium=True),
        BankCustomer("ชำระค่าบริการ"),
        BankCustomer("เปิดบัญชี"),
        BankCustomer("สินเชื่อ")
    ]
    
    for customer in customers:
        bank.add_customer(customer)
        time.sleep(1)
    
    print("\nแสดงลำดับคิว:")
    bank.display_queue()
    
    print("\nเริ่มเรียกลูกค้า:")
    for _ in range(len(customers)):
        bank.serve_next_customer()
        time.sleep(1)

if __name__ == "__main__":
    demo_bank_queue()
