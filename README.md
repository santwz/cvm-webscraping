# Consulta de Ativos da CVM

Este projeto utiliza o Selenium para automatizar a consulta de informações de ativos no site da CVM (Comissão de Valores Mobiliários do Brasil). Ele lê códigos de ativos a partir de um arquivo `codigos.txt`, realiza as consultas no site da CVM, salva e exporta para um arquivo Excel.


## Requisitos

- Python 3.x
- Selenium
- Pandas
- geckodriver (para Firefox)

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/santwz/cvm-webscraping.git
    cd cvm-webscraping
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Certifique-se de que o `geckodriver` está instalado e disponível no PATH. Você pode baixar o `geckodriver` [aqui](https://github.com/mozilla/geckodriver/releases).

## Uso

1. Adicione os códigos dos ativos que você deseja consultar no arquivo `codigos.txt`, com um código por linha:
    ```text
    PETR4
    VALE3
    BPAC11
    ABEV3
    ```

2. Execute o script:
    ```bash
    python consulta_cvm.py
    ```

3. O script irá gerar um arquivo `resultado_consulta.xlsx` com os resultados das consultas.

## Estrutura do Projeto

```plaintext
cvm-webscraping/
│
├── codigos.txt          # Arquivo de entrada com os códigos dos ativos
├── consulta_cvm.py      # Script principal de consulta
├── resultado_consulta.xlsx  # Arquivo de saída com os resultados
├── requirements.txt     # Arquivo de dependências
└── README.md            # Este arquivo
