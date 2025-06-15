# # import streamlit as st
# # from streamlit_drawable_canvas import st_canvas
# # from PIL import Image
# # import io
# # import base64
# # import payments


# # st.set_page_config(layout="wide")
# # st.title("🧠 Infinite Whiteboard (Enhanced Edition with Text Support)")
# # import streamlit as st


# # def login_screen():
    
# #     st.subheader("Please log in.")
# #     st.button("Log in with Google", on_click=st.login)

# # if not st.user.is_logged_in:
# #     login_screen()
# # else:
# #     st.header(f"Welcome to DrawFlow, {st.user.name}!")
# #     # st.json(st.user)
    

# # # Initialize session state for canvas and text objects
# #     if "canvas_key" not in st.session_state:
# #         st.session_state.canvas_key = "canvas_1"
# #     if "text_objects" not in st.session_state:
# #         st.session_state.text_objects = []


# #     st.sidebar.image(st.user.picture)
# #     if st.sidebar.button("Subscribe"):
# #         st.switch_page("payments.py")
# #     # Sidebar drawing options
# #     stroke_width = st.sidebar.slider("Stroke width", 1, 25, 3)
# #     stroke_color = st.sidebar.color_picker("Stroke color", "#000000")

# #     fill_color_hex = st.sidebar.color_picker("Fill color", "#FFFFFF")
# #     fill_opacity = st.sidebar.slider("Fill opacity", 0.0, 1.0, 0.3)
# #     fill_color = f"rgba({int(fill_color_hex[1:3], 16)}, {int(fill_color_hex[3:5], 16)}, {int(fill_color_hex[5:7], 16)}, {fill_opacity})"

# #     drawing_mode = st.sidebar.selectbox(
# #         "Drawing tool",
# #         ("freedraw", "line", "rect", "circle", "polygon", "point", "path", "transform")
# #     )

# #     bg_color = st.sidebar.color_picker("Background color", "#FFFFFF")

# #     # Text placement UI
    
# #     st.sidebar.markdown("---")
# #     st.sidebar.subheader("📌 Add Text")
# #     text_input = st.sidebar.text_input("Text to place", "")
# #     font_size = st.sidebar.slider("Font size", 10, 80, 30)

# #     if st.sidebar.button("Place Text"):
# #         if text_input.strip() != "":
# #             # Dynamically offset each text to avoid overlap
# #             offset = len(st.session_state.text_objects) * 50
# #             st.session_state.text_objects.append({
# #                 "type": "i-text",
# #                 "left": 100 + offset,
# #                 "top": 100 + offset,
# #                 "text": text_input,
# #                 "fontSize": font_size,
# #                 "fill": stroke_color,
# #             })
# #     st.sidebar.button("Log out", on_click=st.logout)

# #     # Clear canvas logic
# #     if st.button("🧹 Clear Screen"):
# #         st.session_state.canvas_key = f"canvas_{st.session_state.canvas_key.split('_')[1]}_cleared"
# #         st.session_state.text_objects = []

# #     # Draw the canvas
# #     canvas_result = st_canvas(
# #         fill_color=fill_color,
# #         stroke_width=stroke_width,
# #         stroke_color=stroke_color,
# #         background_color=bg_color,
# #         background_image=None,
# #         height=2000,
# #         width=3000,
# #         drawing_mode=drawing_mode,
# #         key=st.session_state.canvas_key,
# #         update_streamlit=True,
# #         display_toolbar=True,
# #         initial_drawing={"objects": st.session_state.text_objects}
# #     )

# #     # Export canvas image
# #     if canvas_result.image_data is not None:
# #         st.subheader("📥 Save Canvas as Image")
# #         img = Image.fromarray(canvas_result.image_data.astype("uint8"))

# #         buf = io.BytesIO()
# #         img.save(buf, format="PNG")
# #         byte_im = buf.getvalue()

# #         b64 = base64.b64encode(byte_im).decode()
# #         href = f'<a href="data:file/png;base64,{b64}" download="whiteboard.png">📥 Download Canvas as PNG</a>'
# #         st.markdown(href, unsafe_allow_html=True)


