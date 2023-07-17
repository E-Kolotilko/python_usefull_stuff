import easyocr
from easyocr import config as ocr_config
import sys
import os

WARNING_BORDER = 0.75


def text_recognition(file_path : str, langs = ['en', 'ru']) -> list:
    """return list of ([[x,y],[x,y],[x,y],[x,y]], text_str, probability) based on image"""
    reader = easyocr.Reader(langs)
    #paragraph = True -> ([[x,y],[x,y],[x,y],[x,y]], paragraph_text)
    #yep, huge chunk and no probabilities.... Can be usefull if you go for captcha or something short
    result = reader.readtext(file_path)
    return result


def get_file_path():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    if not path or not os.path.exists(path): 
        manually = input('Path not provided or not found. Want to provide it manually? (y/n)\n')
        if manually.lower().startswith('y'):
            path = input('Path for image:\n')
            while not os.path.exists(path):
                path = input(f"Can't find path{path}. Enter path to image:\n")
            return path
        else:
            return None
    return path


def get_languages():
    """Return list of selected languages based on sys.argv or else on user choice"""
    #langs = sys.argv[2:] if len(sys.argv) > 2 else ocr_config.all_lang_list
    #Note: yep, it can't use its' own list : some languages are not found
    langs = sys.argv[2:] if len(sys.argv) > 2 else None
    while not langs:
        langs = input(f'Languages not found. Provide at least one. Available*: {ocr_config.all_lang_list} \n').split()
    langs = [x for x in langs if x in ocr_config.all_lang_list]
    if (not langs):
        print('Available languages not selected. Breaking routine...')
        return []
    return langs


def write_raw_result(write_path, ocr_raw_result, with_warnings = True):
    """Write to a file all text from raw ocr result in one line, no new lines"""
    with open(write_path, 'w') as result_file:
        for item in ocr_raw_result:
            result_file.write(item[1])
            result_file.write(' ')
            if (with_warnings and len(item) > 1 and item[2] <= WARNING_BORDER):
                print('Warning border triggered for item:')
                print(item)


def get_lines_based_on_coords(ocr_result : str, warnings_on = False) -> list:
    """Return list of lines based on coordinates of recognized text
    
    Expects list of ([[x,y],[x,y],[x,y],[x,y]], text_str, probability) to go through
    and try to make lines based on coordinates of recognized text. 
    """
    #([[238, 248], [320, 248], [320, 276], [238, 276]], 'Альфа" ', 0.3207814442789472)
    if not ocr_result or len(ocr_result) == 0:
        return []
    x_now = ocr_result[0][0][0][0]
    #Note: if you would decide to work through y, then height_coef has to be around 0.5
    resulting_lines = []
    a_line = []
    for item in ocr_result:
        if warnings_on and item[2] <= WARNING_BORDER:
            print('Warning border triggered for item:')
            print(item)
        if item[0][0][0] < x_now:
            resulting_lines.append(' '.join(a_line))
            a_line = []
        x_now = item[0][0][0]
        a_line.append(item[1])
    #last line will not be added -> add manually
    if a_line:
        resulting_lines.append(' '.join(a_line))
    return resulting_lines


def write_lined_result(write_path, ocr_raw_result, with_warnings = False):
    lines_to_write = get_lines_based_on_coords(ocr_raw_result, with_warnings)
    if not lines_to_write:
        print('No lines to write to file...')
        return
    with open(write_path, 'w') as result_file:
        for i, val in enumerate(lines_to_write):
            result_file.write(str(i)+' ')
            result_file.write(val)
            result_file.write('\n')


def main_routine():
    path = get_file_path()
    if not path:
        return
    langs = get_languages()
    if not langs:
        return
    result = text_recognition(path, langs)
    #write_raw_result(path+'_res.txt', result)
    write_lined_result(path+'_res.txt', result)


if __name__=='__main__':
    #python3 script_name.py file_path lang1 lang2 ... langN
    #result will be written to <file_path>_res.txt
    main_routine()
    print('Done')
