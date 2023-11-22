Este projeto desenvolve um chatbot simples, utilizando a API OpenAI, para auxiliar usuários na pesquisa de normas de segurança em ambientes industriais. O sistema inclui uma interface gráfica e responde de forma sucinta e clara às perguntas dos usuários.


## Características

- **API OpenAI**: Utiliza a API da OpenAI para processamento de linguagem natural.

- **Interface Gráfica**: Interface de usuário amigável desenvolvida com `gradio`.

- **Respostas Concisas**: Focado em fornecer informações específicas sobre normas de segurança industrial.


## Pré-Requisitos

- Python 3.6 ou superior

- Acesso à API da OpenAI

- Bibliotecas: `openai`, `langchain`, `gradio` (instaláveis via pip)


## Instalação

Para instalar as bibliotecas necessárias, execute:

```bash
pip install openai langchain gradio
```


## Uso

1. Clone o repositório ou baixe os arquivos do projeto.

```bash
git clone https://github.com/danielquintaos/mod8-pon4
```

2. Substitua 'your_api_key' pela sua chave API da OpenAI no script do chatbot.

3. Execute o script Python para iniciar a interface do chatbot.

```
python app.py
```


## Interface

Após a execução, uma interface gráfica será aberta no navegador. Os usuários podem digitar suas perguntas relacionadas a normas de segurança industrial e receber respostas instantâneas.


## Segurança e Limites

- Mantenha sua chave API segura e não a exponha no código.

- Esteja ciente dos limites de uso da API OpenAI para evitar cobranças excessivas.


## Personalização

O sistema pode ser customizado para atender a diferentes necessidades, ajustando o prompt do sistema, a interface gráfica, e o comportamento de resposta.


## Demonstração

Vídeo: https://youtu.be/MJDN83N6YdI