# # import streamlit as st
# # from streamlit_drawable_canvas import st_canvas
# # from PIL import Image
# # import io
# # import base64

# # # Razorpay config (dummy test key for now)
# # RAZORPAY_KEY = "JmM7NmDCzhQ9RY1CVTXuylmE"
# # # RAZORPAY_LOGO = "https://yourdomain.com/logo.png"

# # def razorpay_button(amount_paise, name, plan_id):
# #     return f"""
# #     <form>
# #         <script src="https://checkout.razorpay.com/v1/checkout.js"
# #                 data-key="{RAZORPAY_KEY}"
# #                 data-amount="{amount_paise}"
# #                 data-currency="INR"
# #                 data-name="{name}"
# #                 data-description="{plan_id}"
# #                 data-theme.color="#18181b">
# #         </script>
# #     </form>
# #     """

# # # Login check
# # st.set_page_config(layout="wide", page_title="DrawFlow")

# # st.title("🧠 Infinite Whiteboard (Enhanced Edition with Text Support)")

# # def login_screen():
# #     st.subheader("Please log in.")
# #     st.button("Log in with Google", on_click=st.login)

# # if not st.user.is_logged_in:
# #     login_screen()
# # else:
# #     if "canvas_key" not in st.session_state:
# #         st.session_state.canvas_key = "canvas_1"
# #     if "text_objects" not in st.session_state:
# #         st.session_state.text_objects = []
# #     if "active_tab" not in st.session_state:
# #         st.session_state.active_tab = "Whiteboard"

# #     st.sidebar.image(st.user.picture)
# #     if st.sidebar.button("Subscribe"):
# #         st.session_state.active_tab = "Payments"

# #     st.sidebar.button("Log out", on_click=st.logout)

# #     tabs = st.tabs(["📝 Whiteboard", "💳 Payments"])

# #     if st.session_state.active_tab == "Whiteboard":
# #         with tabs[0]:
# #             st.header(f"Welcome to DrawFlow, {st.user.name}!")

# #             # Sidebar tools
# #             stroke_width = st.sidebar.slider("Stroke width", 1, 25, 3)
# #             stroke_color = st.sidebar.color_picker("Stroke color", "#000000")
# #             fill_color_hex = st.sidebar.color_picker("Fill color", "#FFFFFF")
# #             fill_opacity = st.sidebar.slider("Fill opacity", 0.0, 1.0, 0.3)
# #             fill_color = f"rgba({int(fill_color_hex[1:3], 16)}, {int(fill_color_hex[3:5], 16)}, {int(fill_color_hex[5:7], 16)}, {fill_opacity})"
# #             drawing_mode = st.sidebar.selectbox("Drawing tool", ("freedraw", "line", "rect", "circle", "polygon", "point", "path", "transform"))
# #             bg_color = st.sidebar.color_picker("Background color", "#FFFFFF")

# #             # Text input
# #             st.sidebar.markdown("---")
# #             st.sidebar.subheader("📌 Add Text")
# #             text_input = st.sidebar.text_input("Text to place", "")
# #             font_size = st.sidebar.slider("Font size", 10, 80, 30)

# #             if st.sidebar.button("Place Text"):
# #                 if text_input.strip() != "":
# #                     offset = len(st.session_state.text_objects) * 50
# #                     st.session_state.text_objects.append({
# #                         "type": "i-text",
# #                         "left": 100 + offset,
# #                         "top": 100 + offset,
# #                         "text": text_input,
# #                         "fontSize": font_size,
# #                         "fill": stroke_color,
# #                     })

# #             # Clear screen
# #             if st.button("🧹 Clear Screen"):
# #                 st.session_state.canvas_key = f"canvas_{st.session_state.canvas_key.split('_')[1]}_cleared"
# #                 st.session_state.text_objects = []

# #             # Canvas
# #             canvas_result = st_canvas(
# #                 fill_color=fill_color,
# #                 stroke_width=stroke_width,
# #                 stroke_color=stroke_color,
# #                 background_color=bg_color,
# #                 background_image=None,
# #                 height=2000,
# #                 width=3000,
# #                 drawing_mode=drawing_mode,
# #                 key=st.session_state.canvas_key,
# #                 update_streamlit=True,
# #                 display_toolbar=True,
# #                 initial_drawing={"objects": st.session_state.text_objects}
# #             )

