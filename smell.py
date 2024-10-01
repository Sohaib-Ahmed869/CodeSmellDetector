import random
import string

class GodClass:
    def __init__(self):
        self.data = []

    def generate_and_process_data(self, count, length, sort_asc, random_range_start, random_range_end):
        for _ in range(count):
            random_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))
            random_number = random.randint(random_range_start, random_range_end)
            self.data.append((random_string, random_number))
        
        print(f"Generated {len(self.data)} random string and number pairs.")

        if sort_asc:
            self.data.sort(key=lambda x: x[1])
        else:
            self.data.sort(key=lambda x: x[1], reverse=True)

        print(f"Data sorted: {self.data}")

        self.filter_data()

        self.show_statistics()

    def filter_data(self, threshold=10, case_sensitive=False, filter_by="number", operation="greater", start=0, end=100):
        filtered_data = []

        if filter_by == "number":
            if operation == "greater":
                filtered_data = [item for item in self.data if item[1] > threshold]
            elif operation == "less":
                filtered_data = [item for item in self.data if item[1] < threshold]
        elif filter_by == "string":
            if case_sensitive:
                filtered_data = [item for item in self.data if start <= ord(item[0][0]) <= end]
            else:
                filtered_data = [item for item in self.data if start <= ord(item[0][0].lower()) <= end]

        self.data = filtered_data
        print(f"Filtered data: {self.data}")

    def show_statistics(self):
        if len(self.data) == 0:
            print("No data available.")
            return

        sum_numbers = sum(item[1] for item in self.data)
        avg_number = sum_numbers / len(self.data)
        print(f"Sum of numbers: {sum_numbers}")
        print(f"Average of numbers: {avg_number}")

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def external_process_data(god_class, count, length, sort_asc, random_range_start, random_range_end, threshold=10):
    god_class.generate_and_process_data(count, length, sort_asc, random_range_start, random_range_end)
    god_class.filter_data(threshold=threshold)

def main():
    gc = GodClass()

    gc.generate_and_process_data(5, 10, True, 1, 100)

    external_process_data(gc, 10, 8, False, 1, 200, 50)

if __name__ == "__main__":
    main()
