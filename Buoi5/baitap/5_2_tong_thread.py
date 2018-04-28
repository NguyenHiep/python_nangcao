import threading
import random

class SumThread(threading.Thread):
    
    def __init__(self, lo, hi, list_nums):
        threading.Thread.__init__(self)
        self.lo        = lo
        self.hi        = hi
        self.list_nums = list_nums
        self.sum       = 0

    def run(self):
        self.set_sum()

    def set_sum(self):
        i = self.lo
        while i < self.hi:
            self.sum += self.list_nums[i]
            i += 1
        return

    def get_sum(self):
        return self.sum

    def print_list(self):
        str_list = ''
        i = self.lo
        while i < self.hi:
            str_list += str(self.list_nums[i]) + ';'
            i += 1
        return str_list

def tinh_tong(list_numbers, n_threads):
    tong         = 0
    so_pt        = len(list_numbers)
    list_threads = []
    i            = 0

    while i < n_threads:
        lo = int((i*so_pt)/n_threads)
        hi = int((i+1)*so_pt/n_threads)
        thread = SumThread(lo,hi, list_numbers)
        list_threads.append(thread)
        list_threads[i].start()
        i += 1
    
    j = 0
    
    while j < n_threads:
        list_threads[j].join()
        tong += list_threads[j].get_sum()
        print('Thread ', j + 1, ':', list_threads[j].print_list())
        j += 1
    return tong

if __name__ == '__main__':
    list_numbers = []
    n = int(input('Nhap so phan tu: \t'))
    i = 0

    while i < n:
        list_numbers.append(random.randrange(9))
        i += 1
    print('List:', list_numbers)

    #Begin thread
    n_threads = int(input('Nhap vao so thread: \t'))
    sum = tinh_tong(list_numbers, n_threads)
    print('Tong list la: ', sum)