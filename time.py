import utime

def monotonic():
    return utime.ticks_ms()

def sleep(seconds):
    utime.sleep(seconds)
    
def struct_time(param):
    utime.mktime(param)
    
def time():
    return utime.time()
    
def monotonic_ns():
    return utime.ticks_us()
    
def localtime(param):
    return utime.localtime(param)
    
def mktime(param):
    return utime.mktime(param)

