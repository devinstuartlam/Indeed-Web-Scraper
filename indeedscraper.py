#Devin Lam MGS 314 B1
import requests
from bs4 import BeautifulSoup 

URL = 'https://www.indeed.com/jobs?q=python&l=new+york'
page = requests.get(URL).text
jobs_file = open('job.txt', 'w', encoding ='utf8')
soup = BeautifulSoup(page, 'html.parser')

with jobs_file as o:
    for jobs in soup.find_all('div', class_='jobsearch-SerpJobCard'):
        title = jobs.h2.a.text.strip()
        geturl = 'https://www.indeed.com' + jobs.h2.a.get('href')
        company = jobs.find('span', 'company').text.strip()
        location = jobs.find('div', 'recJobLoc').get('data-rc-loc')
        o.write('Job Title: ' + str(title) + '\n')
        o.write('Company: ' + str(company) + '\n')
        o.write('Location: ' + str(location) + '\n')
        o.write('URL: ' + str(geturl) + '\n')
        o.write('---------------------' + '\n')
        o.close

fileopen = open('job.txt', 'r', encoding = 'utf8')
print(fileopen.read())





