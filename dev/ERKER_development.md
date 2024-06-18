# ERKER_development



## alpha_v1.1 Diskussion
01.08.2022

1.  Pseudonym
    - entschieden: standortspezifische Pseudonymisierung
    - Treuhandstelle (A. Essenwanger) für UMG, Charité, etc.
        - Kontaktaufnahme für jeweiige Standorte
    - Für Algorithmische Analysen: eigene Pseudonymisierung sei schnell möglich, sobald Testdaten analysiert werden
        - Überlappungsausschluss via SMPC

2.	Erweiterung Geschlecht 2.2	
    - entschieden: karyotpypic Sex für OrphaDiagnose 6.1.1 & 6.1.2
    - entschieden: 4 Möglichen vom ERDRI bleiben
        - Elisabeth fragt nach bezgl. 'divers'

3.	Pflichtfelder / Identifier
    - 6.1: Orpha,
    - 2.1: Geburtsdatum
    - 2.2: Geschlecht
    - 7.1, 7.2: Datenweiterverarbeitung

4.	Ungenaue Datumserfassung 5.1, 5.2…
    - Kontaktaufnahme Simona Martin (letzte Juli Woche)
    - entschieden: bei Auswahl Datum:
        - 3 Unterpunkte: Tag, Monat, Jahr

5.	Alpha ID 6.1
    - vorläufig 
    - Alpha ID unter 6.1: Ja/nein/nicht erfasst
        - bei Ja: kommt Liste oder Textbox
    - irgendwann DIAKOS 

6.	Orpha Subtyp Diagnose 6.1
    - entschieden: OMIM bei 6.1 weg, nur bei 6.2 
    - Orpha Subtyp bleibt als 6.1.2

7.	Krankheitsspezifische Valuesets bei Diagnose 6.1/6.2/6.3
    - 6.3 Phänotypisierung generell  wird immer erhoben
    - 6.3.0 nicht diag. Fall ja/nein ..
    - 'unendliche Phänotpyen
    - krankheitsspez. Valuesets / Phänotypisierung in externen Formularen

8.	Ohne Diagnose: weitere Phänotypen 6.3
    - wie viele Phänotypen bei unklarer Diagnose? 
    - Kontaktaufnahme Hr Hetey für 'unendliche' Verlängerung
    - relationales Datenmodell wie in OSSE
      - RedCap hat mySQL als Datenbank, wäre dadurch relational

9.	Terminologie Integration 6.1, 6.2, 6.3, 8.1
    - ICD-10: kein ICD-10 GM, nur int.
        - in DE gilt nur ICD-10 GM 
        - entschieden für ICD10 CM (clinical modification)
    - BioPortal Göttingen fehlt Freigabe
    - Kontaktaufnahme Köln Terminologieserver A. Grönke (27.07.2022)
        - für jeden mit DFN Userzertifikat erreichbar
        - Integration in REDCap:in Absprache mit Hr Hetey (Serveradmin Charité)


10. NARSE Erweiterung via NARSE_AddOn
    - Formular fertig
    - Integration in den ERKER selbst
        - Workflow für NARSE optimieren
    - Erstellung Skripte für spezifischen Export an NARSE, ERDRI, etc. 
        - .xls Datei
    - in den ERKER einen Vermerk für jew. Export hinzufügen (als Notiz, Logo, etc.)
        - Hetey fragen: Exportmöglichkeiten

11.	Erweiterung Modul Forschung & Behinderung 7.1,7.2,7.3,7.4,8.1
    - 7.2 Nur als Überschrift
        - 7.2.1 Einwilligung zur Übermittlung nach NARSE
        - 7.2.2 Einwilligung für Forschungszwecke im ERKER

12.	Variablen Definition
    - erstmal so lassen 
    - Liste von Erklärungen für Variablen mit Abkürzungen
        - als Codebook in REDCap abrufbar
 

13. Familienanamnese NARSE
    - MII KDS: dort umfangreicher als im NARSE?
    - vorläufig: krankheitsspez. Familienanamnese auch mit krankheitsspez. Formularen in Abh. von Anforderungen der FOSAS 
    -  Humangenetik Absprache Dominik Seelow & Stefan Mundlos
       - für jetzt nur NARSE Version in ERKER, damit v1.0 läuft
       - generelle Integration/Erweiterung Fam Anamnese für SE

