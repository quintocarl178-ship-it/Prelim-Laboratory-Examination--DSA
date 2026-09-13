class Student:

    def __init__(self, student_id, name, course, year_level):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.year_level = year_level

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Course: {self.course} | Year: {self.year_level}"


class DynamicArray:

    def __init__(self, initial_capacity=5):
        self.capacity = initial_capacity
        self.count = 0
        self.array = [None] * self.capacity

    def size(self):
        return self.count

    def resize(self):
        old_capacity = self.capacity
        self.capacity = old_capacity * 2

        new_array = [None] * self.capacity

        for i in range(self.count):
            new_array[i] = self.array[i]

        self.array = new_array

        print(f"\n[SYSTEM]: Capacity increased from {old_capacity} to {self.capacity}")

    def add(self, student):

        if self.count == self.capacity:
            print("\n[SYSTEM]: Array is full. Resizing capacity...")
            self.resize()

        self.array[self.count] = student
        self.count += 1

        print("[SUCCESS]: Student added successfully.")

    def get(self, index):

        if 0 <= index < self.count:
            return self.array[index]

        return None

    def search(self, student_id):

        for i in range(self.count):

            if self.array[i].student_id == student_id:
                return i

        return -1

    def set(self, student_id, new_name, new_course, new_year):

        index = self.search(student_id)

        if index != -1:
            self.array[index].name = new_name
            self.array[index].course = new_course
            self.array[index].year_level = new_year
            return True

        return False

    def remove(self, student_id):

        index = self.search(student_id)

        if index == -1:
            return False

        for i in range(index, self.count - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.count - 1] = None
        self.count -= 1

        return True

    def display(self):

        if self.count == 0:
            print("No student records found.")
            return

        print("\n--- STUDENT RECORDS ---")

        for i in range(self.count):
            print(f"[{i + 1}] {self.array[i]}")


def main_student_manager():

    array_adt = DynamicArray(initial_capacity=5)

    while True:

        print("\n" + "=" * 30)
        print(" STUDENT RECORD MANAGER ")
        print("=" * 30)
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Remove Student")
        print("6. Display Array Information")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            sid = input("Enter Student ID: ").strip()

            if array_adt.search(sid) != -1:
                print("[ERROR]: Student ID already exists!")
                continue

            name = input("Enter Student Name: ").strip()
            course = input("Enter Course: ").strip()
            year = input("Enter Year Level: ").strip()

            student = Student(sid, name, course, year)

            array_adt.add(student)

        elif choice == "2":

            array_adt.display()

        elif choice == "3":

            sid = input("Enter Student ID to search: ").strip()

            idx = array_adt.search(sid)

            if idx != -1:
                print(f"\n[FOUND]: {array_adt.get(idx)}")
            else:
                print("\n[ERROR]: Student not found.")

        elif choice == "4":

            sid = input("Enter Student ID to update: ").strip()

            idx = array_adt.search(sid)

            if idx != -1:

                print(f"Current Record: {array_adt.get(idx)}")

                new_name = input("Enter New Name: ").strip()
                new_course = input("Enter New Course: ").strip()
                new_year = input("Enter New Year Level: ").strip()

                array_adt.set(sid, new_name, new_course, new_year)

                print("[SUCCESS]: Student record updated successfully.")

            else:
                print("\n[ERROR]: Student not found.")

        elif choice == "5":

            sid = input("Enter Student ID to remove: ").strip()

            if array_adt.remove(sid):
                print("[SUCCESS]: Student removed and array shifted.")
            else:
                print("\n[ERROR]: Student record not found.")

        elif choice == "6":

            print(f"\nCurrent Students Count: {array_adt.size()}")
            print(f"Current Capacity: {array_adt.capacity}")

        elif choice == "7":

            print("Exiting Student Record Manager...")
            break

        else:

            print("[ERROR]: Invalid choice. Please select from 1 to 7.")


if __name__ == "__main__":
    main_student_manager()