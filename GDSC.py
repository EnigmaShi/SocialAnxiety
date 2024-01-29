import wikipediaapi
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def content(page):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    headers = {'User-Agent': user_agent}
    url = f'https://en.wikipedia.org/wiki/{page}'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        return None

def wordcloudy(data):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(data)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

page = 'Blockchain'
wiki_content = content(page)

if wiki_content:
    processed_text = wiki_content.replace('\n', ' ').replace('[', '').replace(']', '')
    wordcloudy(processed_text)
else:
    print(f"The Wikipedia page '{page}' does not exist.")