14.	Weitere Diskussionspunkte
    - 
  

## alpha_v1.2 Diskussion
09.08.2022 

### Änderungen

1. __entschieden: Laut Hr Hetey kein genaues Geb.Datum erlaubt bei Erfassung in der Charité REDCap
  - nur Jahreszahl
  - generell keine identifizierenden Daten in REDCap möglich
    - Lösung: identifizierende Daten können in parallel ausgelagerter Datei Standortintern abgelegt
      - diese können auf dem Server der Treuhandstelle abgelegt werden 
  - standortspezifische Absprachen notwendig

2. entschiden:NARSE: Symptom und Diagnosebeginn anders erfasst als im ERDRI
   - Vorschlag: ERDRI Erfassung beibehalten, NARSE ungenau 

3. extra Geschwister aus NARSE hinzufügbar: (Alter & Geschlecht)
   - bisher 4 Geschwister, mehr hinzufügen?
   - entschieden: 10 Geschwister, um auf der sicheren Seite zu sein

4. Phänotypiserung
   - bisher 10 HPOs hinzufügbar
   - auf wie viele soll sich hier geeinigt werden?
   - entschieden: 30 HPOs 
     - Können nochmal P. Robinson fragen für seine Einschätzung

5. Kodierung weiterer Variablen
    - mit SNOMED, HPO etc. weitere mögliche Variablen kodieren
    - für Mapping sehr hilfreich
    - FrontEnd: einfache Auswahlmöglichkeiten
    - BackEnd: Alle Codes werden für das FHIR Mapping genutzt



## beta_v1.0
- Erfassung von Testdaten via:
  - FHIR Daten aus ERKER
  - .csv Daten erstellen


- grundsätzlich möglichst nah an value sets & molek. gen. Befundbericht



# beta_v1.1

- 2.1 variable geburtsdatum -> geburtsjahr

- 3.1 "verweigert"
  - in DE unklar: Auswahlmöglichkeit erweitert um "verweigert (von weiterer Behandlung)"

- 6.1.3 Diagnose: ICD10-CM in ICD-10 Code geändert 
  - ICD-10GM in BioPortal nicht verfügbar

- 6.2. genetische Diagnose: 
  - 6.2.6: Zygotie hinzugefügt
    - Heterozygotie/Homozygotie/Hemizygotie/nicht erfasst 

- 6.3.2 Verdachtsdiagnose: ICD10-CM in ICD-10 Code geändert
  - ICD-10GM in BioPortal nicht verfügbar
  
- 6.4.2 & 6.4.6: Alter Mutter/Vater
  - In Bezug auf Erfassungsdatum
    - Notiz hinzugefügt: "(Zum Zeitpunkt der Erfassung)"
  - 6.4.5 & 6.4.6 getauscht

- 6.4.7: Notiz hinzugefügt: "Folgend bitte nur betroffene Geschwister erfassen!"

- 6.5.1: Therapie_spez: von single choice in multiple choice geändert
  - warum in NARSE als single choice? 
#
- 7.2.4 zustimmung_daten_DIZ hinzugefügt
 


## V1.0 (Produktionsmodus)


- 6.3.2 & 6.1.3: ICD Diagnose & Verdachtsdiagnose: 
  - ICD10GM: freies Textfeld
  - icd10gm

- 6.2. genetische Diagnose: 
  - HGVS: Beispiele hinzugefügt
  - 6.2.4A: Biomarker als String: warten auf endgültiges NARSE-Datensatz Update
    - Jens Göbel: LOINC, SNOMED, Freitext?
      - https://ontoserver.csiro.au/shrimp/?system=http%3A%2F%2Floinc.org&concept=LP31392-1&version=2.72&valueset=http%3A%2F%2Floinc.org%2Fvs 
  - HGVS: für Mapping für jetzt coding-hgvs

- 6.2.6 Zygotie..

- 7.2 Zustimmung Daten
  -
   Jens Göbel Gespräch: Einwilligung inhaltlich, national/internatial?
  - ERKER: gelöscht
  - DIZ: gelöscht




## v1.0: klinische Daten
$$
- Leitfaden muss erstellt werden für weitere Standorte 



