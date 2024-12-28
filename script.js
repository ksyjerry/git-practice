
let user = prompt("가위바위보 중 하나를 입력하세요");
let computer = Math.floor(Math.random() * 3);

console.log(user, computer);

document.getElementById("result").innerText = user;
document.getElementById("result").innerText = computer;
