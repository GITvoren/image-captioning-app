# AI-Powered Web Image & Alt-Text Generator

A multimodal AI web application that automates image captioning and **SEO / accessibility alt-text generation** using Salesforce's **BLIP (Bootstrapping Language-Image Pre-training)** vision-language model, **BeautifulSoup**, and **Streamlit**.

Built to help content teams, web developers, and SEO specialists automatically extract images from live webpages and generate descriptive alt-text—or analyze individual images on demand.

Originally prototyped with Gradio and migrated to Streamlit for cloud deployment.

🔗 **Live Demo:** <a href="https://image-captioning-app-mtigqkzntld7ypmuz9appjf.streamlit.app/" target="_blank">Launch AI App</a>

## Features

* **Automated Webpage Image Scraper & Alt-Text Generator:** Enter any public URL to automatically extract `<img>` assets, filter out tiny icons/SVGs, generate SEO- and accessibility-friendly alt-text descriptions in batch, and export all results as a downloadable `captions.txt` file.
* **Single Image Captioner:** Upload individual images (JPG, PNG, WebP) for instant natural-language descriptions.
* **Optimized Model Caching:** Uses `@st.cache_resource` to load the BLIP model into memory once for fast inference across repeated runs.
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