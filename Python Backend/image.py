# import streamlit as st
# import numpy as np
# import cv2
# import tensorflow as tf
# from tensorflow.keras.models import load_model
# import os
# import sqlite3
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
# st.set_page_config(
#     page_title="ECG Arrhythmia Classifier",
#     page_icon="💓",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )
# # Database Setup
# def init_db():
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             full_name TEXT NOT NULL,
#             username TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#         )
#     """)
#     conn.commit()
#     conn.close()

# def register_user(full_name, username, password):
#     try:
#         conn = sqlite3.connect("users.db")
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO users (full_name, username, password) VALUES (?, ?, ?)", (full_name, username, password))
#         conn.commit()
#         conn.close()
#         return True
#     except sqlite3.IntegrityError:
#         return False

# def check_user(username, password):
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
#     user = cursor.fetchone()
#     conn.close()
#     return user is not None

# init_db()

# # Load the trained model
# model_path = "svm_model.h5"
# if os.path.exists(model_path):
#     model = load_model(model_path)
# else:
#     st.error(f"Model file does not exist: {model_path}")

# # Label Mapping
# label_to_category = {
#     1: "Normal beats",
#     2: "Supraventricular beats",
#     3: "Unknown beats",
#     4: "Ventricular beats",
#     5: "Fusion beats",
# }

# # Preprocess Image
# def preprocess_image(image):
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     image = cv2.resize(image, (224, 224))
#     image = image / 255.0
#     return np.expand_dims(image, axis=0)

# # Sidebar Navigation with Collapsed Initial State
# with st.sidebar:
#     st.sidebar.title("ECG Arrhythmia Classifier")
#     if "logged_in" not in st.session_state:
#         st.session_state.logged_in = False
#         st.session_state.username = ""
#     st.write("""This app predicts the type of heartbeats based on provided ECG image.

#     Normal beats  
#     Supraventricular  beats  
#     Ventricular  beats  
#     Fusion beats  
#     Unknown beats 

#     """)
#     if not st.session_state.logged_in:
#         page = st.sidebar.radio("Account", ["Login", "Sign Up"], index=0, key="nav")
#     else:
#         page = "ECG Classification"

# # Signup Page
# if page == "Sign Up":
#     st.title("Sign Up")
#     full_name = st.text_input("Full Name")
#     new_username = st.text_input("Username")
#     new_password = st.text_input("Password", type="password")
#     confirm_password = st.text_input("Confirm Password", type="password")
    
#     if st.button("Register"):
#         if new_password != confirm_password:
#             st.warning("Passwords do not match. Try again.")
#         elif register_user(full_name, new_username, new_password):
#             st.success("Registered successfully! Go to Login page.")
#         else:
#             st.warning("Username already exists. Try another.")
    


# # Login Page
# elif page == "Login":
#     st.title("Login")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
    
#     if st.button("Login"):
#         if check_user(username, password):
#             st.session_state.logged_in = True
#             st.session_state.username = username
#             st.success("Login successful! Redirecting...")
#             st.rerun()
#         else:
#             st.error("Invalid username or password")
    


# # ECG Classification Page (Protected Page)
# if st.session_state.logged_in:
#     st.sidebar.radio("", ["ECG Classification"], index=0)
#     st.title("ECG Heartbeat Classification")
#     st.write("Upload an ECG Image to Predict the Beat Type.")
#     uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
    
#     if uploaded_file is not None:
#         file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#         image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
#         if image is not None:
#             st.image(image, caption="Uploaded Image", use_container_width=True)
#             st.write("Processing...")
#             try:
#                 input_image = preprocess_image(image)
#                 y_pred = model.predict(input_image)
#                 predicted_label = label_to_category.get(np.argmax(y_pred), "Unknown")
#                 st.success(f"Predicted Class: **{predicted_label}**")
#             except Exception as e:
#                 st.error(f"Error: {str(e)}")
#         else:
#             st.error("Error loading image. Please upload a valid file.")



# hide_deploy = """
#     <style>
#         button[kind="deploy"], 
#         div[data-testid="stToolbar"] { 
#             display: none !important; 
#         }
#     </style>
# """
# st.markdown(hide_deploy, unsafe_allow_html=True)

