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

st.image("https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/CASSIAR_v02_small.png")
st.header("Cassiar AI Labs Demo Site")

st.write("")
"Welcome!"
st.write("")
st.write("This is a demo site created to showcase our advances in the field of image  and video processing using the newest AI techniques - developed here at the labs.")


st.markdown("### Kramer with the painting")
image_comparison(
    img1="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/kramer_original.png",
    img2="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/kramer_new.png",
    label1="Original",
    label2="Swapped",
)

st.markdown("### Example 1")
image_comparison(
    img1="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/1-input.jpg",
    img2="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/1-output.png",
    label1="Original",
    label2="Face-Swapped",
)

st.markdown("### Example 2")
image_comparison(
    img1="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/2-input.jpg",
    img2="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/2-output.png",
    label1="Original",
    label2="Face-Swapped",
)


st.markdown("### Example 3")
image_comparison(
    img1="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/3-input.jpg",
    img2="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/3-output.png",
    label1="Original",
    label2="Swapped",
)

st.markdown("### Example 4")
image_comparison(
    img1="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/4-input.jpg",
    img2="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/4-output.png",
    label1="Original",
    label2="Swapped",
)


st.markdown("### Example 5")
image_comparison(
    img1="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/5-input.jpg",
    img2="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/5-output.png",
    label1="Original",
    label2="Swapped",
)

st.markdown("### Example 6")
image_comparison(
    img1="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/6-input.jpg",
    img2="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/6-output.png",
    label1="Original",
    label2="Swapped",
)

