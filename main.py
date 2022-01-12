# Requires a folder named 'Songs' and 'Videos' in the same directory.

import youtube_dl
import os


class InvalidNumber(Exception):
    pass


class Colours:
    black = "\033[0;30m"
    red = "\033[0;31m"
    green = "\033[0;32m"
    yellow = "\033[0;33m"
    blue = "\033[0;34m"
    magenta = "\033[0;35m"
    cyan = "\033[0;36m"
    white = "\033[0;37m"
    bright_black = "\033[0;90m"
    bright_red = "\033[0;91m"
    bright_green = "\033[0;92m"
    bright_yellow = "\033[0;93m"
    bright_blue = "\033[0;94m"
    bright_magenta = "\033[0;95m"
    bright_cyan = "\033[0;96m"
    bright_white = "\033[0;97m"


def downloadcheck(d):
    if d['status'] == 'finished':
        print(Colours.bright_green + 'Done downloading, now converting ...')


ydl_opts = {
    'no_warnings': True,
    'outtmpl': '%(id)s',
    'noplaylist': True,
    'progress_hooks': [downloadcheck],
}


def formatCheck(formatNum):
    if formatNum == 1:
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['audioformat'] = "mp3"
        ydl_opts['extractaudio']: True
        if formatNum == 2:
            ydl_opts['format'] = 'bestvideo[height<=480]+bestaudio/best[height<=480]'
            ydl_opts['videoformat'] = "mp4"


def download(opts: ydl_opts, url):
    try:
        with youtube_dl.YoutubeDL(opts) as ydl:
            meta = ydl.extract_info(url, download=True)
            return meta
    except youtube_dl.utils.DownloadError:
        print('INVALID URL.')
        return False


def nameR(meta: dict, url, formatNum):
    globDict = {}
    title = meta['title']
    title = title.replace('/', '')
    if formatNum == 1:
        globDict['filetype'] = '.mp3'
        globDict['dir'] = 'Songs'
    elif formatNum == 2:
        globDict['filetype'] = '.mp4'
        globDict['dir'] = 'Videos'
    Filetype = globDict['filetype']
    directory = globDict['dir']
    try:
        totalname = f'{directory}/{title}{Filetype}'
        os.rename(url, totalname)
        print(Colours.bright_green + 'DONE!')
    except:
        print('The naming operation failed. Please enter a name of your own.')
        inputn = input('>>> ')
        totalname = f'{directory}/{inputn}{Filetype}'
        os.rename(url, totalname)
        print(Colours.bright_green + 'DONE!')


def main():
    while True:
        url = input(Colours.bright_red + 'url>>> ')

        if url.startswith('https://www.youtube.com/watch?v'):
            url = url.replace('https://www.youtube.com/watch?v=', 'https://www.youtube.com/watch?v=')

        while True:
            try:
                formatIn = int(input(Colours.bright_blue + '''Choose your format
                1) MP3 (Audio)
                2) MP4 (Video)
                Enter 1 or 2
                >>> '''))
                if 0 >= formatIn or formatIn >= 3:
                    raise InvalidNumber
                else:
                    break
            except InvalidNumber:
                print('Enter a valid number (1 or 2)')
            except TypeError:
                print('Enter a valid number (1 or 2)')

        formatCheck(formatIn)
        meta = download(ydl_opts, url)

        if not meta:
            print(Colours.bright_red + 'Enter a real URL next time')
            continue

        nameR(meta, url, formatIn)

        print(Colours.bright_red + 'Do you want to try again? Type 1 for yes, anything else for no.')
        tryAgain = input('>>> ').replace(' ', '')
        if tryAgain != '1':
            break
    print(Colours.bright_cyan + 'Thanks for using!')


main()
