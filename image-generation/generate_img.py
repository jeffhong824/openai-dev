import os
import base64

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv("OPENAI_KEY")

client = OpenAI(api_key=api_key)

prompt = """
A children's book drawing of a veterinarian using a stethoscope to 
listen to the heartbeat of a baby otter.
"""

result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

os.makedirs("output", exist_ok=True)

# Save the image to a file
with open("output/otter.png", "wb") as f:
    f.write(image_bytes)