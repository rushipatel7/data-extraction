from pytube import YouTube

url = "https://www.youtube.com/watch?v=7BXJIjfJCsA"
my_video = YouTube(url)

print(my_video.title)
print(my_video.thumbnail_url)

# set stream resolution
my_video1 = my_video.streams.get_highest_resolution()

# or my_video = my_video.streams.first()

# for stream in my_video:
    # print(stream)

my_video1.download()


# video all resolution
for i in my_video.streams.filter(progressive=True):
    print(i.resolution)