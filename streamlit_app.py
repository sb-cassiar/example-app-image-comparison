import streamlit as st
from streamlit_image_comparison import image_comparison
import cv2

# username password

import hmac


def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if not check_password():
    st.stop()  # Do not continue if check_password is not True.


#
st.set_page_config("Experiments with Face-Swapping", "🔭")

st.header("Experiments with Face-Swapping")

st.write("")
"This is a reproduction of the fantastic [WebbCompare](https://www.webbcompare.com/index.html) app."
st.write("")

st.markdown("### Seinfeld")
image_comparison(
    img1="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/seinfeld_original.png",
    img2="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/seinfeld_new1.png",
    label1="Original",
    label2="Face-Swapped",
)

st.markdown("### Seinfeld")
image_comparison(
    img1="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/seinfeld_original.png",
    img2="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/seinfeld_new2.png",
    label1="Original",
    label2="Face-Swapped",
)

st.markdown("### Kramer with the painting")
image_comparison(
    img1="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/kramer_original.png",
    img2="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/kramer_new.png",
    label1="Original",
    label2="Swapped",
)

st.markdown("### Terminator 2 -first poster")
image_comparison(
    img1="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/t2_original1.png",
    img2="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/t2_new.png",
    label1="Original",
    label2="Swapped",
)

st.markdown("### Terminator 2 -second poster")
image_comparison(
    img1="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/t2_original2.png",
    img2="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/t2_new2.png",
    label1="Original",
    label2="Swapped",
)


