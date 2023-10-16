# ERKER

### ERKER - ERDRI-CDS kompatible Erfassung in REDCap
Der ERKER ermöglicht die Erfassung seltener Patient:innen und überführt diese in ein standardisiertes Format gemäß FAIR-Prinzipien (Findability, Accessability, Interoperability, Reusability). Der ERKER Datensatz wurde auf Basis 
- des ERDRI-CDS (European Rare Disease Registry Infrastructure - Common Data Set) 
  und
- dem NARSE (Nationales Register für Seltene Erkrankungen)
  entwickelt.
Der ERKER-Datensatz wurde um weitere Datenelemente erweitert, um eine präzisere Darstellung des Krankheits- und Behandlungsverlaufes, \
der Geno- und Phänotypisierung und der Primär- und Sekundärdiagnosen zu ermöglichen. 

Die Version 1.7 steht zur Datenerfassung in REDCap als DataDictionary und als ERKER_v1.7.zip im Ordner "v1.7" zur Verfügung. Nachdem ein Projekt in REDCap aufgesetzt wurde kann damit das Formular hochgeladen werden. Näheres hierzu im Ordner Guidelines. 

### Eigenständiges Testen: 
Sie können das Formular bei sich testen. Folgen Sie hierfür diesem Link: https://redcap.charite.de/demo/surveys/?s=XKP4RH3TPXTFMKPE 
oder tragen Sie auf folgender Website https://redcap.charite.de/demo/surveys/ den Code 3DA7DPPEE ein.
Bitte tragen Sie hier <ins>keine Echtdaten</ins> ein.


### ERKER Konzept
![ERKER_Konzept_flow](https://github.com/BIH-CEI/ERKER/assets/109136019/0410962d-1750-424d-be2f-5e01574e5ce3)


## Ordner Strukutur:
#### ERDRI-CDS
Den ERDRI-CDS befindet sich im Ordner ERDRI-CDS auf Englisch und Deutsch.

#### ERKER4NARSE
Hier finden Sie den genauen Leitfaden zur Erfassung für das Nationale Register für Seltene Erkrankungen (NARSE) mit dem ERKER.
Auch die aktuelle Version des ERKER_v1.7_NARSE steht zum Download bereit. Hierbei werden nur die NARSE relevanten Datenelemente angezeigt.

#### ERKERonFHIR
Hier werden relevante Dateien zur Übertragung vom ERKER in FHIR abgelegt.

#### Guidelines
Generelle Guidelines zur Erfassung mit ERKER in REDCap.

#### ERKER2Phenopackets
Das Projekt für die Pipeline von ERKER nach Phenopackets: https://github.com/BIH-CEI/ERKER2Phenopackets 

### v1.7 
Zum Download das aktuelle DataDictionary und die .zip Datei für die Installation im lokalen REDCap Projekt. 