# import streamlit as st
# import numpy as np
# import cv2
# import tensorflow as tf
# from tensorflow.keras.models import load_model
# import os
# import sqlite3
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# st.set_page_config(
#     page_title="ECG Arrhythmia Classifier",
#     page_icon="💓",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Database Setup
# def init_db():
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             full_name TEXT NOT NULL,
#             username TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#         )
#     """)
#     conn.commit()
#     conn.close()

# def register_user(full_name, username, password):
#     try:
#         conn = sqlite3.connect("users.db")
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO users (full_name, username, password) VALUES (?, ?, ?)", (full_name, username, password))
#         conn.commit()
#         conn.close()
#         return True
#     except sqlite3.IntegrityError:
#         return False

# def check_user(username, password):
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
#     user = cursor.fetchone()
#     conn.close()
#     return user is not None

# init_db()

# # Load the trained model
# model_path = "svm_model.h5"
# if os.path.exists(model_path):
#     model = load_model(model_path)
# else:
#     st.error(f"Model file does not exist: {model_path}")

# # Label Mapping
# label_to_category = {
#     1: "Normal beats",
#     2: "Supraventricular beats",
#     3: "Unknown beats",
#     4: "Ventricular beats",
#     5: "Fusion beats",
# }

# # Preprocess Image
# def preprocess_image(image):
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     image = cv2.resize(image, (224, 224))
#     image = image / 255.0
#     return np.expand_dims(image, axis=0)

# # Sidebar Navigation with Collapsed Initial State
# with st.sidebar:
#     st.sidebar.title("ECG Arrhythmia Classifier")
#     if "logged_in" not in st.session_state:
#         st.session_state.logged_in = False
#         st.session_state.username = ""
#     st.write("This app predicts the type of heartbeats based on provided ECG image.")
#     st.write("Normal beats")  
#     st.write("Supraventricular beats")
#     st.write("Ventricular beats ")
#     st.write("Fusion beats ")
#     st.write("Unknown beats ")
#     if not st.session_state.logged_in:
#         page = st.sidebar.radio("Account", ["Login", "Sign Up"], index=0, key="nav")
#     else:
#         page = "ECG Classification"

# # Signup Page
# if page == "Sign Up":
#     st.title("Sign Up")
#     full_name = st.text_input("Full Name")
#     new_username = st.text_input("Username")
#     new_password = st.text_input("Password", type="password")
#     confirm_password = st.text_input("Confirm Password", type="password")
    
#     if st.button("Register"):
#         if new_password != confirm_password:
#             st.warning("Passwords do not match. Try again.")
#         elif register_user(full_name, new_username, new_password):
#             st.success("Registered successfully! Go to Login page.")
#         else:
#             st.warning("Username already exists. Try another.")

# # Login Page
# elif page == "Login":
#     st.title("Login")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
    
#     if st.button("Login"):
#         if check_user(username, password):
#             st.session_state.logged_in = True
#             st.session_state.username = username
#             st.success("Login successful! Redirecting...")
#             st.rerun()
#         else:
#             st.error("Invalid username or password")

# # ECG Classification Page (Protected Page)
# if st.session_state.logged_in:
#     st.sidebar.radio("", ["ECG Classification"], index=0)

#     # ✅ Add Logout Button in the Top-Right Corner
#     col1, col2 = st.columns([8, 1])
#     with col2:
#         if st.button("Logout"):
#             st.session_state.logged_in = False
#             st.session_state.username = ""
#             st.rerun()

#     st.title("ECG Heartbeat Classification")
#     st.write("Upload an ECG Image to Predict the Beat Type.")
#     uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
    
#     if uploaded_file is not None:
#         file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#         image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
#         if image is not None:
#             st.image(image, caption="Uploaded Image", use_container_width=True)
#             st.write("Processing...")
#             try:
#                 input_image = preprocess_image(image)
#                 y_pred = model.predict(input_image)
#                 predicted_label = label_to_category.get(np.argmax(y_pred), "Unknown")
#                 st.success(f"Predicted Class: **{predicted_label}**")
#             except Exception as e:
#                 st.error(f"Error: {str(e)}")
#         else:
#             st.error("Error loading image. Please upload a valid file.")

# # Hide Deploy Button and Toolbar
# hide_deploy = """
#     <style>
#         button[kind="deploy"], 
#         div[data-testid="stToolbar"] { 
#             display: none !important; 
#         }
#     </style>
# """
# st.markdown(hide_deploy, unsafe_allow_html=True)


