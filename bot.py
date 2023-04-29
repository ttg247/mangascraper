import requests
import bs4
import os

def scrape_manga_titles(url):
    # Make a request to the manga website.
    response = requests.get(url)

    # Parse the HTML response.
    soup = bs4.BeautifulSoup(response.content, 'html.parser')

    # Find all the manga titles.
    manga_titles = soup.find_all('a', class_='manga-title')

    # Return a list of the manga titles.
    return [manga_title.text for manga_title in manga_titles]

def download_manga_chapters(manga_title, url):
    # Make a request to the manga chapter website.
    response = requests.get(url)

    # Parse the HTML response.
    soup = bs4.BeautifulSoup(response.content, 'html.parser')

    # Find the manga chapter image.
    image = soup.find('img', class_='manga-chapter-image')

    # Download the manga chapter image.
    with open(manga_title + '.jpg', 'wb') as f:
        f.write(image.get('src'))

def main():
    # Get the manga website URL.
    url = 'https://www.mangadex.org/'

    # Get the list of manga titles.
    manga_titles = scrape_manga_titles(url)

    # Download all the manga chapters for the manga titles.
    for manga_title in manga_titles:
        download_manga_chapters(manga_title, url + manga_title)

if __name__ == '__main__':
    main()
