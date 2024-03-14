const questionButton = document.getElementById("questionButton");
const game = {
	try: 3,
	playerAnswer: [],

	subTry: function () {
		this.try--;
	},

	createWord: function (answerValue) {
		this.answer = answerValue.split("");
		for (let item = 0; item < this.answer.length; item++) {
			this.playerAnswer.push("_");
		}
	},

	changePlayerAnswer: function (letterValue) {
		let letterIndex = [];

		for (item in this.answer) {
			if (this.answer[item] == letterValue)
				letterIndex.push(item);
		}
		for (item of letterIndex) {
			this.playerAnswer[item] = this.answer[item];
		}
	},

	showWord: function (word) {
		document.getElementById("word").innerText = word.join(" ");
	},

	newGame: function () {
		document.getElementById("AnswerInput").value = "";
		document.getElementById("word").value = ""
		this.try = 3;
		this.playerAnswer = [];
		let questionBlock = document.getElementById("questionBlock");
		let answerBlock = document.getElementById("answerBlock");

		questionBlock.style.display = "block";
		answerBlock.style.display = "none";

		delete this.answer;
	},
	gameLogic: function (letter) {

		this.changePlayerAnswer(letter);
		this.showWord(this.playerAnswer);

		if (!this.playerAnswer.includes("_") && this.playerAnswer != 0) {
			alert(`Поздравляю!!! Ты угадал загаданное слово: ${this.playerAnswer.join("")}`)
			this.newGame();
		} else {
			if (!this.answer.includes(letter)) {
				this.subTry();
				if (this.try > 0) {
					alert(`Такой буквы нет в слове\nУвас: ${game["try"]} попыток`);
				} else {
					alert(`Ты проиграл\nЗагаданное слово: ${this.answer.join("")}`)
					this.newGame();
				}
			}
		}
	},
};

questionButton.addEventListener("click", function () {
	let AnswerInput = document.getElementById("AnswerInput");

	if (AnswerInput.value.length === 0) {
		alert("Заполните полe");
	} else {
		let check = confirm(`Ваше слово: ${AnswerInput.value}?`);

		if (check) {
			game.createWord(AnswerInput.value.toLowerCase())

			let questionBlock = document.getElementById("questionBlock");
			let answerBlock = document.getElementById("answerBlock");
			let keyboard = document.getElementById("keyboard");

			questionBlock.style.display = "none";
			answerBlock.style.display = "block";
			keyboard.style.display = "block";

			game.showWord(game["playerAnswer"]);
		}
	}
	document.querySelectorAll("#rows .k-key").forEach(function (element) {
		element.classList.remove("active");
	});
});


document.onkeydown = function (event) {
	if (!document.querySelector('#rows .k-key[data="' + event.keyCode + '"]').classList.contains('active')) {
		document.querySelector('#rows .k-key[data="' + event.keyCode + '"]').classList.add('active');
		game.gameLogic(event.key);
	}
};


document.querySelectorAll("#rows .k-key").forEach(function (element) {
	element.onclick = function () {
		this.classList.add("active");
		game.gameLogic(this.innerHTML);
	}
});