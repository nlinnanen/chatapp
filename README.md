# Keskustelusovellus

Keskustelusovellus on web-sovellus, jossa käyttäjät voivat keskustella eri aiheista.

## Teknologiat

Backend on toteutettu Pythonilla Flask-kirjastolla. Tietokantana käytetään PostgreSQL:ää. Frontendin tyylit on kirjoitettu tailwindilla ja sovellus hyödyntää [htmx](https://htmx.org/)-kirjastoa dynaamisuuden toteuttamiseen.

## Sovelluksen ominaisuuksia

- Käyttäjä voi luoda tunnuksen
- Käyttäjä voi kirjautua sisään
- Käyttäjä voi kirjoittaa viestejä
- Käyttäjä voi poistaa viestejä
- Käyttäjä voi muokata viestejä
- Käyttäjä voi kirjautua ulos
- Käyttäjä voi poistaa tunnuksen
- Käyttäjä voi luoda keskustelun
- Käyttäjä voi poistaa keskustelun
- Käyttäjä voi luoda keskustelukategorian
- Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana

## Käynnistys

Projekti käyttää Pythonin Flask-kirjastoa docker kontissa. Jos et ole ladannut dockeria koneellesi, tee se [näiden](https://docs.docker.com/engine/install/) ohjeiden mukaan. Sovelluksen käynnistys onnistuu komennolla `docker compose up`. Sovellus käynnistyy osoitteeseen http://localhost:5001.

Kehitystyössä käytetään devcontaineria. Tämä vaatii Visual Studio Coden ja [Dev Container](https://code.visualstudio.com/docs/remote/containers) laajennuksen. Kun olet ladannut nämä, voit avata projektin Visual Studio Codessa ja valita `Reopen in Container` -komennon. Kontin sisällä voit käynnistää sovelluksen komennolla `flask run --host=0.0.0.0`, jolloin sovellus käynnistyy osoitteeseen http://localhost:5000.