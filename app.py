import requests
from bs4 import BeautifulSoup
import sys
from textblob import TextBlob

# Getting HTML
url = 'https://www.rte.ie/news/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Getting Data
data = soup.findAll('div', attrs={'class': 'top-story-wrapper'})

for item in data:
    hline = item.find('span', attrs={'class': 'underline'}).text

    cat = item.find(
        'span', attrs={'class': 'category-name primary-color'}).text

    sum = item.find('p', attrs={'class': 'leadin'}).text

    link = item.find(
        'a', attrs={'class': 'image-link img-container'}, href=True)


print('Here is todays top news story')
print('')
print('Headline: ')
print(hline)
print('Category: ')
print(cat)
print('Summary: ')
print(sum)
print('')
user = str(input('Would you like more information on this article? (y/n) '))

if user == "y":
    new_link = url+link['href']

    response = requests.get(new_link)
    soup = BeautifulSoup(response.text, 'html.parser')

    new_data = soup.findAll('section', attrs={
        'class': 'medium-10 medium-offset-1 columns article-body has_embedded_images'})
    for i in new_data:
        content = i.find_all('p')
        contentlist = []
        for a in content:
            contentlist.append(a.text)

    print(*contentlist)
    print('')
    print('')
    content_string = ''.join(contentlist)
    nature = TextBlob(content_string)
    polarity = nature.polarity
    if (polarity == 0.00):
        print(
            f'This article was mostly neutral, with a polarity of {polarity}')

    elif(polarity > 0.00):
        print(
            f'This article was mostly positive, with a polarity of {polarity}')

    elif(polarity < 0.00):
        print(
            f'This article was mostly negative, with a polarity of {polarity}')


elif user == "n":
    print('Goodbye')
    sys.exit()

else:
    print('Invalid Input')
