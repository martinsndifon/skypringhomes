const buttons = document.querySelectorAll('.filter-button');
const sections = document.querySelectorAll('.section');

buttons.forEach((button) => {
  button.addEventListener('click', () => {
    const target = button.getAttribute('data-target');
    showSection(target);
    styleButton(target);
  });
});

function showSection(target) {
  sections.forEach((section) => {
    if (section.getAttribute('id') === `${target}-section`) {
      section.classList.add('active');
    } else {
      section.classList.remove('active');
    }
  });
}

function styleButton(target) {
  buttons.forEach((button) => {
    if (button.getAttribute('data-target') === target) {
      button.classList.add('btn-active');
    } else {
      button.classList.remove('btn-active');
    }
  });
}