# #             # Download Image
# #             if canvas_result.image_data is not None:
# #                 st.subheader("📥 Save Canvas as Image")
# #                 img = Image.fromarray(canvas_result.image_data.astype("uint8"))
# #                 buf = io.BytesIO()
# #                 img.save(buf, format="PNG")
# #                 b64 = base64.b64encode(buf.getvalue()).decode()
# #                 href = f'<a href="data:file/png;base64,{b64}" download="whiteboard.png">📥 Download Canvas as PNG</a>'
# #                 st.markdown(href, unsafe_allow_html=True)

# #     elif st.session_state.active_tab == "Payments":
# #         with tabs[1]:
# #             st.header("💳 Subscription Plans")
# #             billing_cycle = st.radio("Select Billing", ["Monthly", "Annually"], horizontal=True)

# #             if billing_cycle == "Monthly":
# #                 col1, col2 = st.columns(2)
# #                 with col1:
# #                     st.subheader("🆓 Free")
# #                     st.markdown("**$0/mo**")
# #                     st.markdown("✔️ 10 image downloads/month\n👥 3 collaborators")
# #                     st.button("Current Plan", disabled=True)
# #                 with col2:
# #                     st.subheader("💳 Pro")
# #                     st.markdown("**$20/mo**")
# #                     st.markdown("✔️ 50 image downloads/month\n👥 5 collaborators")
# #                     st.components.v1.html(razorpay_button(2000 * 100, "Monthly Pro", "monthly_pro"), height=100)

# #             else:
# #                 col1, col2 = st.columns(2)
# #                 with col1:
# #                     st.subheader("🆓 Free")
# #                     st.markdown("**$0/yr**")
# #                     st.markdown("✔️ 100 image downloads/year\n👥 5 collaborators")
# #                     st.button("Current Plan", disabled=True)
# #                 with col2:
# #                     st.subheader("💎 Pro")
# #                     st.markdown("**$100/yr**")
# #                     st.markdown("✔️ Unlimited downloads\n👥 10 collaborators\n✨ AI Features")
# #                     st.components.v1.html(razorpay_button(10000 * 100, "Annual Pro", "annual_pro"), height=100)


# # main.py
# # main.py

# import streamlit as st
# from streamlit_drawable_canvas import st_canvas
# from PIL import Image
# import io
# import base64
# import firebase_admin
# from firebase_admin import credentials, firestore

# # Firebase Init
# if not firebase_admin._apps:
#     cred = credentials.Certificate("firebase-admin-sdk.json")
#     firebase_admin.initialize_app(cred)

# db = firestore.client()

# # Razorpay Button IDs
# RAZORPAY_BUTTON_MONTHLY = "pl_Qei8yprLiYVKRm"
# RAZORPAY_BUTTON_ANNUALLY = "pl_QeiAfRriDXasBn"

# def razorpay_button_html(button_id, user_email):
#     return f"""
#     <form>
#         <script src=\"https://checkout.razorpay.com/v1/payment-button.js\"
#                 data-payment_button_id=\"{button_id}\"
#                 data-prefill.email=\"{user_email}\"
#                 async>
#         </script>
#     </form>
#     """

# def get_latest_text_objects(email):
#     doc = db.collection("sessions").document(email).get()
#     if doc.exists:
#         data = doc.to_dict()
#         return data.get("text_objects", [])
#     return []

# # Streamlit Config
# st.set_page_config(layout="wide", page_title="DrawFlow")
# st.title("🧠 Infinite Whiteboard (Enhanced Edition with Text Support)")

# def login_screen():
#     st.subheader("Please log in.")
#     st.button("Log in with Google", on_click=st.login)

