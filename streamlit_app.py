import streamlit as st
from PIL import Image
from transformers import BlipForConditionalGeneration, BlipProcessor

# Page config
st.set_page_config(
    page_title="AI Image Captioning App", page_icon="🖼️", layout="centered"
)

st.title("🖼️ AI Image Captioning App")
st.write(
    "Upload an image and let the BLIP AI model generate a natural-language"
    " description for it!"
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


with st.spinner("Loading AI model... Please wait..."):
  processor, model = load_model()

# File uploader widget
uploaded_file = st.file_uploader(
    "Choose an image...", type=["jpg", "jpeg", "png", "webp"]
)

if uploaded_file is not None:
  image = Image.open(uploaded_file).convert("RGB")

  # Display the uploaded image
  st.image(image, caption="Uploaded Image", use_column_width=True)

  # Generate caption button
  if st.button("Generate Caption"):
    with st.spinner("Analyzing image..."):
      inputs = processor(image, return_tensors="pt")
      out = model.generate(**inputs)
      caption = processor.decode(out[0], skip_special_notes=True)

    st.success("### Caption:")
    st.write(f"*{caption}*")