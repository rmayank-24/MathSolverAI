import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv
from langchain.callbacks import StreamlitCallbackHandler
from langchain_google_genai import ChatGoogleGenerativeAI

# Set up Streamlit App
st.set_page_config(page_title="Text to Math Problem Solver and Data Search Assistant", page_icon="🧮")
st.title("🧮 Text to Math Problem Solver Using Google Gemini")

# Sidebar: Input Google API Key
google_api_key = st.sidebar.text_input(label="🔑 Enter your Google API Key", type="password")

# Check if key is provided
if not google_api_key:
    st.info("Please add your Google API key to continue.")
    st.stop()

# Initialize Google Gemini-Pro LLM with user-provided key
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
,
    temperature=0.7,
    top_p=1,
    max_output_tokens=1024,
    google_api_key=google_api_key  # ✅ Using user input here
)

# Wikipedia Tool
wiki = WikipediaAPIWrapper()
wiki_tool = Tool(
    name="Wikipedia",
    func=wiki.run,
    description="Useful for searching the internet for general knowledge and topics."
)

# Math Tool using LLMMathChain
math_chain = LLMMathChain.from_llm(llm=llm)
calculator = Tool(
    name="Calculator",
    func=math_chain.run,
    description="Solves math problems based on input expressions."
)

# Custom Reasoning Prompt
prompt = """
You are an AI agent designed to solve mathematical and reasoning questions step-by-step.
Carefully analyze the question and present a detailed explanation in bullet points.

Question: {question}
Answer:
"""

prompt_template = PromptTemplate(
    input_variables=["question"],
    template=prompt
)

# Reasoning Tool
reasoning_chain = LLMChain(llm=llm, prompt=prompt_template)
reasoning_tool = Tool(
    name="Reasoning Tool",
    func=reasoning_chain.run,
    description="Handles reasoning and step-by-step problem-solving questions."
)

# Initialize the Agent with all tools
assistant_agent = initialize_agent(
    tools=[wiki_tool, calculator, reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

# Store Chat History
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi! I'm a math chatbot. Ask me anything related to calculations or general topics."}
    ]

# Display Chat History
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User Input
question = st.text_area("📝 Enter your question:", value="I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries. Each pack of blueberries contains 25 berries. How many total pieces of fruit do I have at the end?")

# Process on Button Click
if st.button("🔍 Find My Answer"):
    if question.strip():
        with st.spinner("Generating response..."):
            st.session_state.messages.append({"role": "user", "content": question})
            st.chat_message("user").write(question)

            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = assistant_agent.run(st.session_state.messages, callbacks=[st_cb])

            st.session_state.messages.append({"role": "assistant", "content": response})
            st.chat_message("assistant").write(response)
            st.success("✅ Answer generated successfully!")
    else:
        st.warning("⚠️ Please enter a valid question.")
