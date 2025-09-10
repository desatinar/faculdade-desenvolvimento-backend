# Projeto Diabetes – Análise de Pacientes e Consultas

## Descrição  
Este projeto tem como objetivo manipular e analisar dados relacionados a pacientes e consultas médicas associadas ao diabetes.  
A partir do arquivo `diabetes_id.csv`, foram geradas duas novas tabelas com auxílio de **Inteligência Artificial**:  

- `pacientes.csv` → contendo **300+ registros** simulados de pacientes;  
- `consultas.csv` → contendo **300+ registros** simulados de consultas.  

Além disso, o projeto responde às questões propostas no arquivo `diabetes_perguntas.txt`, utilizando análise de dados sobre as bases criadas.  

> **Nota:** O arquivo de banco de dados `.db` foi adicionado diretamente ao repositório para simplificação do projeto.  
> Embora não seja uma boa prática (já que bancos de dados podem crescer rápido e dificultar o versionamento), essa abordagem foi adotada aqui para atender aos requisitos da atividade.  

---

## Estrutura do Projeto  

```bash
projeto-diabetes
 ┣ data
 ┃ ┣ diabetes_id.csv
 ┃ ┣ pacientes.csv
 ┃ ┣ consultas.csv
 ┃ ┗ clinica.db
 ┣ src
 ┃ ┣ __init__.py
 ┃ ┣ setup.py          # gera o banco a partir dos CSVs
 ┃ ┣ query.py          # executa queries no banco SQLite
 ┃ ┗ utils.py          # funções auxiliares (se precisar)
 ┣ docs
 ┃ ┗ diabetes_perguntas.docx
 ┣ queries
 ┃ ┗ query.sql         # arquivo com consultas SQL
 ┣ README.md
 ┗ requirements.txt

