import streamlit as st
from openai import OpenAI
import os

from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 从环境变量加载 API 密钥
api_key = os.getenv("OPENAI_API_KEY")

# 初始化 OpenAI 客户端
client = OpenAI(api_key=api_key)

# 页面标题
st.set_page_config(page_title="Dish Recommender", layout="wide")
st.title("AI-Powered Dish Recommender")

# 检查是否有收藏的餐厅
if "favorites" not in st.session_state or not st.session_state.favorites:
    st.write("You haven't added any favorites yet. Go back and add some!")
else:
    st.write("### Recommended Dishes for Your Favorite Restaurants")

    # 函数：为餐厅生成推荐菜品
    def recommend_dishes(restaurant_name, cuisine_type):
        try:
            # 生成推荐的 Prompt
            prompt = f"""
            I have a restaurant named '{restaurant_name}', specializing in {cuisine_type}. 
            Suggest three unique and popular dishes for this restaurant, with a short description for each dish.
            """

            # 调用 OpenAI API
            response = client.chat.completions.create(model="gpt-3.5-turbo",  # 使用 GPT-3.5 或其他可用模型
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7)

            # 提取推荐结果
            recommendations = response.choices[0].message.content.strip()
            return recommendations
        except Exception as e:
            return f"Error generating recommendations: {str(e)}"

    # 遍历收藏的餐厅，为每个餐厅生成推荐菜品
    for favorite in st.session_state.favorites:
        st.subheader(f"{favorite['Name']}")

        # 用户自定义餐厅类型（如中餐、法餐等）
        cuisine_type = st.text_input(f"Specify the cuisine type for {favorite['Name']}", key=f"cuisine-{favorite['Name']}")

        # 推荐按钮
        if st.button(f"Get Recommendations for {favorite['Name']}", key=f"recommend-{favorite['Name']}"):
            if cuisine_type:
                with st.spinner("Generating recommendations..."):
                    recommendations = recommend_dishes(favorite['Name'], cuisine_type)
                    st.write(f"### Recommended Dishes for {favorite['Name']}")
                    st.write(recommendations)
            else:
                st.warning("Please specify the cuisine type before generating recommendations.")
