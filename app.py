import streamlit as st
import base64

# --- Login Page ---
def login_page():
    st.title("Login to Dashboard")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
            st.rerun()  # Updated: Using st.rerun()
        else:
            st.error("Invalid username or password")

# --- Dashboard with File Uploader ---
def dashboard():
    st.title("Dashboard")
    st.write("Welcome, admin!")

    st.header("File Uploader")
    uploaded_file = st.file_uploader("Upload any file (PDF, Image, Word, etc.)", type=None)

    if uploaded_file is not None:
        st.success("File uploaded successfully!")
        st.write(f"File Name: {uploaded_file.name}")
        st.write(f"File Type: {uploaded_file.type}")

        # Display content based on file type
        if uploaded_file.type.startswith('image'):
            st.image(uploaded_file, caption=f"Uploaded Image: {uploaded_file.name}", use_column_width=True)
        elif uploaded_file.type == 'application/pdf':
            st.subheader("PDF File")
            # To allow download, you can create a base64 encoded link
            base64_pdf = base64.b64encode(uploaded_file.read()).decode('utf-8')
            pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="500" type="application/pdf">'
            st.markdown(pdf_display, unsafe_allow_html=True)
            st.download_button(
                label="Download PDF",
                data=uploaded_file,
                file_name=uploaded_file.name,
                mime="application/pdf"
            )
        else:
            st.subheader("Other File Type")
            st.write("Streamlit does not directly render all file types.")
            st.download_button(
                label=f"Download {uploaded_file.name}",
                data=uploaded_file,
                file_name=uploaded_file.name,
                mime=uploaded_file.type
            )

    st.markdown("---")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun() # Updated: Using st.rerun()

# --- Main Application Logic ---
def main():
    # Initialize session_state.logged_in if it doesn't exist
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        dashboard()
    else:
        login_page()

if __name__ == "__main__":
    main()