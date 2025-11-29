import wikipedia


def main():
    search_phrase = input('Page title: ')
    while search_phrase != "":
        page = wikipedia.page(search_phrase, auto_suggest=True)

        print(f"\nTitle: {page.title}")
        print(f"URL: {page.url}")
        print(page)

        search_phrase = input('Page title: ')


if __name__ == '__main__':
    main()
