import time
import multiprocessing


def read_info(name):
    all_data = []  

    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())

if __name__ == '__main__':
    filenames = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f"Линейное выполнение: {end_time - start_time:.6f} секунд")

    # Многопроцессный вызов
    start_time = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Многопроцессное выполнение: {end_time - start_time:.6f} секунд")
