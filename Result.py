class Result:
    def __init__(self, elements, threads=1, task_size=0):
        self.elements = elements
        self.threads = threads
        self.task_size = task_size
        self.time_counts = []
        self.spead_up = None

    def add_time(self, time):
        self.time_counts.append(time)

    def count_average_time(self):
        return round(sum(self.time_counts) / len(self.time_counts), 11)

    def count_speed_up(self, sequential_speed):
        self.spead_up = sequential_speed / self.count_average_time()

    def print_res(self):
        print("{:<10} {:<4} {:4} {:<17} {:<17}".format(self.elements, self.threads, self.task_size,
                                                       round(self.time_counts[0], 11), self.count_average_time()))

        for i in range(1, len(self.time_counts)):
            print("{:<20} {:<17}".format(" ", round(self.time_counts[i], 11)))

    def get_info(self, sequential_speed):
        self.count_speed_up(sequential_speed)
        return [self.elements, self.threads, self.task_size, self.count_average_time(), round(self.spead_up, 8)]
