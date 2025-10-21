Automação Power BI

Este projeto automatiza o processo de geração de relatórios no Power BI a partir de dados extraídos de fontes específicas. A automação facilita a atualização e a distribuição de relatórios, economizando tempo e reduzindo erros manuais.

Funcionalidades

Extração de Dados: Coleta dados de fontes configuradas.

Transformação de Dados: Aplica transformações necessárias para análise.

Geração de Relatórios: Cria relatórios no Power BI com base nos dados processados.

Agendamento: Permite agendar a execução automática do processo.

Tecnologias Utilizadas

Python: Linguagem principal para automação.

Power BI: Ferramenta de visualização de dados.

Git: Controle de versão do código-fonte.

Pré-requisitos

Python 3.8 ou superior

Bibliotecas Python listadas em requirements.txt

Power BI instalado e configurado

Instalação

Clone o repositório:

git clone https://github.com/Luix3005/automacao-powerbi.git
cd automacao-powerbi


Crie e ative um ambiente virtual:

python -m venv venv
.\venv\Scripts\activate  # No Windows
source venv/bin/activate  # No Linux/Mac


Instale as dependências:

pip install -r requirements.txt


Configure as fontes de dados e agendamentos conforme necessário.

Como Usar

Execute o script principal:

python main.py


Para agendar a execução, utilize ferramentas como o Agendador de Tarefas do Windows ou cron no Linux.

Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.