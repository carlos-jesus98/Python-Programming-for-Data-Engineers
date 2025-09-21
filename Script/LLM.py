import google.generativeai as genai
import yaml 
import os
from IPython.display import display, Markdown
import pandas as pd
from pathlib import Path
import logging


class LLM:
        
        def gen_ia(self,chave_ia):
            genai.configure(api_key=chave_ia)
            model = genai.GenerativeModel('gemini-2.5-pro')
            prompt = f"Aja como um consultor financeiro preparando um resumo para um executivo que não tem tempo a perder. Use os dados abaixo para responder de forma clara e direta à seguinte pergunta: Explique em termos simples como está a variação das 5 principais moedas frente ao Dolar hoje."
            
            response = model.generate_content(prompt)
            print(response.text )            
            logging.info("Conexao e prompit enviado com sucesso a LLM.")