from Script.Extract import Extract
from Script.Refined import Refined
from Script.Trusted import Trusted
import yaml 

with open(r".\YAML\config.yaml","r") as file:
            config=yaml.safe_load(file)
            api_key = config["api_key"]

extract = Extract()
refined = Refined()
trusted = Trusted()
moeda = "USD"

extract.resultado_api(moeda,api_key)

raw_data = refined.json_read(moeda)

refined.trans_json(raw_data)
trusted.Refinamento(moeda)  