# footer = """
#     <style>
#         .footer {
#             position: center;
#             bottom: 0;
#             width: 100%;
#             background-color: #222;
#             color: white;
#             text-align: center;
#             padding: 10px;
#             font-size: 14px;
#         }
#     </style>
#     <div class="footer">
#         &copy; <span id="year"></span> ECG Arrhythmia Classifier. All rights reserved.
#     </div>
#     <script>
#         document.getElementById("year").textContent = new Date().getFullYear();
#     </script>
# """

# # Display Footer
# st.markdown(footer, unsafe_allow_html=True)

# import streamlit as st
# import numpy as np
# import cv2
# import tensorflow as tf
# from tensorflow.keras.models import load_model
# import os
# import sqlite3
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# st.set_page_config(
#     page_title="ECG Arrhythmia Classifier",
#     page_icon="💓",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Database Setup
# def init_db():
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             full_name TEXT NOT NULL,
#             username TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#         )
#     """)
#     conn.commit()
#     conn.close()

# def register_user(full_name, username, password):
#     try:
#         conn = sqlite3.connect("users.db")
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO users (full_name, username, password) VALUES (?, ?, ?)", (full_name, username, password))
#         conn.commit()
#         conn.close()
#         return True
#     except sqlite3.IntegrityError:
#         return False

# def check_user(username, password):
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
#     user = cursor.fetchone()
#     conn.close()
#     return user is not None

# init_db()

# # Load the trained model
# model_path = "svm_model.h5"
# if os.path.exists(model_path):
#     model = load_model(model_path)
# else:
#     st.error(f"Model file does not exist: {model_path}")

# # Label Mapping
# label_to_category = {
#     1: "Normal beats",
#     2: "Supraventricular beats",
#     3: "Unknown beats",
#     4: "Ventricular beats",
#     5: "Fusion beats",
# }

# # Preprocess Image
# def preprocess_image(image):
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     image = cv2.resize(image, (224, 224))
#     image = image / 255.0
#     return np.expand_dims(image, axis=0)

# # Sidebar Navigation
# with st.sidebar:
#     st.sidebar.title("ECG Arrhythmia Classifier")
    
#     if "logged_in" not in st.session_state:
#         st.session_state.logged_in = False
#         st.session_state.username = ""

#     st.write("This app predicts the type of heartbeats based on provided ECG image.")
#     st.write("Normal beats")  
#     st.write("Supraventricular beats")
#     st.write("Ventricular beats")
#     st.write("Fusion beats")
#     st.write("Unknown beats")

#     if not st.session_state.logged_in:
#         st.markdown(
#             """
#             <div style="padding: 10px;">
#                 <a href="?page=login" style="font-size:18px; text-decoration:none; margin-right: 15px;">🔑 Login</a>  
#                 <a href="?page=signup" style="font-size:18px; text-decoration:none; color: #ff4b4b;">📝 Sign Up</a>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )
#         page = st.query_params.get("page", "Login")
#     else:
#         page = "ECG Classification"

# # Signup Page
# if page == "signup":
#     st.title("Sign Up")
#     full_name = st.text_input("Full Name")
#     new_username = st.text_input("Username")
#     new_password = st.text_input("Password", type="password")
#     confirm_password = st.text_input("Confirm Password", type="password")
    
#     if st.button("Register"):
#         if new_password != confirm_password:
#             st.warning("Passwords do not match. Try again.")
#         elif register_user(full_name, new_username, new_password):
#             st.success("Registered successfully! Go to Login page.")
#         else:
#             st.warning("Username already exists. Try another.")

# # Login Page
# elif page == "login":
#     st.title("Login")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
    
#     if st.button("Login"):
#         if check_user(username, password):
#             st.session_state.logged_in = True
#             st.session_state.username = username
#             st.success("Login successful! Redirecting...")
#             st.rerun()
#         else:
#             st.error("Invalid username or password")

# # ECG Classification Page (Protected Page)
# if st.session_state.logged_in:
#     st.sidebar.radio("", ["ECG Classification"], index=0)

#     # ✅ Add Logout Button in the Top-Right Corner
#     col1, col2 = st.columns([8, 1])
#     with col2:
#         if st.button("Logout"):
#             st.session_state.logged_in = False
#             st.session_state.username = ""
#             st.rerun()

