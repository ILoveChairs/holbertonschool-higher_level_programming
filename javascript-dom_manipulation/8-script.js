fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
.then((response) => response.json())
.then((data) => {
    const character = document.getElementById('hello');
    character.innerHTML = data.hello;
  }).catch((err) => {
    character.innerHTML = err.toString();
  });
