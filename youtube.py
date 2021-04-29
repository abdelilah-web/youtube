from pytube import YouTube

link = 'https://www.youtube.com/watch?v=YW0aIgcFO28&ab_channel=DYNAMLYRICS'

video = YouTube(link)

print(f'The video title is:\n{video.title}\n---------------- ')
print(f'The video description is :\n{video.description}\n--------------')
print(f'The video views are :\n{video.views}\n--------------')
print(f'The video rating is :\n{video.rating}\n--------------')
print(f'The video duration is :\n{video.length}\n--------------')

for stream in video.streams.filter(progressive=True):
    print((stream))

print(video.streams.get_highest_resolution())

def finish():
    print('dowload done')
video.streams.get_highest_resolution().download(output_path=r'E:\Nouveau dossier')
video.register_on_complete_callback(finish())