from collections import deque
from queue import Queue

class SeatNode:
    def __init__(self, seat_no):
        self.seat_no = seat_no
        self.booked = False
        self.left = None
        self.right = None

class SeatTree:
    def __init__(self):
        self.root = None

    def insert(self, seat_no):
        if not self.root:
            self.root = SeatNode(seat_no)
            return
        q = deque([self.root])
        while q:
            node = q.popleft()
            if not node.left:
                node.left = SeatNode(seat_no)
                return
            elif not node.right:
                node.right = SeatNode(seat_no)
                return
            else:
                q.append(node.left)
                q.append(node.right)

    def find_available_seat(self):
        if not self.root:
            return None
        q = deque([self.root])
        while q:
            node = q.popleft()
            if not node.booked:
                return node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return None
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.seat_no, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.seat_no, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.seat_no, end=" ")

    def level_order(self):
        if not self.root:
            return
        q = deque([self.root])
        while q:
            node = q.popleft()
            print(node.seat_no, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

seat_tree = SeatTree()
booking_queue = Queue()
waiting_list = deque()
booking_stack = []
seat_deque = deque()

def create_seats():
    n = int(input("Enter number of seats: "))
    if n == 0:
        print("No seats created")
        return
    for _ in range(n):
        seat = int(input("Enter seat number: "))
        seat_tree.insert(seat)
        seat_deque.append(seat)
    print("Seats created successfully")

def book_ticket():
    name = input("Passenger Name: ")
    p_type = input("Type (normal/tatkal): ").lower()
    booking_queue.put(name)

    seat = seat_tree.find_available_seat()
    if seat:
        seat.booked = True
        booking_stack.append((name, seat.seat_no))
        print(f"{name} booked Seat {seat.seat_no}")
    else:
        if p_type == "tatkal":
            waiting_list.appendleft(name)
        else:
            waiting_list.append(name)
        print(f"{name} added to Waiting List")

def cancel_ticket():
    if not booking_stack:
        print("No bookings to cancel")
        return

    name, seat_no = booking_stack.pop()
    print(f"Cancelled booking of {name} (Seat {seat_no})")

    # free seat
    q = deque([seat_tree.root])
    while q:
        node = q.popleft()
        if node.seat_no == seat_no:
            node.booked = False
            break
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    if waiting_list:
        next_p = waiting_list.popleft()
        node.booked = True
        booking_stack.append((next_p, seat_no))
        print(f"{next_p} allocated Seat {seat_no} from Waiting List")

def rotate_seats():
    if not seat_deque:
        print("No seats to rotate")
        return
    direction = input("Left or Right rotation (L/R): ").upper()
    k = int(input("Rotate by how many positions: "))
    if direction == "L":
        seat_deque.rotate(-k)
    else:
        seat_deque.rotate(k)
    print("Seat order after rotation:", list(seat_deque))

def admin_reports():
    if not seat_tree.root:
        print("No seats available")
        return
    print("Inorder:", end=" ")
    seat_tree.inorder(seat_tree.root)
    print("\nPreorder:", end=" ")
    seat_tree.preorder(seat_tree.root)
    print("\nPostorder:", end=" ")
    seat_tree.postorder(seat_tree.root)
    print("\nLevel Order:", end=" ")
    seat_tree.level_order()
    print()


while True:
    print("""
1. Create Seats
2. Book Ticket
3. Cancel Ticket
4. Rotate Seats
5. Admin Reports
6. Exit
""")
    choice = int(input("Enter choice: "))

    if choice == 1:
        create_seats()
    elif choice == 2:
        book_ticket()
    elif choice == 3:
        cancel_ticket()
    elif choice == 4:
        rotate_seats()
    elif choice == 5:
        admin_reports()
    elif choice == 6:
        print("System Closed")
        break
    else:
        print("Invalid choice")
