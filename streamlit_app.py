import streamlit as st
from streamlit_image_comparison import image_comparison
import cv2


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