# if not st.user.is_logged_in:
#     login_screen()
# else:
#     if "user_plan" not in st.session_state:
#         user_ref = db.collection("subscriptions").document(st.user.email)
#         doc = user_ref.get()
#         if doc.exists:
#             st.session_state.user_plan = doc.to_dict().get("plan", "Free")
#         else:
#             user_ref.set({"plan": "Free"})
#             st.session_state.user_plan = "Free"
#     if "canvas_key" not in st.session_state:
#         st.session_state.canvas_key = "canvas_1"
#     if "text_objects" not in st.session_state:
#         st.session_state.text_objects = []
#     if "owner_email" not in st.session_state:
#         st.session_state.owner_email = st.user.email
#     if "active_tab" not in st.session_state:
#         st.session_state.active_tab = "Whiteboard"

#     # Real-time sync (no collaborators)
#     owner_email = st.user.email
#     latest_text_objects = get_latest_text_objects(owner_email)
#     st.session_state.text_objects = latest_text_objects

#     st.sidebar.image(st.user.picture)
#     if st.sidebar.button("Subscribe"):
#         st.session_state.active_tab = "Payments"
#     st.sidebar.button("Log out", on_click=st.logout)

#     tabs = st.tabs(["📝 Whiteboard", "💳 Payments"])

#     if st.session_state.active_tab == "Whiteboard":
#         with tabs[0]:
#             st.header(f"Welcome to DrawFlow, {st.user.name}!")
#             st.info(f"🎯 Your current plan: {st.session_state.user_plan}")

#             stroke_width = st.sidebar.slider("Stroke width", 1, 25, 3)
#             stroke_color = st.sidebar.color_picker("Stroke color", "#000000")
#             fill_color_hex = st.sidebar.color_picker("Fill color", "#FFFFFF")
#             fill_opacity = st.sidebar.slider("Fill opacity", 0.0, 1.0, 0.3)
#             fill_color = f"rgba({int(fill_color_hex[1:3], 16)}, {int(fill_color_hex[3:5], 16)}, {int(fill_color_hex[5:7], 16)}, {fill_opacity})"
#             drawing_mode = st.sidebar.selectbox("Drawing tool", ("freedraw", "line", "rect", "circle", "polygon", "point", "path", "transform"))
#             bg_color = st.sidebar.color_picker("Background color", "#FFFFFF")

#             st.sidebar.markdown("---")
#             st.sidebar.subheader("📌 Add Text")
#             text_input = st.sidebar.text_input("Text to place", "")
#             font_size = st.sidebar.slider("Font size", 10, 80, 30)

#             if st.sidebar.button("Place Text"):
#                 if text_input.strip():
#                     offset = len(st.session_state.text_objects) * 50
#                     st.session_state.text_objects.append({
#                         "type": "i-text",
#                         "left": 100 + offset,
#                         "top": 100 + offset,
#                         "text": text_input,
#                         "fontSize": font_size,
#                         "fill": stroke_color,
#                     })

#             if st.button("🧹 Clear Screen"):
#                 st.session_state.canvas_key = f"canvas_{st.session_state.canvas_key.split('_')[1]}_cleared"
#                 st.session_state.text_objects = []

#             canvas_result = st_canvas(
#                 fill_color=fill_color,
#                 stroke_width=stroke_width,
#                 stroke_color=stroke_color,
#                 background_color=bg_color,
#                 background_image=None,
#                 height=2000,
#                 width=3000,
#                 drawing_mode=drawing_mode,
#                 key=st.session_state.canvas_key,
#                 update_streamlit=True,
#                 display_toolbar=True,
#                 initial_drawing={"objects": st.session_state.text_objects}
#             )

#             if canvas_result.image_data is not None:
#                 st.subheader("📥 Save Canvas as Image")
#                 img = Image.fromarray(canvas_result.image_data.astype("uint8"))
#                 buf = io.BytesIO()
#                 img.save(buf, format="PNG")
#                 b64 = base64.b64encode(buf.getvalue()).decode()
#                 href = f'<a href="data:file/png;base64,{b64}" download="whiteboard.png">📥 Download Canvas as PNG</a>'
#                 st.markdown(href, unsafe_allow_html=True)

#             # PDF Export logic
#             from PIL import Image
#             import base64
#             from fpdf import FPDF

#             def export_canvas_as_pdf(image_data):
#                 img = Image.fromarray(image_data.astype("uint8"))
#                 temp_img_path = "/tmp/temp_canvas.png"
#                 img.save(temp_img_path)

