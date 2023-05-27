const buttons = document.querySelectorAll('.filter-button');
const sections = document.querySelectorAll('.section');

buttons.forEach((button) => {
  button.addEventListener('click', () => {
    const target = button.getAttribute('data-target');
    showSection(target);
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