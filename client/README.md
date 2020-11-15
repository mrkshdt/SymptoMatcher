# Getting Started
Voraussetzung zur Verwendung der React App ist die Installation von node.js. Ist dies gegeben, müssen alle für das Projekt notwendigen node Module (aufgelistet in package.json) installiert werden indem lediglich folgender Befehl im client Verzeichnis über die Kommandozeile ausgeführt wird:

`npm install`

Die React App ist anschließend Einsatzbereit und kann mit folgendem Befehl im Client Verzeichnis gestartet werden:

`npm start`

Im Standardbrowser öffnet sich nun die React App.

# Anmerkungen
Die React App kommuniziert mit einem Flask API Server im Hintergrund, der parallel gestartet werden muss. Es wird davon ausgegeangen, dass dieser unter folgender (Standard-)Adresse ansprechbar ist http://localhost:5000 . Dies kann allerding durch Änderung der "proxy" Eigenschaft in package.json angepasst werden.