#                 pdf = FPDF()
#                 pdf.add_page()
#                 pdf.image(temp_img_path, x=10, y=10, w=180)

#                 if st.session_state.user_plan == "Free":
#                     pdf.set_font("Arial", size=12)
#                     pdf.set_text_color(180, 180, 180)
#                     pdf.text(10, 280, "Generated with DrawFlow (Free Plan)")

#                 output_pdf = "/tmp/canvas_output.pdf"
#                 pdf.output(output_pdf)

#                 with open(output_pdf, "rb") as f:
#                     base64_pdf = base64.b64encode(f.read()).decode("utf-8")
#                     href = f'<a href="data:application/pdf;base64,{base64_pdf}" download="whiteboard.pdf">📄 Download Canvas as PDF</a>'
#                     st.markdown(href, unsafe_allow_html=True)

#             if canvas_result.image_data is not None:
#                 if "pdf_exports" not in st.session_state:
#                     st.session_state.pdf_exports = 0

#                 if st.button("📄 Export as PDF"):
#                     if st.session_state.user_plan == "Free" and st.session_state.pdf_exports >= 5:
#                         st.warning("You’ve reached the 5 free PDF exports limit this month.")
#                     else:
#                         export_canvas_as_pdf(canvas_result.image_data)
#                         st.session_state.pdf_exports += 1

#             doc_ref = db.collection("sessions").document(st.user.email)
#             doc_ref.set({
#                 "text_objects": st.session_state.text_objects,
#             }, merge=True)

#             if st.session_state.user_plan == "Free":
#                 st.caption("🔒 Limited to 10 downloads/month & 5 PDF exports in Free Plan.")
#             elif st.session_state.user_plan == "Pro":
#                 st.success("✅ Pro benefits unlocked: 50 downloads & 50 PDF exports (or more)")

#     elif st.session_state.active_tab == "Payments":
#         with tabs[1]:
#             st.header("💳 Subscription Plans")
#             billing_cycle = st.radio("Select Billing", ["Monthly", "Annually"], horizontal=True)

#             if billing_cycle == "Monthly":
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     st.subheader("🆓 Free")
#                     st.markdown("**₹0/mo**")
#                     st.markdown("✔️ 10 image downloads/month\n✔️ 5 PDF exports/month (with watermark)")
#                     st.button("Current Plan", disabled=True)
#                 with col2:
#                     st.subheader("💳 Pro")
#                     st.markdown("**₹299/mo**")
#                     st.markdown("✔️ 50 image downloads/month\n✔️ 50 PDF exports/month (no watermark)")
#                     if st.session_state.user_plan == "Pro":
#                         st.button("Current Plan", disabled=True)
#                     else:
#                         st.components.v1.html(razorpay_button_html(RAZORPAY_BUTTON_MONTHLY, st.user.email), height=650)
#                         if st.button("Simulate Pro Upgrade (for dev only)"):
#                             db.collection("subscriptions").document(st.user.email).set({"plan": "Pro"})
#                             st.session_state.user_plan = "Pro"

#             else:
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     st.subheader("🆓 Free")
#                     st.markdown("**₹0/yr**")
#                     st.markdown("✔️ 100 image downloads/year\n✔️ 5 PDF exports/month (with watermark)")
#                     st.button("Current Plan", disabled=True)
#                 with col2:
#                     st.subheader("💎 Pro")
#                     st.markdown("**₹1099/yr**")
#                     st.markdown("✔️ Unlimited image downloads\n✔️ Unlimited PDF exports (no watermark)\n✨ AI Features")
#                     if st.session_state.user_plan == "Pro":
#                         st.button("Current Plan", disabled=True)
#                     else:
#                         st.components.v1.html(razorpay_button_html(RAZORPAY_BUTTON_ANNUALLY, st.user.email), height=650)
#                         if st.button("Simulate Pro Upgrade (for dev only)"):
#                             db.collection("subscriptions").document(st.user.email).set({"plan": "Pro"})
#                             st.session_state.user_plan = "Pro"


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
    st.subheader("Please log in.")
    st.button("Log in with Google", on_click=st.login)

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