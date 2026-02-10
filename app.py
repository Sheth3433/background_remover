import streamlit as st
from PIL import Image
from rembg import remove
import io

# Page config
st.set_page_config(
    page_title="AI Background Remover - Professional Tool",
    page_icon="✂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    /* Main container styling */
    .main {
        padding: 2rem;
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .header-title {
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .header-subtitle {
        font-size: 1.3rem;
        opacity: 0.95;
        margin-bottom: 1rem;
    }
    
    /* Feature cards */
    .feature-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .feature-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    
    .feature-title {
        font-weight: 600;
        color: #333;
        margin-bottom: 0.5rem;
    }
    
    /* Image container */
    .image-container {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        background: white;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Button styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 600;
        font-size: 1.1rem;
        padding: 0.75rem 2rem;
        border-radius: 8px;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Download button */
    .stDownloadButton>button {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        font-weight: 600;
        width: 100%;
        padding: 0.75rem 2rem;
        border-radius: 8px;
        border: none;
    }
    
    .stDownloadButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(17, 153, 142, 0.4);
    }
    
    /* File uploader */
    .uploadedFile {
        border: 2px dashed #667eea;
        border-radius: 10px;
        padding: 2rem;
    }
    
    /* Success/Error messages */
    .stSuccess, .stError {
        border-radius: 8px;
        padding: 1rem;
    }
    
    /* Stats container */
    .stats-container {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 2rem 0;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
    }
    
    .stat-label {
        font-size: 1rem;
        opacity: 0.9;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        margin-top: 3rem;
        border-top: 1px solid #e0e0e0;
        color: #666;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header-container">
        <div class="header-title">✂️ AI Background Remover</div>
        <div class="header-subtitle">Remove image backgrounds instantly with cutting-edge AI technology</div>
        <p style="font-size: 1rem; opacity: 0.9;">Fast • Accurate • Free • No Sign-up Required</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://raw.githubusercontent.com/streamlit/streamlit/develop/examples/data/cat.jpg", 
             caption="Before & After Example", use_container_width=True)
    
    st.markdown("### 🎯 Features")
    st.markdown("""
    - ✨ **AI-Powered** removal
    - 🚀 **Instant** processing
    - 📱 **Mobile** friendly
    - 💾 **High-quality** output
    - 🔒 **Privacy** focused
    - 🆓 **Completely** free
    """)
    
    st.markdown("### 📖 How to Use")
    st.markdown("""
    1. Upload your image (PNG, JPG, JPEG)
    2. Click "Remove Background"
    3. Preview the result
    4. Download your image
    """)
    
    st.markdown("### 💡 Tips")
    st.markdown("""
    - Use **high-quality** images for best results
    - Works great with **portraits** and **products**
    - Transparent background in PNG format
    - Perfect for **e-commerce** listings
    """)
    
    st.markdown("---")
    st.markdown("### 🔧 Supported Formats")
    st.markdown("**Input:** PNG, JPG, JPEG")
    st.markdown("**Output:** PNG (transparent)")

# Main content
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("### 📤 Upload Your Image")
    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=["png", "jpg", "jpeg"],
        help="Supported formats: PNG, JPG, JPEG (Max size: 200MB)"
    )

if uploaded_file is not None:
    try:
        # Load image
        img = Image.open(uploaded_file)
        
        # Display image info
        st.markdown("---")
        info_col1, info_col2, info_col3, info_col4 = st.columns(4)
        with info_col1:
            st.metric("📐 Width", f"{img.width}px")
        with info_col2:
            st.metric("📏 Height", f"{img.height}px")
        with info_col3:
            st.metric("🎨 Mode", img.mode)
        with info_col4:
            file_size = len(uploaded_file.getvalue()) / 1024
            st.metric("💾 Size", f"{file_size:.1f} KB")
        
        st.markdown("---")
        
        # Image comparison
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="image-container">', unsafe_allow_html=True)
            st.markdown("#### 📷 Original Image")
            st.image(img, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Process button
        st.markdown("<br>", unsafe_allow_html=True)
        
        center_col1, center_col2, center_col3 = st.columns([1, 2, 1])
        with center_col2:
            process_button = st.button("✨ Remove Background", type="primary", use_container_width=True)
        
        if process_button:
            with st.spinner("🤖 AI is working its magic... Please wait"):
                # Remove background
                output = remove(img)
                
                with col2:
                    st.markdown('<div class="image-container">', unsafe_allow_html=True)
                    st.markdown("#### 🎨 Background Removed")
                    st.image(output, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                
                # Convert image for download
                buf = io.BytesIO()
                output.save(buf, format="PNG")
                byte_im = buf.getvalue()
                
                # Success message and download
                st.success("✅ Background removed successfully! Your image is ready.", icon="✅")
                
                # Download button
                download_col1, download_col2, download_col3 = st.columns([1, 2, 1])
                with download_col2:
                    st.download_button(
                        label="⬇️ Download PNG Image",
                        data=byte_im,
                        file_name=f"removed_bg_{uploaded_file.name.split('.')[0]}.png",
                        mime="image/png",
                        use_container_width=True
                    )
                
                # Show output info
                st.info(f"💡 **Output Info:** PNG format with transparent background ({len(byte_im) / 1024:.1f} KB)", icon="ℹ️")
                
    except Exception as e:
        st.error(f"❌ Error processing image: {str(e)}", icon="🚫")
        st.info("💡 Try using a different image or check the file format.", icon="ℹ️")

else:
    # Show welcome content when no file is uploaded
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Feature showcase
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Precise AI Detection</div>
            <p>Advanced neural networks detect and separate subjects with pixel-perfect accuracy</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Lightning Fast</div>
            <p>Process images in seconds with our optimized AI algorithms</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔒</div>
            <div class="feature-title">100% Private</div>
            <p>Your images are processed locally and never stored on our servers</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Use cases
    st.markdown("### 🎯 Perfect For")
    
    use_case_col1, use_case_col2, use_case_col3, use_case_col4 = st.columns(4)
    
    with use_case_col1:
        st.markdown("**🛍️ E-commerce**")
        st.write("Product photos for online stores")
    
    with use_case_col2:
        st.markdown("**👤 Portraits**")
        st.write("Professional headshots and profile pictures")
    
    with use_case_col3:
        st.markdown("**🎨 Design**")
        st.write("Graphic design and creative projects")
    
    with use_case_col4:
        st.markdown("**📱 Social Media**")
        st.write("Eye-catching posts and stories")

# Footer
st.markdown("---")
st.markdown("""
    <div class="footer">
        <p style="font-size: 1.1rem; font-weight: 600; color: #333;">✨ AI Background Remover</p>
        <p>Built with ❤️ using Streamlit and AI • Free Forever • No Registration Required</p>
        <p style="font-size: 0.9rem; margin-top: 1rem;">
            🔒 Your privacy matters: All processing happens in real-time. Images are never stored.
        </p>
    </div>
""", unsafe_allow_html=True)
