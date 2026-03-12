# media_engine.py

def monitor(func):
    def wrapper(*args, **kwargs):
        print("Processing Started")
        result = func(*args, **kwargs)
        print("Processing Completed")
        return result
    return wrapper


@monitor
def signal_shutdown(power):
    print("Signal Strength:", power)

    if power == 0:
        return 1

    return 1 + signal_shutdown(power - 1)


@monitor
def play_count_stream(limit):
    total = 0
    count = 0

    for i in range(limit):
        if i % 2 == 0:
            play = i ** 2
            print("Play Count:", play)
            total += play
            count += 1

    return total, count