import pandas as pd
from pathlib import Path

class Trusted:

    def Refinamento(self,moeda):
        trusted = r"C:\Users\Carlos Vinicius\Documents\Impacta\Aulas\Python Programming for Data Engineers v2\Trusted"
        refined = r"C:\Users\Carlos Vinicius\Documents\Impacta\Aulas\Python Programming for Data Engineers v2\Refined"
        trusted_path = Path(trusted)
        refined_path = Path(refined)
        truste_file_csv = f"{moeda}.csv"
        truste_file_parquet = f"{moeda}.parquet"
        trusted_file_path_csv = trusted_path / truste_file_csv
        trusted_file_path_parquet = refined_path / truste_file_parquet

        df = pd.read_csv(trusted_file_path_csv,sep="|")
        df.to_parquet(trusted_file_path_parquet)