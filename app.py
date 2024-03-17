import json
from difflib import get_close_matches
from listen import listen_and_print
from say import main
# from urllib.parse import quote
import pywhatkit as kit
import webbrowser
# import urllib.parse
from social_medias import *



def load_knowledge_base(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"questions": []}

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

def chat_bot():
    knowledge_base = load_knowledge_base("knowledge_base.json")

    while True:
        user_input = input("You: ").lower()
        # listen_input = listen_and_print()
        # user_input = str(listen_input).lower()

        if user_input == "bye":
            # print("Bot: Bye, have a nice day!")
            bye = "Bye Buddy! have a nice day."
            print(f"Bot: {bye}")
            main(bye)
            break
        
        if "open my instagram" in user_input:
            webbrowser.open("https://instagram.com/heyy.mani1/")
            main("Opening your Instagram")
            continue
        
        if "channel" in user_input and ("youtube" in user_input or "yt" in user_input):
            try:
                sfyc = input("Enter the YouTube channel name: ").lower()
                yt_channel_search(sfyc)
                main(f"Opening YouTube and searching for {sfyc} channel...")
                continue
            except:
                error = "Network error occurred"
                print(error)
                main(error)
                continue
                # print("Network error occured")
        
        if "youtube" in user_input or "yt" in user_input:
            try:
                soy = input("what you want to play on youtube: ").lower()
                kit.playonyt(soy)
                main(f"playing {soy} on youtube...")
                continue
            except:
                error = "Network error occured"
                print(error)
                main(error)
                # print("Network error occured.")
                continue
            
        if "google" in user_input or "chrome" in user_input:
            try:
                sog = input("what you want me to search on google: ").lower()
                # url = f"https://www.google.com/search?q={urllib.parse.quote(sog)}"
                # webbrowser.open(url)
                google_search(sog)
                main(f"searching {sog} on google...")
                continue
            except:
                error = "Network error occured"
                print(error)
                main(error)
                # print("Network error occured.")
                continue
            
        if "instagram" in user_input or "insta" in user_input:
            try:
                sfia = input("Enter the username: ").lower()
                insta_acc_search(sfia)
                main(f"Opening Instagram and searching {sfia}")
                continue
            except:
                error = "Network error occured"
                print(error)
                main(error)
                continue
                # print("Network error occured")
                
                
        
            

                    
        
        
        best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
            # print(f"Bot: {answer}")
            print(f"Bot: {answer}")
            main(answer)
        
            
        else:
            # print("Bot: I don't know the answer. Can you teach me?")
            speech = "I don't know the answer. Can you please teach me?"
            print (f"Bot: {speech}")
            main(speech)
            new_answer = input('Type the answer or "skip" to skip: ').lower()

            if new_answer != "skip":
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base("knowledge_base.json", knowledge_base)
                # print("Bot: Thanks! I got it for the future.")
                speech1 = "Thanks! I got it for the future."
                print (f"Bot: {speech1}")
                main(speech1)
                

    

if __name__ == "__main__":
    chat_bot()

