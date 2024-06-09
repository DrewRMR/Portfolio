DROP TABLE IF EXISTS tWords

CREATE TABLE tWords(
	WordID INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
	Word NVARCHAR(100) NOT NULL
)

INSERT INTO tWords(Word) VALUES('seesaw')
INSERT INTO tWords(Word) VALUES('earmuffs')
INSERT INTO tWords(Word) VALUES('toxic')
INSERT INTO tWords(Word) VALUES('spotty')
INSERT INTO tWords(Word) VALUES('screwdriver')
INSERT INTO tWords(Word) VALUES('octopus')
INSERT INTO tWords(Word) VALUES('samsung')

SELECT * FROM tWords