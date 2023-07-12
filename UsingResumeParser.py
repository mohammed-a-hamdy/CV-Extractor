

from pyresparser import ResumeParser
import os
import pandas as pd
import re

f_names = []
l_names = []
emails = []
linkedin_urls = []
paths= []
dir = 'Finance_Managers_CV_1month_Active_MCF'

def split_full_name(full_name):
    names = full_name.split(" ")

    first_name = names[0]
    last_name = names[1]
    return first_name, last_name

def save(f_name, l_name, email, linkedin_url,paths):
    data_item = {'First name': f_name,
                 'Last name': l_name,
                 'Email': email,
                 'LinkedIn Link': linkedin_url,
                 'Paths': paths,
                 }

    dataframe = pd.DataFrame(data_item)

    df = pd.DataFrame(dataframe)
    df.to_excel('CVs.xlsx', index=False)
    

def loop_over_cvs(dir):
    doc_paths = []
    for filename in os.listdir(dir):
        doc_path = os.path.join(dir, filename)
        doc_paths.append(doc_path)
    return doc_paths

doc_paths = loop_over_cvs(dir)
for doc_path in doc_paths:

    data = ResumeParser(doc_path).get_extracted_data()
    print(f" Name : {data['name']}, Email : {data['email']}")
    try:
        f_name ,l_name =split_full_name(data['name'])
    except Exception as e:
        f_name = ''
        l_name = ''
    f_names.append(f_name)
    l_names.append(l_name)
    emails.append(data['email'])
    paths.append(doc_path)
    linkedin_urls.append('linkedin_url')
    save(f_names, l_names, emails, linkedin_urls,paths)
