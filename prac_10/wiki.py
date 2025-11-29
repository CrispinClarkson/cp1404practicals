import wikipedia


def main():
    """Wikipedia search program:"""
    search_phrase = input('Enter page title: ')
    while search_phrase != "":
        try:
            page = wikipedia.page(search_phrase, auto_suggest=False)

            print(f"{page.title}")
            print(f"{page.summary}")
            print(f'{page.url}')

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{search_phrase}" does not match any pages. Try another id!')

        print()
        search_phrase = input('Enter page title: ')
    print("Thank you.")


if __name__ == '__main__':
    main()
