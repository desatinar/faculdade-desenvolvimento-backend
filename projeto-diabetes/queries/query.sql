-- 1.Quais são as tabelas disponíveis no banco de dados atual?
SELECT * FROM sqlite_master WHERE type='table';

--2. Quais são os primeiros 10 registros da tabela pacientes?
SELECT * FROM pacientes LIMIT 10;

--3. Quais são os nomes e tipos de dados das colunas da tabela pacientes?
PRAGMA table_info(pacientes);

--4. Quantos pacientes foram diagnosticados com diabetes e quantos não foram?
SELECT resultado, COUNT(*) AS quantidade FROM diabetes_id GROUP BY resultado;

--5. Mostre o nome e a data de nascimento dos pacientes que moram em "Recife".
SELECT nome, data_nascimento FROM pacientes WHERE cidade = 'Recife';

--6. Conte quantos pacientes do sexo feminino existem em cada cidade.
SELECT cidade, COUNT(*) AS quantidade FROM pacientes WHERE sexo = 'F' GROUP BY cidade;