from multiprocessing import Process
from multiprocessing.dummy import Pool
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from time import time


def factorize(*numbers):
    lst = []
    for i in numbers:
        pre_lst = []
        for j in range(1, i + 1):
            if i % j == 0:
                pre_lst.append(j)
        lst.append(pre_lst)
    return lst
    # raise NotImplementedError()


if __name__ == '__main__':
    timer = time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print(a, b, c, d, sep='\n')
    print(f'Done in {time() - timer:.2f} seconds')

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
    timer_1pr = time()
    pr = Process(target=factorize, args=(128, 255, 99999, 10651060))
    pr.start()
    print('Done by 1 process in {:.3f} seconds'.format(time() - timer_1pr))

    timer_poll = time()
    with Pool(4) as p:
        result = p.map(factorize, [128, 255, 99999, 10651060])
        print('Done by 4 processes dummy in {:.3f} seconds'.format(time() - timer_poll))

    timer_pool_executor = time()
    with ProcessPoolExecutor(max_workers=4) as p:
        result_pr = p.map(factorize, [128, 255, 99999, 10651060])
        print('Done by 4 processes in {:.3f} seconds'.format(time() - timer_pool_executor))

    timer_thread_pool_executor = time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(factorize, [128, 255, 99999, 10651060])
        print('Done by 4 threads in {:.3f} seconds'.format(time() - timer_thread_pool_executor))


