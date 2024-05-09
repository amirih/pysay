from mock.computations import run
def do_task( time=5):
    print(f"Task with {time} started...")
    run(time)
    print(f"Task with {time} completed...")