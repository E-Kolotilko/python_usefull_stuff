from PIL import Image, ExifTags
import sys
import os


def extract_metadata(path):
    with Image.open(path) as image:
        raw_data = image.getexif()
        decoded_data = {}
        for tag_id in raw_data:
            #second param of TAGS.get(tag_id, tag_id) is default value
            decoded_data[ExifTags.TAGS.get(tag_id, tag_id)] = raw_data.get(tag_id)
        return raw_data, decoded_data


if __name__ == '__main__':
    image_path = input('Enter image path\n') if len(sys.argv)<2 else sys.argv[1]
    while not os.path.exists(image_path):
        image_path = input('Entered image path does not exist. Retry\n')
    raw_data, decoded_data = extract_metadata(image_path)
    print(raw_data)
    print(decoded_data)
