import pandas as pd
import spacy
import os
import re
import PyPDF2
import os
import docx2txt
dir = 'FOLDER with BULK CVs Path'


f_names = []
l_names = []
emails = []
linkedin_urls = []
paths= []

def extract_text_from_doc(file_path):
    try:
        text_content = docx2txt.process(file_path)
        return text_content
    except Exception as e:
        return ''

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        extracted_text = ""

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            extracted_text += page.extract_text()

    return extracted_text


def split_full_name(full_name):
    names = full_name.split(" ")

    first_name = names[0]
    last_name = names[1]
    return first_name, last_name


nlp = spacy.load('en_core_web_trf')


def extract_information(text,path):
    doc = nlp(text)
    # TEST TEST
    doc2 = nlp(path)
    for ent in doc2.ents:
        if ent.label_ == 'PERSON':
            
            print(f'NAME in path : {ent.text}')
    # TEST TEST
    # Extract named entities
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            name = ent.text
            break

    try:
        f_name, l_name = split_full_name(name)
        return f_name, l_name
    except Exception as e:
        return '', ''


def extract_information_re(text):
    # Extract first name and last name using regex patterns
    email = re.search(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)
    linkedin_url = re.search(
       r"(?i)\blinkedin\.com/[^ .,;\n()<>]+(?:\([\w\d]+\))?/?[^ .,;\n()<>]+", text)

    # Extract captured groups from regex matches
    email = email.group() if email else ""
    linkedin_url = linkedin_url.group() if linkedin_url else ""
    linkedin_url = linkedin_url.replace("\n", "")

    return email, linkedin_url


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
    


def loop_over_cvs_pdf(dir):
    pdf_paths = []
    for filename in os.listdir(dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(dir, filename)
            pdf_paths.append(pdf_path)
    return pdf_paths

def loop_over_cvs_doc(dir):
    doc_paths = []
    for filename in os.listdir(dir):
        if ".doc" in filename:
            doc_path = os.path.join(dir, filename)
            doc_paths.append(doc_path)
    return doc_paths

pdf_paths = loop_over_cvs_pdf(dir)
for pdf_path in pdf_paths:
    f_name, l_name = extract_information(extract_text_from_pdf(pdf_path),pdf_path)
    email, linkedin_url = extract_information_re(
        extract_text_from_pdf(pdf_path).lower())
    print(f' F : {f_name}, L : {l_name}, E: {email}, Li: {linkedin_url}, P: {pdf_path}')
    f_names.append(f_name)
    l_names.append(l_name)
    emails.append(email)
    paths.append(pdf_path)
    linkedin_urls.append(linkedin_url)
    save(f_names, l_names, emails, linkedin_urls,paths)

doc_paths = loop_over_cvs_doc(dir)
for doc_path in doc_paths:
    f_name, l_name = extract_information(extract_text_from_doc(doc_path),doc_path)
    email, linkedin_url = extract_information_re(
        extract_text_from_doc(doc_path).lower())
    print(f' F : {f_name}, L : {l_name}, E: {email}, Li: {linkedin_url}, P: {doc_path}')
    f_names.append(f_name)
    l_names.append(l_name)
    emails.append(email)
    paths.append(doc_path)
    linkedin_urls.append(linkedin_url)
    save(f_names, l_names, emails, linkedin_urls,paths)



