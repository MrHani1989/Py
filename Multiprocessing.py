import multiprocessing
import time


def first_process(arg):
    while True:
        print("here is first process with arg {}".format(arg))
        time.sleep(1)


def second_process(arg):
    while True:
        print("here is second process with arg {}".format(arg))
        time.sleep(1)


if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=first_process, args=("a",))
    p2 = multiprocessing.Process(target=second_process, args=("b",))

    # starting processes
    p1.start()
    p2.start()

    while True:
        print("I'm here")
        time.sleep(5)
    # try to catch CTRL + C while joining for processes
    try:
        p1.join()
        p2.join()
    except KeyboardInterrupt:
        print("The application is stopped")
    finally:
        p1.terminate()
        p2.terminate()
