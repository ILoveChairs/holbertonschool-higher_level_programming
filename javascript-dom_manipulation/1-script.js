const pseudoButton = document.getElementById('red_header');
const header = document.querySelector('header');
pseudoButton.onclick = () => {
  header.style.color = 'red';
};
