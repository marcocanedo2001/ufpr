DROP TABLE IF EXISTS municipio;
DROP TABLE IF EXISTS estado;


CREATE TABLE estado(
    uf TEXT PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE,
    regiao TEXT NOT NULL,
    FOREIGN KEY (regiao) REFERENCES regiao(sigla)
);

--NORTE
INSERT INTO estado (uf, nome, regiao) VALUES ('AC', 'Acre', 'N');
INSERT INTO estado (uf, nome, regiao) VALUES ('RO', 'Rondônia', 'N');
INSERT INTO estado (uf, nome, regiao) VALUES ('AM', 'Amazonas', 'N');
INSERT INTO estado (uf, nome, regiao) VALUES ('RR', 'Roraima', 'N');
INSERT INTO estado (uf, nome, regiao) VALUES ('PA', 'Pará', 'N');
INSERT INTO estado (uf, nome, regiao) VALUES ('AP', 'Amapá', 'N');
INSERT INTO estado (uf, nome, regiao) VALUES ('TO', 'Tocantins', 'N');


--NORDESTE
INSERT INTO estado (uf, nome, regiao) VALUES ('AL', 'Alagoas', 'NE');
INSERT INTO estado (uf, nome, regiao) VALUES ('BA', 'Bahia','NE');
INSERT INTO estado (uf, nome, regiao) VALUES ('MA', 'Maranhão','NE');
INSERT INTO estado (uf, nome, regiao) VALUES ('CE', 'Ceará','NE');
INSERT INTO estado (uf, nome, regiao) VALUES ('PI', 'Piauí','NE');
INSERT INTO estado (uf, nome, regiao) VALUES ('RN', 'Rio Grande do Norte','NE');
INSERT INTO estado (uf, nome, regiao) VALUES ('PB', 'Paraíba','NE');
INSERT INTO estado (uf, nome, regiao) VALUES ('PE', 'Pernambuco','NE');
INSERT INTO estado (uf, nome, regiao) VALUES ('SE', 'Sergipe','NE');

--SUDESTE
INSERT INTO estado (uf, nome, regiao) VALUES ('MG', 'Minas Gerais', 'SE');
INSERT INTO estado (uf, nome, regiao) VALUES ('ES', 'Espírito Santo', 'SE');
INSERT INTO estado (uf, nome, regiao) VALUES ('RJ', 'Rio de Janeiro', 'SE');
INSERT INTO estado (uf, nome, regiao) VALUES ('SP', 'São Paulo', 'SE');

--SUL
INSERT INTO estado (uf, nome, regiao) VALUES ('PR', 'Paraná', 'S');
INSERT INTO estado (uf, nome, regiao) VALUES ('SC', 'Santa Catarina', 'S');
INSERT INTO estado (uf, nome, regiao) VALUES ('RS', 'Rio Grande do Sul', 'S');

--Centro-Oeste
INSERT INTO estado (uf, nome, regiao) VALUES ('DF', 'Distrito Federal', 'CO');
INSERT INTO estado (uf, nome, regiao) VALUES ('GO', 'Goiás', 'CO');
INSERT INTO estado (uf, nome, regiao) VALUES ('MT', 'Mato Grosso', 'CO');
INSERT INTO estado (uf, nome, regiao) VALUES ('MS', 'Mato Grosso do Sul', 'CO');