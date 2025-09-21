from Script.Extract import Extract
from Script.Refined import Refined
from Script.Trusted import Trusted
from Script.LLM import LLM
import yaml 

with open(r".\YAML\config.yaml","r") as file:
            config=yaml.safe_load(file)
            api_key = config["api_key"]
            ai_key = config["ai_key"]

extract = Extract()
refined = Refined()
trusted = Trusted()
llm = LLM()
moeda = "USD"

extract.resultado_api(moeda,api_key)

raw_data = refined.json_read(moeda)

refined.trans_json(raw_data)
trusted.Refinamento(moeda)
#print(ai_key)

retorno = llm.gen_ia(ai_key)
print(retorno)