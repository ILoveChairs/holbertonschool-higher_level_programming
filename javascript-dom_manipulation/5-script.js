const pseudoButton = document.getElementById('update_header');
const header = document.querySelector('header');
pseudoButton.onclick = () => {
  header.innerHTML = 'New Header!!!';
};
