import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import pathlib
from name import get_info

#### LOAD MODEL ####
data_dir = pathlib.Path("PokemonData/train_data")  # turn our training path into a Python path
class_names = np.array(
    sorted([item.name for item in data_dir.glob('*')]))  # created a list of class_names from the subdirectories

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(filters=10,
                           kernel_size=3,
                           activation="relu", input_shape=(200, 200, 3)),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.MaxPool2D(pool_size=2,
                              padding="valid"),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.MaxPool2D(2),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.MaxPool2D(2),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.Conv2D(10, 3, activation="relu"),
    tf.keras.layers.MaxPool2D(2),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(len(class_names), activation="softmax")
])
model.compile(loss="sparse_categorical_crossentropy",
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.0007),
              metrics=["accuracy"])
model.load_weights("model_checkpoints/cp.ckpt")

st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """,
            unsafe_allow_html=True)
st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="https://github.com/Brice-Vergnou/pokedex" target="_blank">Smart Pokedex</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Image-Based Pokedex<span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://share.streamlit.io/brice-vergnou/pokedex/name.py" >Name-Based Pokedex</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)
st.header("Pokemon classifier Analytics")
st.write("\n\n\n\n\n\n\n\n")
st.write("\n:wave:    **Welcome, here you can identify a Pokemon from a picture and quickly get some informations about it. It \
can't recognize all the Pokémons, but only the top 50 (single) in OU Gen 8. The list of these pokemons is available at the very bottom**")
st.write("\n\n\n\n\n\n\n")


def main():
    uploaded = st.file_uploader("Choose the image to recognize", type=["jpg", "jpeg"])
    st.write("\n\n\n\n\n\n\n")
    if uploaded is not None:
        image = Image.open(uploaded)
        figure = plt.figure()
        plt.imshow(image)
        plt.axis("off")
        result, prob = predict_class(image)
        c1, c2 = st.columns(2)
        with c1:
            st.write(f"🧮   With **{prob * 100:.2f}%** chance : **{result.capitalize()}**")
        with c2:
            st.pyplot(figure, width=150, use_column_width=True)
        option = st.sidebar.selectbox(
            'Which format are you interested in ?',
            ('Single', 'VGC'))
        if option == "Single":
            get_info(result, "https://www.pikalytics.com/api/p/2021-12/gen8ou-1825/")
        else:
            get_info(result, "https://www.pikalytics.com/api/p/2021-12/ss-1760/")


def predict_class(image):
    test_image = image.resize((200, 200))
    test_image = tf.keras.utils.img_to_array(test_image)
    test_image = test_image / 255
    test_image = np.expand_dims(test_image, axis=0)
    prediction = model.predict(test_image)
    score = tf.nn.softmax(prediction[0])
    score = score.numpy()
    image_class = class_names[np.argmax(score)]
    prob = prediction[0][np.argmax(score)]
    return image_class, prob


if __name__ == "__main__":
    main()
    with st.expander("List of Pokemons"):
        st.write(sorted([item.name for item in data_dir.glob('*')]))