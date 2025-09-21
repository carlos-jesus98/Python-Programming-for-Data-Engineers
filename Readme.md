Esse projeto extrai dados da API  https://www.exchangerate-api.com/, gera as 3 camadas da arquitetura medalhao (bronze,silver e gold), e conecta com uma API de LLM para geracao de Insights

Projeto por Carlos Jesus


✨ Funcionalidades
**Ingestão (Ingest):** Coleta diária de dados de cotações da API ExchangeRate-API.

**Transformação (Transform):** Normalização e limpeza dos dados, garantindo a qualidade e o formato adequado para análise.

**Carga (Load):** Armazenamento dos dados processados em formato Parquet otimizado para analytics.

**Enriquecimento com LLM:** Geração de resumos executivos e insights em linguagem natural sobre as variações cambiais diárias.

**Logging Estruturado:** Monitoramento completo do pipeline com logs detalhados para cada etapa.

***
🛠️ Tecnologias Utilizadas
Linguagem: Python 3.9+

**Bibliotecas Principais:**

**requests:** Para requisições HTTP à API.

**pandas:** Para manipulação e transformação de dados.

**yaml:** Para captura das principais keys com seguranca.

**logging:** Para gerar logs de execucao e controle.

**google.generativeai:** Para conexao com o Gemini.

**Ferramentas:**

**Git & GitHub:** Para versionamento de código.

***

📂 Estrutura do Projeto
O projeto está organizado da seguinte forma para garantir a separação de responsabilidades e a clareza do pipeline:

/
├── src/
│   ├── LLM.py                  # Script de enriquecimento com LLM               
|   ├── Extract.py              # Script de coleta de dados
|   ├── Refined.py              # Script de normalização
|   ├── Trusted.py              # Script de carga para Parquet
├── main.py                     # Orquestrador do pipeline (opcional)
├── Raw/
├── Trusted/
├── Refined/
├── Log.log                     # Log de execucoes
├── .gitignore
└── README.md