#     st.title("ECG Heartbeat Classification")
#     st.write("Upload an ECG Image to Predict the Beat Type.")
#     uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
    
#     if uploaded_file is not None:
#         file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#         image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
#         if image is not None:
#             st.image(image, caption="Uploaded Image", use_container_width=True)
#             st.write("Processing...")
#             try:
#                 input_image = preprocess_image(image)
#                 y_pred = model.predict(input_image)
#                 predicted_label = label_to_category.get(np.argmax(y_pred), "Unknown")
#                 st.success(f"Predicted Class: **{predicted_label}**")
#             except Exception as e:
#                 st.error(f"Error: {str(e)}")
#         else:
#             st.error("Error loading image. Please upload a valid file.")

# # Hide Deploy Button and Toolbar
# hide_deploy = """
#     <style>
#         button[kind="deploy"], 
#         div[data-testid="stToolbar"] { 
#             display: none !important; 
#         }
#     </style>
# """
# st.markdown(hide_deploy, unsafe_allow_html=True)

# # Footer
# footer = """
#     <style>
#         .footer {
#             position: center;
#             bottom: 0;
#             width: 100%;
#             background-color: #222;
#             color: white;
#             text-align: center;
#             padding: 10px;
#             font-size: 14px;
#         }
#     </style>
#     <div class="footer">
#         &copy; <span id="year"></span> ECG Arrhythmia Classifier. All rights reserved.
#     </div>
#     <script>
#         document.getElementById("year").textContent = new Date().getFullYear();
#     </script>
# """

# # Display Footer
# st.markdown(footer, unsafe_allow_html=True)

# import streamlit as st
# import numpy as np
# import cv2
# import tensorflow as tf
# from tensorflow.keras.models import load_model
# import os
# import sqlite3
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# # Ensure eager execution is enabled (TensorFlow 2.x should have it enabled by default)
# if not tf.executing_eagerly():
#     tf.compat.v1.enable_eager_execution()

# st.set_page_config(
#     page_title="ECG Arrhythmia Classifier",
#     page_icon="💓",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Database Setup
# def init_db():
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             full_name TEXT NOT NULL,
#             username TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#         )
#     """)
#     conn.commit()
#     conn.close()

# def register_user(full_name, username, password):
#     try:
#         conn = sqlite3.connect("users.db")
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO users (full_name, username, password) VALUES (?, ?, ?)", (full_name, username, password))
#         conn.commit()
#         conn.close()
#         return True
#     except sqlite3.IntegrityError:
#         return False

# def check_user(username, password):
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
#     user = cursor.fetchone()
#     conn.close()
#     return user is not None

# init_db()

# # Load the trained model
# model_path = "svm_model.h5"
# if os.path.exists(model_path):
#     model = load_model(model_path)
# else:
#     st.error(f"Model file does not exist: {model_path}")

# # Label Mapping
# label_to_category = {
#     1: "Normal beats",
#     2: "Supraventricular beats",
#     3: "Unknown beats",
#     4: "Ventricular beats",
#     5: "Fusion beats",
# }

# # Preprocess Image
# def preprocess_image(image):
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     image = cv2.resize(image, (224, 224))
#     image = image / 255.0
#     return np.expand_dims(image, axis=0)

# # Sidebar Navigation with Login/Signup
# with st.sidebar:
#     st.sidebar.title("ECG Arrhythmia Classifier")
#     if "logged_in" not in st.session_state:
#         st.session_state.logged_in = False
#         st.session_state.username = ""
#         st.session_state.page = "login"
    
#     if not st.session_state.logged_in:
#         if st.session_state.page == "login":
#             st.subheader("Login")
#             username = st.text_input("Username")
#             password = st.text_input("Password", type="password")
#             if st.button("Login"):
#                 if check_user(username, password):
#                     st.session_state.logged_in = True
#                     st.session_state.username = username
#                     st.success("Login successful! Redirecting...")
#                     st.rerun()
#                 else:
#                     st.error("Invalid username or password")
#             # Add link text for new registration below login
#             st.markdown("[New Registration](#)", unsafe_allow_html=True)
#             if st.button("New Registration"):
#                 st.session_state.page = "signup"
#                 st.rerun()
        
