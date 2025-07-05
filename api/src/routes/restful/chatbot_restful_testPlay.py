import requests  # type: ignore

session_id = "test123"
base_url = "http://localhost:8000/endless/chatbot/chat"

response1 = requests.post(base_url, json={"session_id": session_id})
print("Bot:", response1.json()["response"])

game_choice = input("Jeu choisi : ")
response2 = requests.post(
    base_url, json={"session_id": session_id, "selected_game": game_choice}
)
print("Bot:", response2.json()["response"])

while True:
    user_message = input("Toi : ")
    response = requests.post(
        base_url, json={"session_id": session_id, "message": user_message}
    )
    print("Bot:", response.json()["response"])

    if user_message.strip().lower() == "/end":
        print("Fin de la session. Merci !")
        break
