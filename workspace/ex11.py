import requests


def main():
    search_term = input('Enter movie name: ')
    apikey='aa9e49f'
    url = f'https://omdbapi.com?apikey={apikey}&s={search_term}'

    r = requests.get(url)

    if r.status_code != 200:
        print(r.text)
        exit(r.status_code)

    data = r.json()
    movies = data['Search']
    for each_movie in movies:
        print(each_movie['Title'])


if __name__ == '__main__':
    main()
