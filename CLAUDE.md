# CallTime – noter til Claude

Simpel tidsregistrerings-app for en filmfotograf (Steadicam/kamera): jobs → dage → start/slut-tid, transporttid, udstyr, og lønberegning efter FAF's overenskomster (reklamefilm 2024–26 og fiktion 2025–27). UI og tekster er på dansk.

## Drift
- Hostes på GitHub Pages fra `main`, rodmappen: https://dkjonastorp-ux.github.io/calltime
- En push til `main` er en udrulning. Appen henter selv nyeste version (service worker er network-first).
- Brugeren arbejder ikke selv med koden; Claude laver ændringer og committer.
- **Arbejdsgang (brugerens regel):** Lav altid ændringer i forhåndsvisningen (artifact) først. Push til GitHub først, når brugeren skriver "go".

## Filer
- `index.html` – hele appen (HTML, CSS og ES5-JavaScript i én fil). `calc(job,d)` er lønberegningen, `buildText` er teksten der kopieres til Dinero.
- `firebase-config.js` – Firebase web-konfiguration (projekt `calltime-9d6cd`), ikke hemmelig.
- `firestore.rules` – kopi af reglerne i Firebase-konsollen (indsættes manuelt der ved ændring).
- `sw.js` – service worker. Hæv `CACHE`-navnet hvis caching driller.
- `manifest.webmanifest`, `icon-*.png` – hjemmeskærms-app.

## Data
- Firebase Auth (e-mail/adgangskode) + Firestore-dokument `users/{uid}/data/state` = `{json: JSON.stringify(S), updated}`.
- `S = {jobs:[{id,name,agr:'reklame'|'fiktion',grp,single,rate,days:[{id,date,start,end,tr,unv,gear[],note,gene}]}], updated}`.
- Også gemt i localStorage (`filmdage-v1`). Nyeste `updated` vinder.

## Konventioner
- Test før push: `node --check` på scriptet og et Playwright-skærmbillede i 390 px bredde, mørk tilstand.
- Hold det simpelt og iPhone-venligt; render() tegner hele `#app` om, så undgå re-render mens tids-/datofelter har fokus.

## Forhåndsvisning til kommentarer
Byg forhåndsvisningen med `python3 tools/build-preview.py index.html calltime-preview.html` (fjerner Firebase, manifest og service worker og indsætter eksempeldata). Publicér den som artifact, lad brugeren kommentere, og push først ved "go".