#         elif st.session_state.page == "signup":
#             st.subheader("Sign Up")
#             full_name = st.text_input("Full Name")
#             new_username = st.text_input("New Username")
#             new_password = st.text_input("New Password", type="password")
#             confirm_password = st.text_input("Confirm Password", type="password")
#             if st.button("Register"):
#                 if new_password != confirm_password:
#                     st.warning("Passwords do not match. Try again.")
#                 elif register_user(full_name, new_username, new_password):
#                     st.success("Registered successfully! Please login.")
#                     st.session_state.page = "login"
#                     st.rerun()
#                 else:
#                     st.warning("Username already exists. Try another.")
#             if st.button("Back to Login"):
#                 st.session_state.page = "login"
#                 st.rerun()
#     else:
#         if st.button("Logout"):
#             st.session_state.logged_in = False
#             st.session_state.username = ""
#             st.rerun()

# # Main Page Content
# st.title("ECG Arrhythmia Classification System")
# st.write("This app predicts the type of heartbeats based on provided ECG images.")
# st.markdown("""
#     - **Normal beats**  
#     - **Supraventricular beats**  
#     - **Ventricular beats**  
#     - **Fusion beats**  
#     - **Unknown beats**  
# """)

# # ECG Classification Page (Protected Page)
# if st.session_state.logged_in:
#     st.title("Upload ECG Image for Classification")
#     uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
    
#     if uploaded_file is not None:
#         file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#         image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
#         if image is not None:
#             st.image(image, caption="Uploaded Image", use_container_width=True)
#             st.write("Processing...")
#             try:
#                 input_image = preprocess_image(image)
#                 y_pred = model.predict(input_image)
#                 predicted_label = label_to_category.get(np.argmax(y_pred), "Unknown")
#                 st.success(f"Predicted Class: **{predicted_label}**")
#             except Exception as e:
#                 st.error(f"Error: {str(e)}")
#         else:
#             st.error("Error loading image. Please upload a valid file.")

# # Footer
# footer = """
#     <style>
#         .footer {
#             position: center;
#             bottom: 0;
#             width: 100%;
#             background-color: #222;
#             color: white;
#             text-align: center;
#             padding: 10px;
#             font-size: 14px;
#         }
#     </style>
#     <div class="footer">
#         &copy; <span id="year"></span> ECG Arrhythmia Classifier. All rights reserved.
#     </div>
#     <script>
#         document.getElementById("year").textContent = new Date().getFullYear();
#     </script>
# """
# hide_deploy = """
#     <style>
#         button[kind="deploy"], 
#         div[data-testid="stToolbar"] { 
#             display: none !important; 
#         }
#     </style>
# """
# st.markdown(hide_deploy, unsafe_allow_html=True)
# st.markdown(footer, unsafe_allow_html=True)


# import streamlit as st
# import numpy as np
# import cv2
# import tensorflow as tf
# from tensorflow.keras.models import load_model
# import os
# import sqlite3

# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# # Ensure eager execution is enabled (TensorFlow 2.x should have it enabled by default)
# if not tf.executing_eagerly():
#     tf.compat.v1.enable_eager_execution()

# st.set_page_config(
#     page_title="ECG Arrhythmia Classifier",
#     page_icon="💓",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Database Setup
# def init_db():
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             full_name TEXT NOT NULL,
#             username TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#         )
#     """)
#     conn.commit()
#     conn.close()

# def register_user(full_name, username, password):
#     if not full_name or not username or not password:
#         return "All fields are required."
    
#     try:
#         conn = sqlite3.connect("users.db")
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO users (full_name, username, password) VALUES (?, ?, ?)", (full_name, username, password))
#         conn.commit()
#         conn.close()
#         return "success"
#     except sqlite3.IntegrityError:
#         return "Username already exists. Try another."

# def check_user(username, password):
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
#     user = cursor.fetchone()
#     conn.close()
#     return user is not None

# init_db()

# # Load the trained model
# model_path = "svm_model.h5"
# if os.path.exists(model_path):
#     model = load_model(model_path)
# else:
#     st.error(f"Model file does not exist: {model_path}")

# # Label Mapping
# label_to_category = {
#     1: "Normal beats",
#     2: "Supraventricular beats",
#     3: "Unknown beats",
#     4: "Ventricular beats",
#     5: "Fusion beats",
# }

# # Preprocess Image
# def preprocess_image(image):
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     image = cv2.resize(image, (224, 224))
#     image = image / 255.0
#     return np.expand_dims(image, axis=0)

