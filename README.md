# Keskustelusovellus

Keskustelusovellus on web-sovellus, jossa käyttäjät voivat keskustella eri aiheista.

## Teknologiat

Backend on toteutettu Pythonilla Flask-kirjastolla. Tietokantana käytetään PostgreSQL:ää. Frontendin tyylit on kirjoitettu tailwindilla ja sovellus hyödyntää [htmx](https://htmx.org/)-kirjastoa dynaamisuuden toteuttamiseen.

## Sovelluksen ominaisuuksia

- Käyttäjä voi luoda tunnuksen (ei vielä implementoitu)
- Käyttäjä voi kirjautua sisään (salasanat ei vielä implementoitu)
- Käyttäjä voi kirjoittaa viestejä
- Käyttäjä voi poistaa viestejä
- Käyttäjä voi muokata viestejä (ei vielä implementoitu)
- Käyttäjä voi kirjautua ulos
- Käyttäjä voi poistaa tunnuksen (ei vielä implementoitu)
- Käyttäjä voi luoda keskustelun
- Käyttäjä voi poistaa keskustelun
- Käyttäjä voi luoda keskustelukategorian (ei vielä implementoitu)
- Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana (ei vielä implementoitu)

## Käynnistys

Projekti käyttää Pythonin Flask-kirjastoa docker kontissa. Jos et ole ladannut dockeria koneellesi, tee se [näiden](https://docs.docker.com/engine/install/) ohjeiden mukaan. Sovelluksen käynnistys onnistuu komennolla `docker compose up`. Sovellus käynnistyy osoitteeseen http://localhost:5001.

## Kansiorakenne

Kansiorakenne on hieman erilainen kuin mitä kurssimateriaaleissa ohjeistetaan. Sovelluksen lähdekoodi on `flaskr`-kansiossa. Tietokantaskeema löytyy juuresta tiedostosta `schema.sql`. Docker-konfiguraatio löytyy `docker-compose.yml`-tiedostosta.

## Docker

Sovellus käyttää kolmea docker konttia: flask, postgres ja tailwind. Flask-kontti pyörittää applikaatiota, postgres-kontti tietokantaa ja tailwind-kontti luo parsii frontendin tyylit. Tailwind tarvitsee node.js:n, minkä takia se on oma konttinsa.