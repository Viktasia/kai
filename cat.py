import requests
from PIL import Image
from io import BytesIO
import webbrowser

API_KEY = "live_9vqMb2R9YkdEyYPjkLNKFObRo1RbBoMMgMh02U9otygKYi7mjrzxKWLNGOalBjrg"

def get_cat_with_breed():
    url = "https://api.thecatapi.com/v1/images/search?has_breeds=1"
    headers = {"x-api-key": API_KEY}

    for _ in range(10):  # до 10 спроб
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()[0]

            image_url = data.get("url", "")
            breeds = data.get("breeds", [])
            breed_name = breeds[0]["name"] if breeds else "Невідома порода"

            if breed_name != "Невідома порода":
                return image_url, breed_name
            else:
                print("⚠️ Кіт без породи, спробуємо ще раз...")
        except Exception as e:
            print(f"⚠️ Помилка: {e}")

    return None, None

def main():
    image_url, breed = get_cat_with_breed()

    if image_url:
        print("🎉 Випадкове зображення кота:")
        print("📷 URL зображення:", image_url)
        print("🐾 Порода кота:", breed)

        # Відкрити зображення у браузері
        webbrowser.open(image_url)
    else:
        print("❌ Не вдалося знайти кота з породою 🐾")

if __name__ == "__main__":
    main()
