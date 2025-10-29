import streamlit as st
import random
from streamlit.components.v1 import html

# 页面配置
st.set_page_config(page_title="漂浮文字", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    .stApp {margin: 0; padding: 0;}
    .float-text {position: absolute; color: pink; font-family: 楷体; font-size: 45px;}
    </style>
""", unsafe_allow_html=True)

# 生成漂浮文字的HTML+JS
def float_text_html():
    texts = ["我爱你♥"] * 200  # 对应原200个弹窗的效果
    html_content = "<div id='float-container' style='position: fixed; top:0; left:0; width:100vw; height:100vh;'>"
    for idx, text in enumerate(texts):
        # 随机初始位置
        x = random.randint(0, 95)
        y = random.randint(0, 95)
        html_content += f"""
        <div class='float-text' id='text-{idx}' style='left:{x}vw; top:{y}vh;'>
            {text}
        </div>
        """
    # JS实现漂浮动画
    html_content += """
    <script>
    const texts = document.querySelectorAll('.float-text');
    setInterval(() => {
        texts.forEach(text => {
            // 随机移动
            const x = parseFloat(text.style.left) + (Math.random() - 0.5) * 4;
            const y = parseFloat(text.style.top) + (Math.random() - 0.5) * 4;
            // 限制在视口内
            text.style.left = Math.max(0, Math.min(95, x)) + 'vw';
            text.style.top = Math.max(0, Math.min(95, y)) + 'vh';
        });
    }, 100);
    </script>
    </div>
    """
    return html_content

# 渲染漂浮文字
html(float_text_html(), height=800, width=1200)