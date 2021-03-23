#Here we import pytube, if your're using pycharm, download in setting/pythoninterpreter

from pytube import YouTube
link = input("Enter the video link: ")
yt = YouTube(link)

#print some info from the vid

print("Title of the video: ", yt.title)
print("Views on the video: ", yt.views)
print("Length of the video: ", yt.length)
ys = yt.streams.get_highest_resolution()
#wait

print("Downloading the video... ")
ys.download()
print("Your download is complete!")
#done!
