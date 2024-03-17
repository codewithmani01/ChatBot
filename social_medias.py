import webbrowser
import urllib.parse
from urllib.parse import quote


# Google Search 

def google_search(query):
    search_url = f"https://www.google.com/search?q={quote(query)}"
    webbrowser.open(search_url)
    print(f"Google search for '{query}' initiated.")
    
    
# Instagram Account Search 


def insta_acc_search(username):
    search_url = f"https://www.instagram.com/{username}/"
    webbrowser.open(search_url)
    print(f"Opening Instagram and searching for {username}")
    
    
# Search for youtube channels 

def yt_channel_search(username):
    search_url = f"https://www.youtube.com/@{username}"
    webbrowser.open(search_url)
    print(f"Opening Youtube Channel {username}")
    
    
def youtube_search(query):
    search_url = f"https://www.youtube.com/search?q={quote(query)}"
    webbrowser.open(search_url)
    print(f"Youtube search for '{query}' initiated.")