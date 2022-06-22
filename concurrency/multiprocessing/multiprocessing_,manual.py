from multiprocessing import Process
from time import sleep, perf_counter


def test_func():
    sleep(2)
    print("Voila!")


def main():
    start = perf_counter()
    processes = []

    # Run test_func() three times takes about 6 seconds
    # test_func()
    # test_func()
    # test_func()

    # run test_func() 3 times, but using multiprocessing takes significantly less time
    for i in range(3):
        proc = Process(target=test_func)
        processes.append(proc)

    for proc in processes:
        proc.start()

    for proc in processes:
        proc.join()

    end = perf_counter()
    total_time = end - start
    print(total_time)


if __name__ == "__main__":
    main()