import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 基礎')
st.write('Hello World!')

# データフレームの準備
df = pd.DataFrame({
    '1列目' : [1, 2, 3, 4],
    '2列目' : [10, 20, 30, 40]
})

# 動的なテーブル
st.dataframe(df)

# 引数を使用した動的テーブル
st.dataframe(df.style.highlight_max(axis = 0) , width = 100 , height = 150)

# Pillow
from PIL import Image

# 画像の読み込み
img = Image.open('iris.jpg')
st.image(img,caption = 'Iris' , use_column_width = True)
