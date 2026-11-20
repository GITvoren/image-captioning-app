from io import BytesIO
from bs4 import BeautifulSoup
from PIL import Image
import requests
import streamlit as st
from transformers import BlipForConditionalGeneration, BlipProcessor

# Page config
st.set_page_config(
    page_title="AI Image Captioning Suite", page_icon="🖼️", layout="wide"
)

st.title("AI-Powered Web Image & Alt-Text Generator")
st.write(
    "Powered by Salesforce BLIP — choose between single image analysis or"
    " automated batch-scraping for web content."
)


# Load model and processor with caching so it only loads once
@st.cache_resource
def load_model():
  processor = BlipProcessor.from_pretrained(
      "Salesforce/blip-image-captioning-base"
  )
  model = BlipForConditionalGeneration.from_pretrained(
      "Salesforce/blip-image-captioning-base"
  )
  return processor, model


with st.spinner("Loading AI model into memory... Please wait..."):
  processor, model = load_model()

# Create tabs for dual modes
tab2, tab1 = st.tabs(["🌐 Batch URL Scraper", "🖼️ Single Image Uploader"])

# --- TAB 1: Single Image Uploader ---
with tab1:
  st.subheader("Upload a Single Image")
  st.write("Upload an image to instantly generate a descriptive caption.")

  uploaded_file = st.file_uploader(
      "Choose an image...", type=["jpg", "jpeg", "png", "webp"]
  )

  if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Caption"):
      with st.spinner("Analyzing image..."):
        inputs = processor(image, return_tensors="pt")
        out = model.generate(**inputs, max_new_tokens=50)
        caption = (
            processor.decode(out[0], skip_special_tokens=True)
            .replace("[SEP]", "")
            .strip()
        )

      st.success("### Generated Caption:")
      st.write(f"*{caption}*")

# --- TAB 2: Batch URL Scraper ---
with tab2:
  st.subheader("Automate Webpage Image Captioning")
  st.write(
      "Enter a public article or webpage URL to automatically scrape images,"
      " generate alt-text captions, and compile them for SEO/accessibility."
  )

  url_input = st.text_input(
      "Webpage URL", "https://en.wikipedia.org/wiki/IBM"
  )

  # Add a slider to let the user control how many images to scrape
  max_images = st.slider(
      "Max images to scrape", min_value=1, max_value=20, value=10
  )

  if st.button("Scrape & Caption Images"):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
      with st.spinner(f"Fetching content from {url_input}..."):
        response = requests.get(url_input, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        img_elements = soup.find_all("img")

      st.info(
          f"Found {len(img_elements)} total `<img>` tags. Processing up to"
          f" {max_images} valid images..."
      )

      captions_output = []
      progress_bar = st.progress(0)
      valid_images_count = 0

      for idx, img_element in enumerate(img_elements):
        # Stop scraping immediately if we hit the user's limit
        if valid_images_count >= max_images:
          break

        # Extract and clean URL
        img_url = img_element.get("src") or img_element.get("data-src")
        if not img_url and img_element.has_attr("srcset"):
          img_url = img_element["srcset"].split()[0]
        if not img_url or ".svg" in img_url:
          continue

        if img_url.startswith("//"):
          img_url = "https:" + img_url
        elif img_url.startswith("/"):
          from urllib.parse import urlparse

          parsed_url = urlparse(url_input)
          img_url = f"{parsed_url.scheme}://{parsed_url.netloc}{img_url}"
        elif not img_url.startswith("http"):
          continue

        try:
          r = requests.get(img_url, timeout=5, headers=headers)
          raw_image = Image.open(BytesIO(r.content))

          if raw_image.size[0] * raw_image.size[1] < 400:
            continue  # Skip tiny icons/logos

          raw_image = raw_image.convert("RGB")
          inputs = processor(
              images=raw_image, text="the image of", return_tensors="pt"
          )
          out = model.generate(**inputs, max_new_tokens=40)
          caption = (
              processor.decode(out[0], skip_special_tokens=True)
              .replace("[SEP]", "")
              .strip()
          )

          captions_output.append(f"{img_url} -> {caption}")
          valid_images_count += 1

          # Display every successfully processed image since the max is small (e.g. 10)
          col1, col2 = st.columns([1, 2])
          with col1:
            st.image(raw_image, width=120)
          with col2:
            st.write(f"**Image:** `{img_url}`")
            st.write(f"**Caption:** *{caption}*")
          st.divider()

        except Exception:
          continue

        # Update progress bar safely based on total checked elements
        progress_bar.progress(min((idx + 1) / len(img_elements), 1.0))

      if captions_output:
        st.success(
            f"Successfully captioned {len(captions_output)} images from the"
            " webpage!"
        )
        result_text = "\n".join(captions_output)
        st.download_button(
            label="📥 Download captions.txt",
            data=result_text,
            file_name="captions.txt",
            mime="text/plain",
        )
      else:
        st.warning(
            "No valid processable images found on that page. Try a different"
            " URL!"
        )

    except Exception as e:
      st.error(f"Error accessing webpage: {e}")