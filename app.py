from openai import OpenAI
import streamlit as st 

f = open('keys/.openai_api_key.txt')
OPENAI_API_KEY = f.read()
client = OpenAI(api_key = OPENAI_API_KEY)

# Custom CSS styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #e8d8a9;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #000080;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover{
    background-color :  #09704a;
    }
    .stTextInput>div>div>textarea{
    overflow-y:hidden;
    resize: none;
    transition: height o.3s;
    color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='color:black;'>💭AI Code Reviewer</h1>", unsafe_allow_html=True)
st.subheader("⌨📝")

prompt = st.text_area("Enter a code to review the code!!",height=100, key="textarea") 

if st.button("Generate") == True:

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": """You are a solving assistant working with a company to fix the bugs in the code. 
                                            Your job here is to help the colleagues fix there code.
                                            You are know to be polite and helpful AI bot. 
                                            If the doubt is not related to fixing bug from code you can politely ask the user another doubt.
                                            """},
                                            
                            {"role": "user", "content": prompt}
                        ]
    )

    st.write (response.choices[0].message.content)