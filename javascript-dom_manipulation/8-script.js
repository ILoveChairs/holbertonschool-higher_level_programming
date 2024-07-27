window.onload=function() {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then((response) => response.json())
  .then((data) => {
      const responseElement = document.getElementById('hello');
      responseElement.innerHTML = data.hello;
    }).catch((err) => {
      const responseElement = document.getElementById('hello');
      responseElement.innerHTML = err.toString();
    });
}
