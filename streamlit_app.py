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
st.set_page_config("Cassiar AI Labs Demo", "🔭")

st.image("https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/CASSIAR_v02_small.png")
st.header("Cassiar AI Labs Demo Site")

# st.markdown('##AI Labs')
st.write("Welcome!")
st.write("This is a demo site created to showcase our advances in the field of image  and video processing using the newest AI techniques - developed here at the labs.")
st.write("We love working with visual media - images and videos, and we have categorize them into: Faces, Architecture and Landscapes")
# st.write("")
st.image("https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/AI Labs.png")


st.markdown("### FaceMagic")
st.write("Let us begin with our AI Labs app - FaceMagic, aimed at simplifying and speeding the high quality image and video generation in face swapping.")
# st.write("")
st.image("https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/facemagic placeholder1.png")


st.write("")




st.write("FaceMagic uses reference faces, source media to swap faces with and a number of settings and parameters for the artist to change")
st.write("Here is an example of how the FaceMagic works closely with the artist, giving them the full control over image generation and image quality.")
st.image("https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/Karan-CH1.png")




st.write("## Other examples")

st.write("Example 1")
image_comparison(
    img1="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/kramer_original.png",
    img2="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/kramer_new.png",
    label1="Original",
    label2="Swapped",
)

st.write("Example 2")
image_comparison(
    img1="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/1-input.jpg",
    img2="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/1-output.png",
    label1="Original",
    label2="Face-Swapped",
)

st.write("Example 3")
image_comparison(
    img1="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/2-input.jpg",
    img2="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/2-output.png",
    label1="Original",
    label2="Face-Swapped",
)


st.write("Example 4")
image_comparison(
    img1="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/3-input.jpg",
    img2="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/3-output.png",
    label1="Original",
    label2="Swapped",
)

st.write("Example 5")
image_comparison(
    img1="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/4-input.jpg",
    img2="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/4-output.png",
    label1="Original",
    label2="Swapped",
)


st.write("Example 6")
image_comparison(
    img1="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/5-input.jpg",
    img2="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/5-output.png",
    label1="Original",
    label2="Swapped",
)

st.write("Example 7")
image_comparison(
    img1="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/6-input.jpg",
    img2="https://sampleimgstorewestus2.blob.core.windows.net/sampleimgs/6-output.png",
    label1="Original",
    label2="Swapped",
)

# st.write("FaceMagic also works with videos. Here are some of the examples of videos before and after")
# st.video()

