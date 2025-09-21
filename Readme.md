Esse projeto extrai dados da API  https://www.exchangerate-api.com/, gera as 3 camadas da arquitetura medalhao (bronze,silver e gold), e conecta com uma API de LLM para geracao de Insights

Projeto por Carlos Jesus


✨ Funcionalidades
Ingestão (Ingest): Coleta diária de dados de cotações da API ExchangeRate-API.

Transformação (Transform): Normalização e limpeza dos dados, garantindo a qualidade e o formato adequado para análise.

Carga (Load): Armazenamento dos dados processados em formato Parquet otimizado para analytics.

Enriquecimento com LLM: Geração de resumos executivos e insights em linguagem natural sobre as variações cambiais diárias.

Logging Estruturado: Monitoramento completo do pipeline com logs detalhados para cada etapa.

***
🛠️ Tecnologias Utilizadas
Linguagem: Python 3.9+

Bibliotecas Principais:

requests: Para requisições HTTP à API.

pandas: Para manipulação e transformação de dados.

pyarrow: Para escrita de arquivos em formato Parquet.

python-dotenv: Para gerenciamento de variáveis de ambiente.

openai: Para integração com a API do ChatGPT ou outro LLM.

pytest: Para execução de testes unitários.

structlog ou logging: Para logging estruturado.

Ferramentas:

Git & GitHub: Para versionamento de código.