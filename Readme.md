Esse projeto extrai dados da API  https://www.exchangerate-api.com/, gera as 3 camadas da arquitetura medalhao (bronze,silver e gold), e conecta com uma API de LLM para geracao de Insights

Projeto por Carlos Jesus


✨ Funcionalidades
Ingestão (Ingest): Coleta diária de dados de cotações da API ExchangeRate-API.

Transformação (Transform): Normalização e limpeza dos dados, garantindo a qualidade e o formato adequado para análise.

Carga (Load): Armazenamento dos dados processados em formato Parquet otimizado para analytics.

Enriquecimento com LLM: Geração de resumos executivos e insights em linguagem natural sobre as variações cambiais diárias.

Logging Estruturado: Monitoramento completo do pipeline com logs detalhados para cada etapa.

Testes Unitários: Garantia de qualidade e integridade dos dados através de testes automatizados.