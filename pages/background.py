import streamlit as st
import mimetypes
from streamlit import runtime
from streamlit.runtime import caching

image = './files/cat_background.jpg'
image_id = 'please_do_not_crash'

# Copied from Streamlit's implementation of st.image
def serve_image(image, image_id):
    mimetype, _ = mimetypes.guess_type(image)
    if mimetype is None:
        mimetype = "application/octet-stream"
    url = runtime.get_instance().media_file_mgr.add(image, mimetype, image_id)
    caching.save_media_data(image, mimetype, image_id)
    return(url)

url = serve_image(image, image_id)

css = f'''
.stApp {{
    background-image: url(.{url});
}}
.stApp > header {{
    background-color: transparent;
}}
'''
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.write('<div style="background-color: grey; font-size: 3em">Image attribution:<br />' \
    '<a href="https://www.vecteezy.com/vector-art/5298806-seamless-pattern-of-cute-cartoon-cat-illustration-design-on-purple-background">Artwork by psmxp</a><br/>' \
    '<a href="https://www.vecteezy.com/free-vector/cat-pattern">Cat Pattern Vectors by Vecteezy</a></div>',unsafe_allow_html=True)