# # Sidebar Navigation with Login/Signup
# with st.sidebar:
#     st.sidebar.title("ECG Arrhythmia Classifier")
    
#     if "page" not in st.session_state:
#         st.session_state.page = "login"  # Default to login page

#     if "logged_in" not in st.session_state:
#         st.session_state.logged_in = False
#         st.session_state.username = ""

#     if st.session_state.page == "login":
#         st.subheader("Login")
#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")
        
#         if st.button("Login"):
#             if check_user(username, password):
#                 st.session_state.logged_in = True
#                 st.session_state.username = username
#                 st.session_state.page = "main"
#                 st.rerun()  # Redirect to main page
#             else:
#                 st.error("Invalid username or password")
        
#         if st.button("New Registration"):
#             st.session_state.page = "signup"
#             st.rerun()

#     elif st.session_state.page == "signup":
#         st.subheader("Sign Up")
#         full_name = st.text_input("Full Name")
#         new_username = st.text_input("New Username")
#         new_password = st.text_input("New Password", type="password")
#         confirm_password = st.text_input("Confirm Password", type="password")

#         if st.button("Register"):
#             if new_password != confirm_password:
#                 st.warning("Passwords do not match. Try again.")
#             else:
#                 result = register_user(full_name, new_username, new_password)
#                 if result == "success":
#                     st.success("Registered successfully! Please login.")
#                     st.session_state.page = "login"
#                     st.experimental_rerun()
#                 else:
#                     st.warning(result)

#         if st.button("Back to Login"):
#             st.session_state.page = "login"
#             st.experimental_rerun()

#     if st.session_state.logged_in:
#         if st.button("Logout"):
#             st.session_state.logged_in = False
#             st.session_state.username = ""
#             st.session_state.page = "login"
#             st.rerun()

# # Main Page Content (Only Show if Logged In)
# if st.session_state.logged_in and st.session_state.page == "main":
#     st.title("ECG Arrhythmia Classification System")
#     st.write("This app predicts the type of heartbeats based on provided ECG images.")
#     st.markdown("""
#         - **Normal beats**  
#         - **Supraventricular beats**  
#         - **Ventricular beats**  
#         - **Fusion beats**  
#         - **Unknown beats**  
#     """)

#     st.title("Upload ECG Image for Classification")
#     uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
    
#     if uploaded_file is not None:
#         file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#         image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
#         if image is not None:
#             st.image(image, caption="Uploaded Image", use_container_width=True)
#             st.write("Processing...")
#             try:
#                 input_image = preprocess_image(image)
#                 y_pred = model.predict(input_image)
#                 predicted_label = label_to_category.get(np.argmax(y_pred), "Unknown")
#                 st.success(f"Predicted Class: **{predicted_label}**")
#             except Exception as e:
#                 st.error(f"Error: {str(e)}")
#         else:
#             st.error("Error loading image. Please upload a valid file.")

# # Footer
# footer = """
#     <style>
#         .footer {
#             position: center;
#             bottom: 0;
#             width: 100%;
#             background-color: #222;
#             color: white;
#             text-align: center;
#             padding: 10px;
#             font-size: 14px;
#         }
#     </style>
#     <div class="footer">
#         &copy; <span id="year"></span> ECG Arrhythmia Classifier. All rights reserved.
#     </div>
#     <script>
#         document.getElementById("year").textContent = new Date().getFullYear();
#     </script>
# """
# hide_deploy = """
#     <style>
#         button[kind="deploy"], 
#         div[data-testid="stToolbar"] { 
#             display: none !important; 
#         }
#     </style>
# """
# st.markdown(hide_deploy, unsafe_allow_html=True)
# st.markdown(footer, unsafe_allow_html=True)


# import streamlit as st
# import numpy as np
# import cv2
# import tensorflow as tf
# from tensorflow.keras.models import load_model
# import os
# import sqlite3

# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# # Ensure eager execution is enabled (TensorFlow 2.x should have it enabled by default)
# if not tf.executing_eagerly():
#     tf.compat.v1.enable_eager_execution()

# st.set_page_config(
#     page_title="ECG Arrhythmia Classifier",
#     page_icon="💓",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Database Setup
# def init_db():
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             full_name TEXT NOT NULL,
#             username TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#         )
#     """)
#     conn.commit()
#     conn.close()

