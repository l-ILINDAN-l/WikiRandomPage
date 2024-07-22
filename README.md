# WikiRandomPage
Application provides a random link to a Wikipedia article. The program asks the user whether to display a random Wikipedia article and displays the page if the answer is positive.

Importing libraries:

requests: for executing HTTP requests.
webbrowser: to open links in the browser.

getRandomWikiPage() function:

Executes a GET request to a special Wikipedia page to get a random article.
Returns the URL of the received article.

The taskHadlerProcessor() function:

The endless loop asks the user if he wants to receive a random article.
If the answer is yes, it calls the getRandomWikiPage() function and outputs a link to the article.
Asks if the user wants to open the article in the browser, and opens it if the answer is yes.
If the user answers the initial question in the negative, the program shuts down.
