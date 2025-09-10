-- 1.Quais são as tabelas disponíveis no banco de dados atual?
SELECT * FROM sqlite_master WHERE type='table';

--2. Quais são os primeiros 10 registros da tabela pacientes?
SELECT * FROM pacientes LIMIT 10;

--3. Quais são os nomes e tipos de dados das colunas da tabela pacientes?
PRAGMA table_info(pacientes);

--4. Quantos pacientes foram diagnosticados com diabetes e quantos não foram?
