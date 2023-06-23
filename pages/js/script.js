document.querySelectorAll('#collapsible .item .head').forEach(item => {
    item.addEventListener('click', event => {
        item.parentElement.classList.toggle('collapsed');
    })
});