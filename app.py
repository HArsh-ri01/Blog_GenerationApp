import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


## Function To get response from the LLAma 2 model

def getLLamaresponse(input_text, no_of_words, blog_type):

    ### LLama 2 Model
    llm = CTransformers(model="model\llama-2-7b.ggmlv3.q8_0.bin", model_type="llama", config={"max_new_tokens": 500, 
    "temperature": 0.01})


    ## prompt Template
    template="""
    write a blog for {blog_type} job profile for a topic {input_text} within {no_of_words} words.
    """

    prompt = PromptTemplate(input_variables=["blog_type","input_text","no_of_words"],template=template)

    ## Generate the response from the LLama 2 model
    response = llm(prompt.format(blog_type=blog_type, input_text=input_text, no_of_words=no_of_words))

    print(response)
    return response

st.set_page_config(page_title="Generate Blogs", 
                   page_icon="🦙", 
                   layout="centered", 
                   initial_sidebar_state="collapsed")

st.header("Generate Blog Posts 🦙")

input_text = st.text_input("Enter the Blog Tilte")

col1, col2 = st.columns([5,5])

with col1:
    no_of_words=st.text_input("Enter the number of words")
with col2:
    blog_type=st.selectbox("Select the Blog Type", ["Technology", "Health", "Finance", "Travel", "Food", "Fashion", "Sports", "Entertainment", "Education", "Science", "Business", "Marketing", "Lifestyle", "Researchers","Data Science","Psychology","Other"], index=0)

Submit=st.button("Generate Blog")

## Final response

if Submit:
    st.write(getLLamaresponse(input_text, no_of_words, blog_type))
