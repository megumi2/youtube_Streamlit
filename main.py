import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image #画像を読み込みたいときに使う
import time

st.title('Streamlit 超入門')

st.write('DataFrame')

#df = pd.DataFrame({
#    '1列目':[1, 2, 3, 4],
#    '2列目':[10, 20, 30, 40]
#})

"""
# 章
## 節
### 項
```python
    import streamlit as st
    import numpy as nm
    import pandas as pd
```
"""
#　表を作成
#st.dataframe(df.style.highlight_max(axis=0))　←ソートできる
#st.table(df.style.highlight_max(axis=0)) # ←ソートできない
#st.dataframeは表の高さと幅を設定することができる
#f.style.highlight_max　大きな数値にハイライトをつける列を指定→０、行を指定→１

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns = ['lat','lon']
)
#np.random.rand(100, 2) →縦に20,横に3つランダムな乱数を出す
#np.random.rand(100, 2)/[50, 50] + [35.69, 139.70]
#35.69付近のランダムな乱数を出す　139.70付近のランダムな乱数を出す
#map 
st.map(df)

#line_chart,bar_chartなどいろいろある

st.write('Display_Image')

#img = Image.open('gogyo.jpg')
#st.image(img, caption='Kohei Imanishi', use_column_width=True)
#画像を表示させる
#use_column_width:Webサイトのカラムに会わせて表示させる

#if st.checkbox('Show Image'):
#    img = Image.open('gogyo.jpg')
#    st.image(img, caption='Kohei Imanishi', use_column_width=True)
#チェックボックスにチェックが入ったら画像が表示される

#option = st.selectbox('あなたが好きな数字を教えて下さい',
#     list(range(1, 11))
#)

#'あなたの好きな数字は', option, 'です。'
#"""
#'''
#option = st.text_input('あなたの趣味を教えて下さい')
#'あなたの趣味は', option, 'です。'

#text_input テキストの入力欄を表示させる
#
#condition = st.slider('あなたの今の調子は', 0, 100, 50)
#'コンディション', condition

#option = st.sidebar.text_input('あなたの趣味を教えて下さい')
#'あなたの趣味は', option, 'です。'

#condition = st.sidebar.slider('あなたの今の調子は', 0, 100, 50)
#'コンディション', condition

#プログレスバーの表示
'Start'
#空の要素を追加
latest_iteration = st.empty()

bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
#fストリング：値を直接文字に埋め込む
    bar.progress(i + 1)
    time.sleep(0.1)
#time.sleep(i)処理をi秒間ストップさせる
'Done'

left_column, right_column = st.beta_columns(2)#3にすれば３カラムになる
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')
#ボタンがtrueになったら（ボタンがおされたら文字を表示）
#option = st.text_input('あなたの趣味を教えて下さい')
#あなたの趣味は', option, 'です。'

#condition = st.slider('あなたの今の調子は', 0, 100, 50)
#'コンディション', condition

#2カラムにする







