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
 ┣ docs
 ┃ ┗ diabetes_perguntas.docx
 ┣ queries
 ┃ ┗ query.sql         # arquivo com consultas SQL
 ┣ README.md
 ┗ requirements.txt
```

## Relatório dos Dados  

O banco de dados possui 3 tabelas principais:  
- consultas  
- pacientes  
- diabetes_id  

### Tabela pacientes  
Colunas:  
- id (INTEGER)  
- nome (TEXT)  
- sexo (TEXT)  
- data_nascimento (TEXT)  
- cidade (TEXT)  
- bairro (TEXT)  

Exemplos de registros iniciais:  
- Brenda Alves (Jaboatão, 1995-02-24)  
- Joaquim Câmara (Olinda, 1954-03-08)  
- Igor Montenegro (Recife, 1985-08-27)  

---

### Estatísticas Gerais  
- Pacientes diagnosticados com diabetes: 52  
- Pacientes sem diabetes: 85  
- Média de glicose registrada: ~118,11  

---

### Distribuição por Cidade e Sexo  
- Recife → 57 pacientes femininos  
- Olinda → 25  
- Paulista → 17  
- Carpina → 14  
- Caruaru → 13  
- Jaboatão → 13  
- Petrolina → 13  

---

### Observações  
- A cidade de Recife concentra a maior parte dos pacientes, incluindo nomes como Igor Montenegro, Mariana Silva e Sandra Oliveira.  
- A relação entre pacientes e consultas pode ser detalhada com queries específicas.  

---