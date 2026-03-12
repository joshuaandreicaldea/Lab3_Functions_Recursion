# main.py

from access_control import compute_access_level, monitor, validate_access
from media_engine import signal_shutdown, play_count_stream

CONTROL_NUM = 3
FAVORITE_ARTIST = "IVOS"

print("===== EXERCISE 1: ACCESS CONTROL =====")

access_level = compute_access_level(CONTROL_NUM, FAVORITE_ARTIST)
decision = validate_access(access_level, CONTROL_NUM)

print("CONTROL_NUM Used:", CONTROL_NUM)
print("FAVORITE_ARTIST Used:", FAVORITE_ARTIST)
print("Computed Access Level:", access_level)
print("Threshold Applied:", CONTROL_NUM * 5)
print("Final Authorization Decision:", decision)


print("\n===== EXERCISE 2: SIGNAL SHUTDOWN =====")

power = CONTROL_NUM + len(FAVORITE_ARTIST)
calls = signal_shutdown(power)

print("Initial Signal Strength:", power)
print("Total Recursive Calls:", calls)


print("\n===== EXERCISE 3: STREAMING ANALYTICS =====")

limit = CONTROL_NUM + len(FAVORITE_ARTIST)

total_plays, records = play_count_stream(limit)

print("CONTROL_NUM Used:", CONTROL_NUM)
print("FAVORITE_ARTIST Used:", FAVORITE_ARTIST)
print("Computed Stream Limit:", limit)
print("Total Plays:", total_plays)
print("Number of Records Processed:", records)