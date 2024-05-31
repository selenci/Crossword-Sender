# Crossword Sender
A simple program that downloads the Universal Crossword, uploads it to downforacross.com, and shares the link to a Discord chat group.

Selenium currently uses Chrome browser, make sure to change the downloaded drivers in [getter.py](getter.py) for other browsers.

# Setup

Before running the program, follow these setup instructions:

1. Install requirements using the command `pip install -r requirements.txt`.
2. Create a file named `crossword_secrets.py`.
3. Inside `crossword_secrets.py`, define the following parameters:

    - `CHAT_ID`: The ID of your Discord message channel. This can be found in the URL when having the channel open in the browser app.
    
    - `TOKEN`: Your Discord user account token. You can find instructions on how to obtain your Discord token [here](https://www.androidauthority.com/get-discord-token-3149920/).
    
    - `GROUP_NAME`: An arbitrary string with characters allowed inside the URL. This name will be included in the URLs of the generated links to indicate your ownership.
