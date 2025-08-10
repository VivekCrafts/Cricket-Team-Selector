import os
from secret_key import api_key
os.environ['GROQ_API_KEY'] = api_key
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq

llm=ChatGroq(model="llama3-70b-8192",temperature=0.8)

# Define the prompt template
prompt = PromptTemplate(
    input_variables=["format","country","pitch","strategy"],
    template = """You are an expert cricket analyst and selector.
    select a {format} cricket team for {country} based on the pitch conditions and the team's strategy.
    the pitch is {pitch} and the strategy is {strategy}.
    Give:
    1. Full Playing XI with roles
    2. Captain and Vice-Captain
    3.Justify why this team suits the conditions.(within 80 words)"""
)
# Create the chain
team_chain = LLMChain(llm=llm,prompt=prompt)

