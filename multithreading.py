import concurrent.futures


# function to run
def f(arg):
    print(arg)


args = list(range(100))  # arguments to pass to f
threads = 100  # number of concurrent threads
with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
    executor.map(f, args)
