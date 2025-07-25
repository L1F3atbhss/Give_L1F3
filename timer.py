import time

def simple_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# Example: 10-second timer
simple_timer(10)
