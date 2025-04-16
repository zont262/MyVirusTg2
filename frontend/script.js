document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("click-button");
  const counter = document.getElementById("coin-counter");

  let coins = 0;

  button.addEventListener("click", () => {
    coins += 1;
    counter.textContent = coins;
  });
});
