def ping(i):
    if i>0:
        return pong(i-1)
    return "0"

def pong(i):
    if i>0:
        return ping(i-1)
    return "1"

print(ping(28),end=' ')