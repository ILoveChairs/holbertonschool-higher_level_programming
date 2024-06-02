#!/usr/bin/python3

'''
    quickdoc
'''

import requests
import csv


def fetch_and_print_posts():
    '''
        quickdoc
    '''

    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(r.status_code)
    dic = r.json()
    for sub_dic in dic:
        print(sub_dic['title'])
        print(sub_dic['body'])


def fetch_and_save_posts():
    '''
        quickdoc
    '''

    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if int(r.status_code / 100) == 2:
        dic = r.json()
        with open("posts.csv", "w+") as f:
            dwriter = csv.DictWriter(f, ['title', 'body'])
            dwriter.writeheader()
            for sub_dic in dic:
                dwriter.writerow({'title': sub_dic['title'], 'body': sub_dic['body']})
