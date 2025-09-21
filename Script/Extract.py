import requests
import json
import yaml  
import logging
from pathlib import Path
from datetime import datetime


class Extract:
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s', 
        filename='Log.log', 
        encoding='utf-8', 
        filemode='a'
    )

    logging.info("Script iniciado. Tentando carregar as configurações.")
    try:
        with open(r"C:\Users\Carlos Vinicius\Documents\Impacta\Aulas\Python Programming for Data Engineers v2\YAML\config.yaml","r") as file:
            config=yaml.safe_load(file)
            api_key = config["api_key"]
            logging.info("Arquivo de configuração 'config.yaml' carregado com sucesso.")
    except KeyError:
        logging.critical("A chave 'api_key' não foi encontrada no 'config.yaml'. O programa será encerrado.")
    

    base_currency = "USD"
    #logging.debug(f"URL da API construída: {url}")
    #output_dir2 = r"C:\Users\Carlos Vinicius\Documents\Impacta\Aulas\Python Programming for Data Engineers v2\Raw"
    #output_dir = Path(output_dir2)
    
    def resultado_api(self,moeda,chave_api):
        url = f"https://v6.exchangerate-api.com/v6/{chave_api}/latest/{moeda}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()

            if data.get("result") == "success":
                logging.error(f"Conectado com sucesso")
                try:
                    timestamp = datetime.now().strftime("%Y%m%d")
                    filename = f"api_response_{moeda}_{timestamp}.json"
                    output_dir2 = r"C:\Users\Carlos Vinicius\Documents\Impacta\Aulas\Python Programming for Data Engineers v2\Raw"
                    output_dir = Path(output_dir2)
                    full_path = output_dir / filename
                
                    with open(full_path, 'w', encoding='utf-8') as json_file:
                        json.dump(data, json_file, indent=4, ensure_ascii=False)
                    logging.info(f"Dados salvos com sucesso em '{filename}'.")
                except Exception as e:
                    logging.error(f"Ocorreu um erro ao tentar salvar o arquivo JSON: {e}")
            else:
                logging.error(f"Error na API")
        except KeyError as e:
            logging.warning(f"A moeda {e} não foi encontrada nas taxas de conversão retornadas.")
    logging.info("Script finalizado.")