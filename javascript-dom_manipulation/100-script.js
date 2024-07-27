window.onload = () => {
  const ul = document.querySelector('.my_list');

  document.getElementById('add_item').onclick = () => {
    const li = document.createElement('li');
    li.appendChild(document.createTextNode('Item'));
    ul.appendChild(li);
  };

  document.getElementById('remove_item').onclick = () => {
    if (ul.children.length > 0) {
      ul.children[ul.children.length - 1].remove();
    }
  };

  document.getElementById('clear_list').onclick = () => {
    ul.innerHTML = '';
  };
}
