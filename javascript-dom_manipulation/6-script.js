fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then((response) => response.json())
  .then((data) => {
    const character = document.getElementById('character');
    character.innerHTML = data.name;
  }).catch((err) => {
    character.innerHTML = err.toString();
  });
