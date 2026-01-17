# Hugging Face SDXL Image Generator

A simple Python script that generates AI images using **Stable Diffusion XL (SDXL)** via the **Hugging Face Inference API**.  
Prompts are read from a JSON file and generated images are saved locally.

---

## Requirements

- Python 3.9+
- Hugging Face API token

Install dependencies:
```bash
pip install -r requirements.txt
Environment Setup
Set your Hugging Face token as an environment variable:

Windows

set HF_TOKEN=your_token
Linux / macOS

export HF_TOKEN=your_token

Usage
python main.py
Generated images will be saved in the generated_images/ folder.

