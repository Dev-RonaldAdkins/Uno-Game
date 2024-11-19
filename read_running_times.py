
def main():
    video_file = open("video_times.txt")

    total = 0.0
    count = 0

    for line in video_file:
        run_time = float(line)
        count += 1
        print("Run time for video #", count, "is",run_time, "seconds.") 
        total += run_time

    video_file.close()

    print("The total running time is", total, "seconds.")
main()