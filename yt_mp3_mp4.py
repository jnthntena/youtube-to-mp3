from pytubefix import YouTube 
import os 

def download_video(url, format_choice):
    yt = YouTube(url)
  
    if format_choice.lower() == '1':
        # extract only audio 
        stream = yt.streams.filter(only_audio=True).first()
        file_extension = 'mp3'
    elif format_choice.lower() == '2':
        # choose the stream with the highest resolution for video
        stream = yt.streams.get_highest_resolution()
        file_extension = 'mp4'
    else:
        format_choice = input("Invalid format choice. Please choose from the following:\n[1] -> 'mp3'\n[2] -> 'mp4'\n>> ")
        download_video(url, format_choice)
        return
  
    # check for destination to save file
    destination = input("Enter the destination (leave blank for current directory):\n") or '.'
  
    # download the file 
    out_file = stream.download(output_path=destination) 
  
    # save the file with the correct extension
    base, _ = os.path.splitext(out_file)
    new_file = base + f'.{file_extension}'
    os.rename(out_file, new_file)
  
    # result of success 
    print(yt.title + f" has been successfully downloaded as {file_extension.upper()}.")

# url input from user 
url = input("Enter the URL of the video you want to download:\n>> ")

# choose the format
format_choice = input("Select the desired format:\n[1] -> 'mp3'\n[2] -> 'mp4'\n>> ")

download_video(url, format_choice)