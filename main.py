import streamlit as st  
from google import genai
def inicializar_cliente():
   return genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    vertexai=True
cliente = inicializar_cliente()
test1='IAmiga'
st.title(test1) 
if not "lista-mensagens" in st.session_state:
    st.session_state['lista-mensagens']=[]
solicitação = st.chat_input('o que tu manda meu chapa?')
for mensagem in st.session_state['lista-mensagens']:
   role=mensagem['role']
   content=mensagem['content']
   st.chat_message(role).write(content)
if solicitação:
   st.chat_message('user').write(solicitação)
   mensagem_usuario={'role': 'user', 'content': solicitação}
   st.session_state['lista-mensagens'].append(mensagem_usuario)
   respostaia=cliente.models.generate_content(model='gemini-2.5-flash', contents=solicitação)
   respostadef= respostaia.text
   st.chat_message('assistant').write(respostadef)
   mensagem_assistente={'role': 'assistant', 'content': respostadef}
   st.session_state['lista-mensagens'].append(mensagem_assistente)
