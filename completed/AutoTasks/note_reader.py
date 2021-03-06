import os
import re

# Path is defined below (L56)


def find_tex_files(path, subject):

    note_dirs = os.listdir(path + subject)
    all_files = [os.listdir(path + subject + i) for i in note_dirs]

    flat_all_files = []

    for sublist in all_files:
        for item in sublist:
            flat_all_files.append(item)

    tex_files = []

    for i in flat_all_files:
        if '.tex' in i:
            tex_files.append(i)

    return tex_files


def clean_date(date):
    # Anno-mese-giorno
    months_dict = {
        "Gennaio":   "01",
        "Febbraio":  "02",
        "Marzo":     "03",
        "Aprile":    "04",
        "Maggio":    "05",
        "Giugno":    "06",
        "Luglio":    "07",
        "Agosto":    "08",
        "Settembre": "09",
        "Ottobre":   "10",
        "Novembre":  "11",
        "Dicembre":  "12"
    }

    date_split = date.split(' ')
    year = date_split[2]
    month = months_dict[date_split[1]]
    day = date_split[0]
    if len(day) == 1:
        day = '0' + day

    new_date = year + '-' + month + '-' + day

    return new_date


def find_dates(subject):
    path = '/home/ginko/Documents/Note/'
    files = find_tex_files(path, subject)
    pattern = re.compile('(?<=date{).+(?=})')
    date_list = []
    for tex in files:
        tex_path = path + subject + tex[:-4] + '/' + tex

        with open(tex_path, 'r') as f:
            for line in f:
                m = re.search(pattern, line)

                if m:
                    date_ = m.group(0)
                    cleaned_date = clean_date(date_)
                    date_list.append(cleaned_date)

    return date_list
