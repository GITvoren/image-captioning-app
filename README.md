# AI Image Captioning App

A web-based multimodal AI application that generates natural-language captions for uploaded images using Salesforce's **BLIP (Bootstrapping Language-Image Pre-training)** vision-language model and **Streamlit**.

Originally prototyped with Gradio and migrated to Streamlit for cloud deployment.

🔗 **Live Demo:** <a href="https://image-captioning-app-mtigqkzntld7ypmuz9appjf.streamlit.app/" target="_blank">Launch AI App</a>

## Features

* **Instant Image-to-Text Generation:** Upload any image (JPG, PNG, WebP) and get an accurate, human-readable description in seconds.
* **Interactive Web Interface:** Built with Streamlit for clean drag-and-drop image uploads, previews, and output rendering.
* **Optimized Model Caching:** Uses `@st.cache_resource` to load the BLIP model into memory once for fast subsequent predictions.
* **Continuous Deployment:** Automatically deploys updates pushed to the `main` branch via Streamlit Community Cloud.

## Tech Stack

* **Language:** Python
* **AI / ML Frameworks:** PyTorch, Hugging Face `transformers`
* **Pre-trained Model:** [`Salesforce/blip-image-captioning-base`](https://huggingface.co/Salesforce/blip-image-captioning-base)
* **Frontend / UI:** Streamlit
* **Image Processing:** Pillow (PIL), NumPy
- **Hosting & CI/CD:** Streamlit Community Cloud (Native GitHub Auto-Deploy)

## Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GITvoren/image-captioning-app
   cd image-captioning-app
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS / Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the application:**
   ```bash
   streamlit run streamlit_app.py
   ```
   Open your browser and navigate to `http://localhost:8501`.

## 📁 Project Structure

```text
├── streamlit_app.py        # Main Streamlit application & BLIP inference logic
├── image_captioning_app.py # Legacy Gradio interface (optional)
├── requirements.txt        # Pinned Python dependencies
├── .gitignore              # Excludes venv, cache, and local environment files
└── README.md               # Project documentation
```

---

### 👨‍💻 Author & Course Context
Built by **Voren** ([GitHub](https://github.com/GITvoren) • [Portfolio](https://vorentejuco.pages.dev))

> **Part of the IBM AI Developer Professional Certificate**  
> Developed as a practical, hands-on capstone/lab project applying modern AI engineering, LLM integration, and full-stack deployment principles.