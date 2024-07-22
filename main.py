import requests
import webbrowser


def getRandomWikiPage():
    response = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    return response.url


def taskHadlerProcessor():
    while True:
        user_input = input("Хотите получить случайную статью в Википедии? (да/нет): ").strip().lower()
        if user_input in ['да', 'yes', 'y']:
            url = getRandomWikiPage()
            print(f"Ссылка на случайную статью: {url}")
            open_page = input("Хотите открыть эту статью в браузере? (да/нет): ").strip().lower()
            if open_page in ['да', 'yes', 'y']:
                webbrowser.open(url)
        elif user_input in ['нет', 'no', 'n']:
            print("Выход из программы.")
            break
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")


if __name__ == "__main__":
    taskHadlerProcessor()
