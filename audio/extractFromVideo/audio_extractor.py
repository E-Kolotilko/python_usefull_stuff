import moviepy.editor
#Note: moviepy is much richer in fuctionality that just extraction audio:
#cut video, compress, work with subtitles
import sys
from pathlib import Path

warning_string = """
Warning! This script creates audio files next to videos. Name is built by adding .mp3. 
Enter y if you are ok with it
"""

def extract_audio(source_file_path):
    source_file = Path(source_file_path);
    if not source_file.exists():
        print('File does not exist:{}'.format(source_file_path))
        return
    video = moviepy.editor.VideoFileClip(source_file_path)
    audio = video.audio;
    audio.write_audiofile(str(source_file_path)+'.mp3')


if (__name__ == '__main__'):
    if len(sys.argv)>0:
        warning_ok = input(warning_string)
        if (warning_ok.lower().startswith('y')):
            paths = sys.argv[1:]
            for a_path in paths:
                extract_audio(a_path)
        else:
            print('Warning condition is unacceptable. Exiting...')
    else:
        print('No paths specified. Exiting...')
    print('Done')


