import timeit

class Timer: 
    """Idea from: http://preshing.com/20110924/timing-your-code-using-pythons-with-statement/
    """
    def __init__(self, name='Timer', verbose=True):
        self.name = name
        self.verbose = verbose
    
    def __enter__(self):  
        if self.verbose:
            print( 'Starting {}...'.format(self.name) )
        self.start = timeit.default_timer()
        return self

    def __exit__(self, *args):
        self.end = timeit.default_timer()
        self.elapsed = self.end - self.start
        if self.verbose:
            print( '{}: elapsed {} sec'.format(self.name, self.elapsed) )