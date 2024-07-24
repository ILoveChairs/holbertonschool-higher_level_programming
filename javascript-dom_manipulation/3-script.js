const pseudoButton = document.getElementById('toggle_header');
const header = document.querySelector('header');
pseudoButton.onclick = () => {
  if (header.classList.contains('red')) {
    header.classList = ['green'];
  } else {
    header.classList = ['red'];
  }
};
