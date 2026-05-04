import requests
import os

# On récupère le lien secret Discord
https://discord.com/api/webhooks/1500942289130754260/-9fp_jCsQ0yZAcuSEiyJgGG56s-TL1ZkQPhG2NvAe87oGPzOpIjzQJZl_Yqc554GEjzp = os.getenv('DISCORD_WEBHOOK')

def send_weather():
    # Coordonnées de Martigny
    url = "https://api.open-meteo.com/v1/forecast?latitude=46.10&longitude=7.07&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&current_weather=true&timezone=Europe/Berlin"
    data = requests.get(url).json()
    
    temp = data['current_weather']['temperature']
    max_t = data['daily']['temperature_2m_max'][0]
    min_t = data['daily']['temperature_2m_min'][0]

    payload = {
        "embeds": [{
            "title": "🏔️ Météo Martigny",
            "description": f"Il fait actuellement **{temp}°C**.\nPrévu aujourd'hui: **{min_t}°C** à **{max_t}°C**.",
            "color": 15418782 # Une couleur orange sympa
        }]
    }
    requests.post(WEBHOOK_URL, json=payload)

if __name__ == "__main__":
    send_weather()
