import multiprocessing as mp


# function to run
def f(arg):
    print(arg)


args = list(range(100))  # arguments to pass to f
# create pool with desired number of processes; mp.cpu_count() yields number of processors
pool = mp.Pool(processes=mp.cpu_count())
results = [pool.apply_async(f, args=[arg]) for arg in args]
results = [res.get() for res in results]
pool.close()  # don't forget to close pool!
