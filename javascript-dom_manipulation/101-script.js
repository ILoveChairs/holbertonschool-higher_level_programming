window.onload = () => {
  const translateButton = document.getElementById('btn_translate')
  const responseElement = document.getElementById('hello');

  translateButton.onclick = () => {
    const lang = document.getElementById('language_code').value;

    fetch(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`)
    .then((response) => response.json())
    .then((data) => {
        responseElement.innerHTML = data.hello;
      }).catch((err) => {
        responseElement.innerHTML = err.toString();
      });
  }
}
