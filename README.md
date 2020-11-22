![SymptoMatcher](https://github.com/mrkshdt/SymptoMatcher/blob/master/SymptoMatcher.jpg?raw=true)

# Genereller Aufbau
Der Api Server übernimmt die Datenverarbeitung auf dessen Ergebnisse der React Client zugreift um mit dem User zu Interagieren.

## Starten des API Servers
Zum Starten des API Servers wird eine python virtual environment (venv) empfohlen in welcher die notwendigen dependencies installiert werden müssen. Hierfür kann die requirements.txt Datei verwendet werden:

`pip install -r requirements.txt`

Im Root Ordner des Projektes kann nun über folgenden Befehl der API Server gestartet werden:

`flask run` 

## Starten des React Clients
Der React Client wird zum Interagieren mit dem User verwendet.
Zur Verwendung, lesen sie bitte die im Ordner client befindliche read.me.

## Hinweise

Um anhand der User-Beschreibung die Zuweisung zum entsprechenden Fachbereich zu realisieren wird per **default** die lexikalische Ähnlichkeit der User Beschreibung mit Fachbegriffen jedes Fachbereiches verglichen. **Alternativ** kann dies mit **Word Embeddings** von FastText erreicht werden, welche sowohl die semantische als auch lexikalische Ähnlichkeit von Worten berücksichtigen. Da dies allerdings den Download einer 8GB großen Datei voraussetzt und entsprechender Rechenleistung bedarf zum Verwenden bedarf, ist dies standardmäßig deaktviert.
Die Funktion kann dennoch genutzt werden, indem der im Ordner api_server\resources aufgeführte Link genutzt wird um die Word Embedding Daten runterzuladen und dort abzulegen und die Variable useFastText in data_processing.py auf True gesetzt wird. Ggf. muss fasttext ebenfalls als python modul installiert werden.