## v1.1:


- backend:
  - SNOMED Codes nochmal mit FHIR Resourcen überprüfen
  - bspw.: Siblings sct von FHIR nutzen (siehe heitmann.xls)
- HGVS / HGNC auf 4-5 erweitern!!
- Backend development: 
  - Variablen verlängert
  - field attribute values
$$

## v1.2: $$$$  $$
### changes: 

- sct_439401001_orpha
  - _orpha_sub
  - _icd10gm
  -> extended from 1 to 3 fields each

- new field: sct_184305005_se: An SE Verstorben?
  - [SCT= Cause of Death]

- 2.2: Geschlecht: sct_281053000
  - new Option: sct_33791000087105, Divers

- 6.2.3: 3x OMIM anstatt 1x

- 6.2.5 Umbenennung genau an NARSE Terminus

- 6.2.7: jew. "Alter des Geschwisterkinds bei Einschluss des Patienten im NARSE" als Field Annotation hinzugefügt

- 7.2.2: Renaming: Datennutzung international *(EU)*
  - Field Annotation: Einwilligung für internationale Datennutzung (beschränkt auf den EU Raum) liegt vor.

## v1.3: still to be implemented Publikationsversion

- OMIM: 
  - 2x: _pheno & _geno? 

- _done_Konsanguinität 
  - 

- _done_Annics Datenpunkte hinzufügen

- _done_NARSE Datensatz finalisierung 
  
- _done_HGVS Erfassung überarbeiten: gemäß MolGen Befund (Caroline fragen)

- _done_3.3 Alterskategorie
  - Ungeboren: neuer sct_value: sct_303112003 https://simplifier.net/basisprofil-de-r4/valuesetlebensphasede 
    - ...[Josef]: - seitens der KBV-MIO-Gruppe ist der folgende SCT-Kode für Ungeborene bestätigt worden: 

- _done_Orpha Diagnose nach BioPortal: Data entry field dann als "Obesity due to pro-opiomelanocortin deficiency" anstatt Orpha Code : 71529 

- Überprüfung sct & lnc codes


hinzugekommen ist: 

