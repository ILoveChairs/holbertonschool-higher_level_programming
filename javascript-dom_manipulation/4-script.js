const pseudoButton = document.getElementById('add_item');
const unorderedList = document.querySelector('.my_list');
pseudoButton.onclick = () => {
  const li = document.createElement('li');
  li.appendChild(document.createTextNode('Item'));
  unorderedList.appendChild(li);
};