# def register_user(full_name, username, password):
#     try:
#         conn = sqlite3.connect("users.db")
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO users (full_name, username, password) VALUES (?, ?, ?)", (full_name, username, password))
#         conn.commit()
#         conn.close()
#         return True
#     except sqlite3.IntegrityError:
#         return False

# def check_user(username, password):
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
#     user = cursor.fetchone()
#     conn.close()
#     return user is not None

# init_db()

# # Load the trained model
# model_path = "svm_model.h5"
# if os.path.exists(model_path):
#     model = load_model(model_path)
# else:
#     st.error(f"Model file does not exist: {model_path}")

# # Label Mapping
# label_to_category = {
#     1: "Normal beats",
#     2: "Supraventricular beats",
#     3: "Unknown beats",
#     4: "Ventricular beats",
#     5: "Fusion beats",
# }

# # Preprocess Image
# def preprocess_image(image):
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     image = cv2.resize(image, (224, 224))
#     image = image / 255.0
#     return np.expand_dims(image, axis=0)

# # Sidebar Navigation with Login/Signup
# with st.sidebar:
#     st.sidebar.title("ECG Arrhythmia Classifier")
#     if "logged_in" not in st.session_state:
#         st.session_state.logged_in = False
#         st.session_state.username = ""
#         st.session_state.page = "login"
    
#     if not st.session_state.logged_in:
#         if st.session_state.page == "login":
#             st.subheader("Login")
#             username = st.text_input("Username")
#             password = st.text_input("Password", type="password")
#             if st.button("Login"):
#                 if check_user(username, password):
#                     st.session_state.logged_in = True
#                     st.session_state.username = username
#                     st.success("Login successful! Redirecting...")
#                     st.rerun()
#                 else:
#                     st.error("Invalid username or password")
#             if st.button("New Registration"):
#                 st.session_state.page = "signup"
#                 st.rerun()
        
#         elif st.session_state.page == "signup":
#             st.subheader("Sign Up")
#             full_name = st.text_input("Full Name")
#             new_username = st.text_input("New Username")
#             new_password = st.text_input("New Password", type="password")
#             confirm_password = st.text_input("Confirm Password", type="password")
#             if st.button("Register"):
#                 if not full_name or not new_username or not new_password or not confirm_password:
#                     st.warning("Please fill in all fields before registering.")
#                 elif new_password != confirm_password:
#                     st.warning("Passwords do not match. Try again.")
#                 elif register_user(full_name, new_username, new_password):
#                     st.success("Registered successfully! Please login.")
#                     st.session_state.page = "login"
#                     st.rerun()
#                 else:
#                     st.warning("Username already exists. Try another.")
#             if st.button("Back to Login"):
#                 st.session_state.page = "login"
#                 st.rerun()
#     else:
#         if st.button("Logout"):
#             st.session_state.logged_in = False
#             st.session_state.username = ""
#             st.rerun()

# # Main Page Content
# st.title("ECG Arrhythmia Classification System")
# st.write("This app predicts the type of heartbeats based on provided ECG images.")

# st.markdown("""
#     ## Welcome to the ECG Arrhythmia Classifier
#     This application allows you to upload an ECG image and classify heartbeats into different categories.
    
#     - **Normal beats** indicate a healthy heart rhythm.
#     - **Supraventricular beats** suggest irregular heart activity in the atria.
#     - **Ventricular beats** are linked to abnormal activity in the ventricles.
#     - **Fusion beats** occur when multiple signals merge.
#     - **Unknown beats** refer to unclassified patterns.

#     Upload your ECG image and get an AI-powered prediction in seconds!
# """)

# # ECG Classification Page (Protected Page)
# if st.session_state.logged_in:
#     st.title("Upload ECG Image for Classification")
#     uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
    
#     if uploaded_file is not None:
#         file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#         image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
#         if image is not None:
#             st.image(image, caption="Uploaded Image", use_container_width=True)
#             st.write("Processing...")
#             try:
#                 input_image = preprocess_image(image)
#                 y_pred = model.predict(input_image)
#                 predicted_label = label_to_category.get(np.argmax(y_pred), "Unknown")
#                 st.success(f"Predicted Class: **{predicted_label}**")
#             except Exception as e:
#                 st.error(f"Error: {str(e)}")
#         else:
#             st.error("Error loading image. Please upload a valid file.")

