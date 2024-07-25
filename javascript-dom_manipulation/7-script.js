fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
    const unorderedList = document.getElementById('list_movies');
    for (const item of data.results) {
      const li = document.createElement('li');
      li.appendChild(document.createTextNode(item.title));
      unorderedList.appendChild(li);
    }
  }).catch((err) => {
    console.log(err.toString());
  });