- all date values to Y-M-D
- 2.3 
- 2.4 eingabe nur als String?
- 2.5
- 3.3: 
  - alle sct codes aus MII KDS Lebensphase (https://simplifier.net/basisprofil-de-r4/valuesetlebensphasede)
- 3.5
- 3.6
- 4 (new section header)
- 4.2
  - here: sct_307836003_mvz -> Medizinisches) Versorgungszentrum (=! Medical care centre (EN) 
- 4.3


- 5.2 
  - 5.2(.1.2.3) -> 5.3(.1.2.3)
  - 5.3 -> 5.4
- 5.4
- 5.5
- 5.6
- 5.7
- 5.8

- 6.1 (new section header)
- 6.1.10(A) -> 6.1.4(A)
- 6.1.7 -> 6.1.3
- 6.1.5
- 6.1.6
- 6.1.7
- 6.1.8
- 6.1.9
  .... bis 6.1.19



- 6.2 "Genetische Diagnose"
- F: Ursprung d. Variante: Observation.component:genomic-source-class 
- G: DNA Mutationstyp: Variant - Observation.component:coding-change-type
- H: Klinische Signifikanz Observation.component:clinical-significance 
- I: Clinical Annotation Level Of Evidence Observation.component:evidence-level
- 
  - 6.2 -> 6.2.1
  - HGVS // HGNC // OMIM !! hier noch MolGen Befund für Hauptdiagnose erweitern? !! 
    - 6.2.2A/B/C // D // E
    - 6.2.3A/B/C // D // E
    - 6.2.4A/B/C // D // E
          - *here we could add another fields: 
            - 1.Status:registered/preliminary/final/amended  
            - 2. date when gene mutation was determined   
            - 3. Haplotype of the carrier (mother / father)  
  - 6.2.4 -> 6.2.5 (/A)
  - 6.2.5 -> 6.2.6

  - 6.2.6 -> nur Zygotie, single choice (vorher multiple choice)
    - -> 6.2.7
  - 6.2.8 neu (Plamsmie), single chice
    - -> 
  - 6.2.9 sct codes fehlen noch: Caroline fragen? 


- 6.3 "Nebendiagnosen" 
  - 6.3.1A/B/C
  - 6.3.2A/B/C
  - ...

- 7.2.: 
  - variablen namen und inhalt geändert

- sct_103330002_ln_48004_6_1/2/3 gelöscht

# v1.4 

- <d biological sex checken? https://browser.ihtsdotools.org/?perspective=full&conceptId1=429019009&edition=MAIN/2023-02-28&release=&languages=en nochmal im SEmanal ansprechen
  - sct_281053000 (sex at delivery of baby): sct_281053000 -> sct_429019009 Finding related to biological sex (finding)

- <d Unterpunkt: 1. Formale Krieterien?

- <d keine radiobuttons, nur listen? 

- <d geburtsland: sct_315354004 -> sct_370159000 

- 2.5 Ethnizität nochmal diskutieren: 
    - Untergruppen von: Racial group (racial group) SCTID: 415229000
    - <d'Hispanic or Latino': hl7_cld_2135-2 -> sct_414408004 ?

- <d Formatierung der Überschriften alle angleichen 

- <d 4.3 'nicht erfasst sct_1220561009 ' hinzufügen

- <d 5.2 fehlt, ab 5.3 einen nach unten rutschen? 
  - 5.3 -> 5.2, 5.4-> 5.3, etc. 

- <d Hauptdiagnose und Nebendiagnose in Prim.- und Sek.diagnosen ändern. 


-  <d 6.1.7 Hauptdiagnose: nicht erfasst hinzufügen

- <d 6.1.16 & 17: https://fhir.loinc.org/ValueSet/LL381-5 für Fieldoptions values übernehmen
  - variable : ln_55198_6 -> ln_48007_9 & ln_48007_9_mitoch
  -        "code": "LA6703-8",
        "display": "Heteroplasmic"
      }, {
        "code": "LA6704-6",
        "display": "Homoplasmic"
      }, {
        "code": "LA6705-3",
        "display": "Homozygous"
      }, {
        "code": "LA6706-1",
        "display": "Heterozygous"
      }, {
        "code": "LA6707-9",
        "display": "Hemizygous" 

- 6.2 Genetischer Befund: 

  - !! g.hgvs -> g.vcf : peter Robinson fragen
  - <d referenzgenom: https://fhir.loinc.org/ValueSet/LL1040-6 
    - <d ln_62374_4_1, _2, _3.... _8
    - __//__ wird nicht mit eingebracht: Eingabe Feld Transcript Ref Seq  (bezieht sich auf c. & p. ) (z.B. NM_005912.3)
  - <d "Transition" macht keinen Sinn, ist auch nur eine Art Punktmutation und es gibt dann eigentlich 2: Transition und Transversion
  - __//__ (6.2.2. Sequenzierung würde ich Sequenzierung unterscheiden noch. Sanger und NGS. Ggf. NGS dann noch in Panel, Exom, Genom) -> NICHT ÜBERNOMMEN, Werte aus Valueset https://fhir.loinc.org/ValueSet/LL4048-6 bleiben
  - __//__ wird nicht übernommen: MolGen Befund bleibt. Klinische Signifikanz vielleicht noch extra Felder für wann die Klassifizierung war und eins für die angewendeten Kriterien die zu der Klassifizierung geführt haben
änderung Variablennamen: 
- <d Ursprung Variante: ln_ll3781_1_1 -> ln_48002_0_1 
- <d klinische Signifikanz: ln_ll4034_6_1 -> ln_53037_8_1

- <d 8. Grad Disability als Überschrift hinzufügen

- <d NARSE: kinder von SE betroffen? 



## post coordinated expressions!
- <d antwort nicht mit frage speichern in backend, also nur z.b. überweisung von als variable und antworts variablen nur die antworten jeweils angeben
  - <d value set auch z.b. von hl7 angeben
  - <d immer code und system (hl7_M) oder sct_49130421

<d immer system vor code
z.b. klinischer status 6.1.7
- https://build.fhir.org/valueset-condition-clinical.html 
- active -> hl7_conditionclinical_active 

- <d in REDCap: in field annotation alle internationalen codes reintun

- postkoordination in choices in field annotations runterschreiben, auch mit field embedding möglich für mehrere Variablen
  - overlap von mehreren variablen möglich , sophie bzw caro fragen

- validierungsrunde: es wurde immer zu zweit kodiert, manchmal sogar mehr 

## variablen änderungen: 
- 2.1
- 2.4
- 3.5
- 4.1
- 4.2
- 6.1.14, 6.1.14A
- 6.2.4F, ff. 

## neu: 
- 3.2B 
- 
## diskussionen:
- teil diskussion: redcap scheiße, aber fhir questionaires wären besser. mit ausblick von fhir questionaires
mit chat gp sct kodieren lassen 
- postkoordinierung: tessa ohlsen (lübeck): postkoordinierungseditor. : snomed ict guide und editorial guide 
- Schwierig für Postkoordinierung: 
  - 6.1.4 & 6.1.4A: AlphaID
  - 6.1.10 Verifizierungsstatus primär diagnose
  - 6.1.12: absicherung Diagonse - Auswahl: Genetische Diagnose, aber Phänotyp (HPO) nicht passend & Klinische Verdachtsdiagnose wahrscheinlich durch Phänotyp (HPO), aber keine genetische Diagnose
  - 6.1.16 Zygotie
  - 6.1.17: mitochondriale Vererbung
  - 6.2.3A & B: OMIM Diagnosen _g und _p
  - Familienanamnese:
    - 6.5.1A: Mother affected of that RD? 
    - 6.5.2A: Father affected of that RD? 
    - 6.5.3: Siblings affected of this RD?
    - 6.5.4: natural children affected of this RD? 
  - all consents: 7.1 - 7.2.2F
- DE relevante Felder: 
  - administratives Geschlecht
  - 

# v1.4.2

- branching logic 6.1.18 spezifische Therpaie und multiple choice




# 1.5 
- changed to multiple choice in spez. Therapie
- updated all validated codes, backend codes changed




# v1.6 (implemented)

### Korrekturen
- heterozygotie: compound und normal 
Compound heterozygous			LA26217-2
Double heterozygous			LA26220-6

- primärdiagnose verifizierungsstatus
  - auswahl differential fixen

- DataDictionary R73, 74, 75
- E6: gendern 

- phänotypisierung -> phänotyp 
  - zu jedem phänotyp : status (bestätigt, ausgeschlossen, nicht erfasst)

sekundärdiagnosen: 
  - zu jedem: verifizierungsstatus https://simplifier.net/packages/hl7.fhir.r4.core/4.0.1/files/81427

- 6.2.1 kommentar hinzufügen: auch wenn keine genetisch gesicherte Diagnose trotzdem Genetischen Befund eintragen 

# v1.7: 

### zygosity
- per genetic variant? so far only for primary diagnosis

### choices code change:
- sct_767023003: CS_MII_Person_Vitalstatus_X, Unbekannt -> sct code für Unbekannt, Unbekannt


# v1.8: 
- 2.4: add Geburtsland Snomed-CT: "Born in Germany" (315431007) oder nur "Germany" (22367004)? 
- 3.3: Notiz erweitern: "Bitte Alterskategorie beim Zeitpunkt der Datenerfassung bzw. dem Einschluss im NARSE angeben."
- 4.3: Notiz hinzufügen: Ziel am Zentrum für SE allgemein
- 5.3: Notiz hinzufügen: Antenatal bedeuted vor der Geburt. Malformation ... 
- 5.5/5.6: branching logic, wenn Indexfall "ja", sollte 5.6 nicht angezeigt werden
- 6.1.16: Notiz hinzufügen: Bedeutung erklären mitochondriale Vererbung
- prospectively for v1.8 we will use @if Action tag, asking at the beginning of the form whether this data capture is for NARSE y/n, then if 'y' then only NARSE elements will be shown (see dev/ERKER_development.md)
- change SCT not recorded (qualifier value) to  SCT_Patient data not recorded (finding)?
- value set variable changes in Sex at Birth and Administrative Gender
- 3.2A: SCT(date of death) -> SCT(time of death) (siehe MII-KDS):https://art-decor.org/ad/#/mide-/datasets/dataset/2.16.840.1.113883.3.1937.777.24.1.1/2018-06-05T12:44:12/concept/2.16.840.1.113883.3.1937.777.24.2.448/2018-08-06T09:32:16
- 