# # Footer
# footer = """
#     <style>
#         .footer {
#             position: fixed;
#             bottom: 0;
#             width: 100%;
#             background-color: #222;
#             color: white;
#             text-align: center;
#             padding: 10px;
#             font-size: 14px;
#         }
#     </style>
#     <div class="footer">
#         &copy; ECG Arrhythmia Classifier. All rights reserved.
#     </div>
# """
# hide_deploy = """
#     <style>
#         button[kind="deploy"], 
#         div[data-testid="stToolbar"] { 
#             display: none !important; 
#         }
#     </style>
# """
# st.markdown(hide_deploy, unsafe_allow_html=True)
# st.markdown(footer, unsafe_allow_html=True)



import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
import sqlite3

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Ensure eager execution is enabled (TensorFlow 2.x should have it enabled by default)
if not tf.executing_eagerly():
    tf.compat.v1.enable_eager_execution()

st.set_page_config(
    page_title="ECG Arrhythmia Classifier",
    page_icon="💓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Database Setup
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def register_user(full_name, username, password):
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (full_name, username, password) VALUES (?, ?, ?)", (full_name, username, password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

def check_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

init_db()

# Load the trained model
model_path = "svm_model.h5"
if os.path.exists(model_path):
    model = load_model(model_path)
else:
    st.error(f"Model file does not exist: {model_path}")

# Label Mapping
label_to_category = {
    1: "Normal beats",
    2: "Supraventricular beats",
    3: "Unknown beats",
    4: "Ventricular beats",
    5: "Fusion beats",
}

# Preprocess Image
def preprocess_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    image = image / 255.0
    return np.expand_dims(image, axis=0)

# Sidebar Navigation with Login/Signup
with st.sidebar:
    st.sidebar.title("ECG Arrhythmia Classifier")
    
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.page = "login"
    
    if not st.session_state.logged_in:
        if st.session_state.page == "login":
            st.subheader("Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                if check_user(username, password):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("Invalid username or password")
            if st.button("New Registration"):
                st.session_state.page = "signup"
                st.rerun()
        
        elif st.session_state.page == "signup":
            st.subheader("Sign Up")
            full_name = st.text_input("Full Name")
            new_username = st.text_input("New Username")
            new_password = st.text_input("New Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            if st.button("Register"):
                if not full_name or not new_username or not new_password or not confirm_password:
                    st.warning("Please fill in all fields before registering.")
                elif new_password != confirm_password:
                    st.warning("Passwords do not match. Try again.")
                elif register_user(full_name, new_username, new_password):
                    st.success("Registered successfully! Please login.")
                    st.session_state.page = "login"
                    st.rerun()
                else:
                    st.warning("Username already exists. Try another.")
            if st.button("Back to Login"):
                st.session_state.page = "login"
                st.rerun()
    else:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.rerun()

# Display Upload Page Only After Login
if st.session_state.logged_in:
    st.title("Upload ECG Image for Classification")
    uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        if image is not None:
            st.image(image, caption="Uploaded Image", use_container_width=True)
            st.write("Processing...")
            try:
                input_image = preprocess_image(image)
                y_pred = model.predict(input_image)
                predicted_label = label_to_category.get(np.argmax(y_pred), "Unknown")
                st.success(f"Predicted Class: **{predicted_label}**")
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.error("Error loading image. Please upload a valid file.")

else:
    # Show login screen instead of main page
    st.title("Welcome to the ECG Arrhythmia Classifier")
    st.markdown("""
        
    This application allows you to upload an ECG image and classify heartbeats into different categories.
    
    - **Normal beats** indicate a healthy heart rhythm.
    - **Supraventricular beats** suggest irregular heart activity in the atria.
    - **Ventricular beats** are linked to abnormal activity in the ventricles.
    - **Fusion beats** occur when multiple signals merge.
    - **Unknown beats** refer to unclassified patterns.
    """)

# Footer
footer = """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #222;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 14px;
        }
    </style>
    <div class="footer">
        &copy; ECG Arrhythmia Classifier. All rights reserved.
    </div>
"""
hide_deploy = """
    <style>
        button[kind="deploy"], 
        div[data-testid="stToolbar"] { 
            display: none !important; 
        }
    </style>
"""
st.markdown(hide_deploy, unsafe_allow_html=True)
st.markdown(footer, unsafe_allow_html=True)
