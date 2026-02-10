import streamlit as st
from PIL import Image
from rembg import remove
import io

# Page config
st.set_page_config(page_title="AI Background Remover", layout="wide")

st.title("🚀 AI Background Remover")
st.write("Upload an image and remove the background instantly using AI!")

uploaded_file = st.file_uploader(
    "📤 Upload Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    try:
        img = Image.open(uploaded_file)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(img, use_container_width=True)

        if st.button("✨ Remove Background"):
            with st.spinner("AI is removing the background..."):

                output = remove(img)

                with col2:
                    st.subheader("Background Removed")
                    st.image(output, use_container_width=True)

                # Convert image for download
                buf = io.BytesIO()
                output.save(buf, format="PNG")
                byte_im = buf.getvalue()

                st.success("✅ Background Removed Successfully!")

                st.download_button(
                    label="⬇ Download Image",
                    data=byte_im,
                    file_name="background_removed.png",
                    mime="image/png"
                )

    except Exception as e:
        st.error("Error processing image 😢")
        st.write(e)
