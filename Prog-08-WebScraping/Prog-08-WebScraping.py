# 2110101 Computer Programming
 
# Prog-08: Web Scraping
# 6330085821 

import urllib
import urllib.request as urq


def load_html(page_url):
    return str(urq.urlopen(page_url).read().decode('utf-8'))
# -------------------------------------------------


def find(load, txt):
    return (i for i in range(len(load)) if load.startswith(txt, i))


def get_faculty_names(url):
    html = load_html(url)
    idx_list = find(html, 'Faculty of')
    faculty_list = []

    for idx in idx_list:
        i = idx
        faculty = ""
        while i < len(html) and html[i] != '<':
            faculty += html[i]
            i += 1
        faculty_list.append(faculty)

    return faculty_list


def save_image(img_url, file_name):
    urllib.request.urlretrieve(img_url, file_name)


def download_faculty_images(url):
    html = load_html(url)
    idx_list = find(html, '-300x188.jpg')
    img_list = []
    for idx in idx_list:
        i = idx-1
        img = ""
        while i >= 0 and html[i] != '/':
            img = html[i] + img
            i -= 1
        if img not in img_list:
            img_list.append(img)
    img_list = img_list[:len(img_list)-3]
    for img in img_list:
        # print("https://waiiinta.github.io/image/"+img+"-300x188.jpg")
        save_image("https://waiiinta.github.io/image/" +
                   img+"-300x188.jpg", img+".jpg")


def print_faculty_numbers(url):
    html = load_html(url)
    idx_list = find(html, '-chulalongkorn-university.html')
    faculty_list = []
    for idx in idx_list:
        i = idx-1
        faculty = ""
        while i >= 0 and html[i] != '/':
            faculty = html[i] + faculty
            i -= 1
        if faculty not in faculty_list:
            faculty_list.append(faculty)
    faculty_list = faculty_list[:len(faculty_list)-3]

    for faculty in faculty_list:
        html = load_html("https://waiiinta.github.io/" + faculty + "-chulalongkorn-university.html")
        idx_list = find(html, 'wpcf-field-wysiwyg wpcf-field-custom-content-contact-2')
        for idx in idx_list:
            i = idx 
            tel = ""
            while i < len(html):
                if html[i:i+3] == '+66':
                    break
                i += 1
            i += 3
            while i < len(html):
                if html[i] == '(':
                    i += 2
                if html[i].isdigit():
                    tel += html[i]
                if len(tel) == 8:
                    break
                i += 1

            print(faculty)
            print("0",tel[:4],tel[4:])
            print()

# -------------------------------------------------

def main():
    pageurl = "https://waiiinta.github.io/"

    print(get_faculty_names(pageurl))

    download_faculty_images(pageurl)

    print_faculty_numbers(pageurl)


# -------------------------------------------------
main()