import requests
import bs4

job_title = []
company_name = []
location = []
skills = []

result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")
source = result.content

soup = bs4.BeautifulSoup(source, "html.parser")
# job titels , job skills , company names , location name .
job_titels = soup.find_all("h2", { "class":"css-m604qf" })
company_names = soup.find_all("a",{"class":"css-17s97q8"})
location_name = soup.find_all("span",{"class":"css-5wys0k"})
job_skills = soup.find_all("div",{"class":"css-y4udm8"})

# for loop to extract data

for i in range(len(job_titels)):
    job_title.append(job_titels[i].text)
print(job_title)

for i in range(len(company_names)):
    company_name.append(company_names[i].text)
print(company_name)

for i in range(len(location_name)):
    location.append(location_name[i].text)
print(location)

for i in range(len(job_skills)):
    skills.append(job_skills[i].text)
print(skills)

