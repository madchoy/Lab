import gevent
from gevent.pool import Pool

# pool has a limit of 2.  that way, only a certain number of greenlets can run at a time.
# set a limitation...
pool = Pool(2)

def hello_from(n):
    print('Size of pool', len(pool))

# this would start up 3 greenlets.  if the pool was not limited.
pool.map(hello_from, xrange(5))
