CREATE TABLE IF NOT EXISTS Usuario(
    ID_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario VARCHAR(255),
    contrasena VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS InfoUser(
    ID_info INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_usuario INTEGER,
    nombre VARCHAR(255),
    email VARCHAR(255),
    altura INTEGER,
    genero VARCHAR(255),
    peso INTEGER,
    grasa INTEGER,
    FOREIGN KEY (ID_usuario) REFERENCES Usuario (ID_usuario)
);

CREATE TABLE IF NOT EXISTS Restricciones(
    ID_restriccion INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_usuario INTEGER,
    restriccion_desc VARCHAR(255),
    FOREIGN KEY (ID_usuario) REFERENCES Usuario (ID_usuario)
);

CREATE TABLE IF NOT EXISTS Rutina(
    ID_rutina INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_info INTEGER,
    nombre_rutina VARCHAR(255),
    FOREIGN KEY (ID_info) REFERENCES InfoUser (ID_info)
);

CREATE TABLE IF NOT EXISTS Comida(
    ID_comida INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_info INTEGER,
    nombre_dieta VARCHAR(255),
    FOREIGN KEY (ID_info) REFERENCES InfoUser (ID_info)
);

CREATE TABLE IF NOT EXISTS Ejercicio(
    ID_ejercicio INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_rutina INTEGER,
    nombre_ejercicio VARCHAR(255),
    setss INTEGER,
    repeticiones INTEGER,
    peso INTEGER,
    musculo VARCHAR(255),
    equipamiento VARCHAR(255),
    FOREIGN KEY (ID_rutina) REFERENCES Rutina (ID_rutina)
);

CREATE TABLE IF NOT EXISTS Alimento(
    ID_alimento INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_comida INTEGER,
    nombre_alimento VARCHAR(255),
    cantidad VARCHAR(255),
    calorias INTEGER,
    FOREIGN KEY (ID_comida) REFERENCES Comida (ID_comida)
);