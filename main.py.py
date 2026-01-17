import json
import os
import requests
import time
from PIL import Image
from io import BytesIO


HF_TOKEN = os.environ.get("HF_TOKEN")

if not HF_TOKEN:
    raise RuntimeError("HF_TOKEN not found. Set environment variable first.")


HF_API_URL = ""
HF_TOKEN = os.environ.get("HF_TOKEN")

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def generate_images():
    with open("prompts.json", "r", encoding="utf-8") as f:
        prompts = json.load(f)

    os.makedirs("generated_images", exist_ok=True)

    for i, prompt in enumerate(prompts, 1):
        print(f"🎨 Generating {i}/{len(prompts)}")

        try:
            response = requests.post(
                HF_API_URL,
                headers=headers,
                json={"inputs": prompt},
                timeout=300
            )

            if response.status_code != 200:
                print(f"❌ Error {response.status_code}: {response.text}")
                time.sleep(10)
                continue

            image = Image.open(BytesIO(response.content))
            filename = f"generated_images/image_{i:03d}.png"
            image.save(filename)

            print(f"✅ Saved {filename}")
            time.sleep(10)  # avoid rate limit

        except Exception as e:
            print("❌ Exception:", e)
            time.sleep(15)

if __name__ == "__main__":
    generate_images()
