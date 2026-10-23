"""Min-heap priority queue for emergency intake (1 is most urgent)."""


class Patient:
    def __init__(self, name, urgency):
        if not isinstance(urgency, int) or isinstance(urgency, bool) or not 1 <= urgency <= 10:
            raise ValueError("Urgency must be an integer from 1 to 10.")
        self.name = name
        self.urgency = urgency


class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index].urgency >= self.data[parent].urgency:
                break
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent

    def heapify_down(self, index):
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index
            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right
            if smallest == index:
                break
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest

    def insert(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("Only Patient objects can be inserted.")
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def peek(self):
        return self.data[0] if self.data else None

    def remove_min(self):
        if not self.data:
            return None
        most_urgent = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self.heapify_down(0)
        return most_urgent


if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()
    next_up = heap.peek()
    print("Next up:", next_up.name, next_up.urgency)
    served = heap.remove_min()
    print("Served:", served.name)
    heap.print_heap()
    print("Empty queue peek/remove:", MinHeap().peek(), MinHeap().remove_min())
