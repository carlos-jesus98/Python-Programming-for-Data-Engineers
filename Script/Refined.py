import pandas as pd
import logging
import yaml  
import os
import json
from datetime import datetime
from pathlib import Path


class Refined:
       
    trusted = r"C:\Users\Carlos Vinicius\Documents\Impacta\Aulas\Python Programming for Data Engineers v2\Trusted"
    trusted_path = Path(trusted)

    def json_read(self,moeda):
        timestamp = datetime.now().strftime("%Y%m%d")
        filename = f"api_response_{moeda}_{timestamp}.json"
        path = r"C:\Users\Carlos Vinicius\Documents\Impacta\Aulas\Python Programming for Data Engineers v2\Raw"
        output_dir = Path(path)  
        
        full_path = output_dir / filename
        with open(full_path,'r', encoding='utf-8') as arquivo:
            raw_data = json.load(arquivo)
        return raw_data
    
    def trans_json(self,entrada):
        base_currency = entrada.get("base_code")
        conversion_rates = entrada["conversion_rates"]
        timestamp = entrada.get("time_last_update_unix")
        trusted = r"C:\Users\Carlos Vinicius\Documents\Impacta\Aulas\Python Programming for Data Engineers v2\Trusted"
        trusted_path = Path(trusted)
        raw = []
        for currency, rate in conversion_rates.items():
            raw.append({
                "base_currency": base_currency,
                "target_currency": currency,
                "rate": rate,
                "timestamp": timestamp
            })
        df = pd.DataFrame(raw)
        df = df[df["rate"] > 0]
        truste_file = f"{base_currency}.csv"
        trusted_file_path = trusted_path / truste_file
        df.to_csv(trusted_file_path,sep='|')
