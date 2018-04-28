import threading
import random

class MaxThread(threading.Thread):
    
    def __init__(self, lo, hi, list_nums):
        threading.Thread.__init__(self)
        self.lo        = lo
        self.hi        = hi
        self.list_nums = list_nums
        self.max       = 0

    def run(self):
        self.set_max()

    def set_max(self):
        i = self.lo
        while i < self.hi:
            # Begin code
            if self.max < self.list_nums[i]:
                self.max = self.list_nums[i]
            i += 1
        return

    def get_max(self):
        return self.max

    def print_list(self):
        str_list = ''
        i = self.lo
        while i < self.hi:
            str_list += str(self.list_nums[i]) + ';'
            i += 1
        return str_list

    
def tim_max(list_numbers, n_threads):
    gt_max       = []
    so_pt        = len(list_numbers)
    list_threads = []
    i            = 0

    while i < n_threads:
        lo = int((i*so_pt)/n_threads)
        hi = int((i+1)*so_pt/n_threads)
        thread = MaxThread(lo,hi, list_numbers)
        list_threads.append(thread)
        list_threads[i].start()
        i += 1
    
    j = 0
    
    while j < n_threads:
        list_threads[j].join()
        gt_max.append(list_threads[j].get_max()) 
        print('Thread ', j + 1, ':', list_threads[j].print_list())
        print('Gia tri max thread ', j + 1, ':', list_threads[j].get_max())
        j += 1
    return max(gt_max)

if __name__ == '__main__':
    list_numbers = []
    n            = int(input('Nhap so phan tu: \t'))
    i            = 0
    gt_max       = 0

    while i < n:
        list_numbers.append(random.randrange(100))
        i += 1
    print('List:', list_numbers)

    #Begin thread
    n_threads = int(input('Nhap vao so thread: \t'))
    gt_max    = tim_max(list_numbers, n_threads)
    print('Gia tri max la: ', gt_max)
