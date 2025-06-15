
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io
import base64
import firebase_admin
from firebase_admin import credentials, firestore

# Firebase Init
if not firebase_admin._apps:
    firebase_dict = dict(st.secrets["firebase"])
    cred = credentials.Certificate(firebase_dict)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Streamlit Config
st.set_page_config(layout="wide", page_title="DrawFlow")
st.title("Draw Flow")

def login_screen():
    st.markdown("""
    <style>
    .login-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 100px;
    }
    .google-btn {
        background-color: white;
        color: #444;
        border: 1px solid #ccc;
        font-size: 16px;
        font-weight: 500;
        font-family: 'Roboto', sans-serif;
        padding: 12px 24px;
        border-radius: 4px;
        display: inline-flex;
        align-items: center;
        cursor: pointer;
        transition: box-shadow 0.3s ease;
        box-shadow: 0px 1px 2px rgba(0,0,0,0.1);
    }
    .google-btn:hover {
        box-shadow: 0px 3px 6px rgba(0,0,0,0.2);
    }
    .google-icon {
        height: 20px;
        margin-right: 12px;
    }
    </style>

    <div class="login-container">
        <button class="google-btn" onclick="window.location.href = '/_stcore/login/google';">
            <img class="google-icon" src="https://upload.wikimedia.org/wikipedia/commons/5/53/Google_%22G%22_Logo.svg" />
            Log in with Google
        </button>
    </div>
    """, unsafe_allow_html=True)
    
if not st.user.is_logged_in:
    login_screen()
else:
    # Track user login in Firestore
    db.collection("users").document(st.user.email).set({
        "name": st.user.name,
        "email": st.user.email,
        "picture": st.user.picture
    }, merge=True)

    if "canvas_key" not in st.session_state:
        st.session_state.canvas_key = "canvas_1"
    if "text_objects" not in st.session_state:
        st.session_state.text_objects = []
    
    import time
    image_url = f"{st.user.picture}?t={int(time.time())}"
    st.sidebar.image(image_url, width=120)
    st.sidebar.button("Log out", on_click=st.logout)

    st.header(f"Welcome to DrawFlow, {st.user.name}!")

    stroke_width = st.sidebar.slider("Stroke width", 1, 25, 3)
    stroke_color = st.sidebar.color_picker("Stroke color", "#000000")
    fill_color_hex = st.sidebar.color_picker("Fill color", "#FFFFFF")
    fill_opacity = st.sidebar.slider("Fill opacity", 0.0, 1.0, 0.3)
    fill_color = f"rgba({int(fill_color_hex[1:3], 16)}, {int(fill_color_hex[3:5], 16)}, {int(fill_color_hex[5:7], 16)}, {fill_opacity})"
    drawing_mode = st.sidebar.selectbox("Drawing tool", ("freedraw", "line", "rect", "circle", "polygon", "point", "path", "transform"))
    bg_color = st.sidebar.color_picker("Background color", "#FFFFFF")

    st.sidebar.markdown("---")
    st.sidebar.subheader("📌 Add Text")
    text_input = st.sidebar.text_input("Text to place", "")
    font_size = st.sidebar.slider("Font size", 10, 80, 30)

    if st.sidebar.button("Place Text"):
        if text_input.strip():
            offset = len(st.session_state.text_objects) * 50
            st.session_state.text_objects.append({
                "type": "i-text",
                "left": 100 + offset,
                "top": 100 + offset,
                "text": text_input,
                "fontSize": font_size,
                "fill": stroke_color,
            })

    if st.button("🧹 Clear Screen"):
        st.session_state.canvas_key = f"canvas_{st.session_state.canvas_key.split('_')[1]}_cleared"
        st.session_state.text_objects = []

    canvas_result = st_canvas(
        fill_color=fill_color,
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        background_image=None,
        height=2000,
        width=3000,
        drawing_mode=drawing_mode,
        key=st.session_state.canvas_key,
        update_streamlit=True,
        display_toolbar=True,
        initial_drawing={"objects": st.session_state.text_objects}
    )

    if canvas_result.image_data is not None:
        st.subheader("📥 Save Canvas as Image")
        img = Image.fromarray(canvas_result.image_data.astype("uint8"))
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        b64 = base64.b64encode(buf.getvalue()).decode()
        href = f'<a href="data:file/png;base64,{b64}" download="whiteboard.png">📥 Download Canvas as PNG</a>'
        st.markdown(href, unsafe_allow_html=True)

    doc_ref = db.collection("sessions").document(st.user.email)
    doc_ref.set({
        "text_objects": st.session_state.text_objects,
    }, merge=True)
