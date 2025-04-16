const tg = window.Telegram.WebApp;
tg.expand();

let user = null;
let coins = 0;

async function init() {
  const initDataUnsafe = tg.initDataUnsafe;
  const res = await fetch('/init', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      telegram_id: initDataUnsafe.user.id,
      username: initDataUnsafe.user.username,
      ref: new URLSearchParams(window.location.search).get('ref')
    })
  });

  const data = await res.json();
  user = data.user;
  coins = data.user.coins;
  updateUI();
}

function updateUI() {
  document.getElementById("coins").innerText = coins;
}

async function clickCoin() {
  const res = await fetch('/click', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ telegram_id: user.telegram_id })
  });

  const data = await res.json();
  coins = data.coins;
  updateUI();
}

document.getElementById("click-button").addEventListener("click", clickCoin);
init();
