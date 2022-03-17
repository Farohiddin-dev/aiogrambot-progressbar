from pytube import YouTube
import asyncio


async def download_video(link, name):
    yt = YouTube(link, on_progress_callback=on_progress)
    yt.streams.filter(progressive=True,
                      file_extension='mp4').order_by('resolution')[-1].download(output_path='export/',
                                                                                filename=f"{name}.mp4")
    yt.register_on_progress_callback(on_progress)


def on_progress(vid, chunk, bytes_remaining):
    total_size = vid.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    totalsz = (total_size/1024)/1024
    totalsz = round(totalsz,1)
    remain = (bytes_remaining / 1024) / 1024
    remain = round(remain, 1)
    dwnd = (bytes_downloaded / 1024) / 1024
    dwnd = round(dwnd, 1)
    percentage_of_completion = round(percentage_of_completion, 2)

    print(f'Total Size: {totalsz} MB')
    print(f'Download Progress: {percentage_of_completion}%, Total Size:{totalsz} MB, Downloaded: '
          f'{dwnd} MB, Remaining:{remain} MB')

# def on_complete(vid, chunk, bytes_remaining):
#     total_size = vid.filesize
#     bytes_downloaded = total_size - bytes_remaining
#     percentage_of_completion = bytes_downloaded / total_size * 100
#     totalsz = (total_size/1024)/1024
#     totalsz = round(totalsz,1)
#     remain = (bytes_remaining / 1024) / 1024
#     remain = round(remain, 1)
#     dwnd = (bytes_downloaded / 1024) / 1024
#     dwnd = round(dwnd, 1)
#     percentage_of_completion = round(percentage_of_completion, 2)
#
#     print(f'Total Size: {totalsz} MB')
#     print(f'Download Progress: {percentage_of_completion}%, Total Size:{totalsz} MB, Downloaded: '
#           f'{dwnd} MB, Remaining:{remain} MB')