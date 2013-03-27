import time

# What is interesting here is that the multiprocessing.pool way of executing the threads runs every thread at once.  If I just had run1 go, with a one second wait,
# it would finish )+1+2+3+...+9 seconds later

# the gevent.pool will run and execute before allowing the next thread to go

# this is what makes gevent.pool deterministic.

def echo(i):
    print 'in echo%d'%i
    time.sleep(1*i)
    print 'finished%d'%i
    return i

# Non Deterministic Process Pool

#from multiprocessing.pool import Pool
#
#p = Pool(10)
#run1 = [a for a in p.imap_unordered(echo, xrange(10))]
#run2 = [a for a in p.imap_unordered(echo, xrange(10))]
#run3 = [a for a in p.imap_unordered(echo, xrange(10))]
#run4 = [a for a in p.imap_unordered(echo, xrange(10))]

#for a in p.imap_unordered(echo, xrange(10)):
#    print a
#print( run1 == run2 == run3 == run4 )

# Deterministic Gevent Pool

from gevent.pool import Pool

p = Pool(10)
run1 = [a for a in p.imap_unordered(echo, xrange(10))]
#run2 = [a for a in p.imap_unordered(echo, xrange(10))]
#run3 = [a for a in p.imap_unordered(echo, xrange(10))]
#run4 = [a for a in p.imap_unordered(echo, xrange(10))]
#
#print( run1 == run2 == run3 == run4 )
