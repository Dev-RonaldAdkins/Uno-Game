def main():

    num_videos= int(input("Enter the number of videos: "))
   
    video_times = open("video_times.txt", "w")
    

    for count in range(1, num_videos + 1):
       run_time = float(input("Enter the runtime of video #" + str(count) + ": "))
       video_times.write(str(run_time) +"\n")

    video_times.close()
    print("The times have been saved to video_times.txt")

main()

        