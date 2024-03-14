const keyboardLetter = ['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю'];
let keyboardCharCode = [81, 87, 69, 82, 84, 89, 85, 73, 79, 80, 219, 221, 65, 83, 68, 70, 71, 72, 74, 75, 76, 186, 222, 90, 88, 67, 86, 66, 78, 77, 188, 190]

// document.onkeydown = function (event) {
// 	// console.log(event);
// 	keyboardCharCode.push(event.keyCode);
// 	console.log(event)
// 	// console.log(keyboardCharCode);
// }


// function init() {
// 	let out = "";

// 	for (let item = 0; item < keyboardLetter.length; item++) {
// 		out += '<div class="k-key" data="' +keyboardCharCode[item]+'">' + keyboardLetter[item] + '</div>'
// 	}
// 	document.getElementById("keyboard").innerHTML = out;
// 	document.getElementById("keyboard").insertAdjacentHTML('afterbegin', out);
// }

// init();


document.onkeydown = function (event) {
	console.log(event.key);
	document.querySelectorAll("#rows .k-key").forEach(function (element) {
		element.classList.remove("active")
	});
	document.querySelector('#rows .k-key[data="' + event.keyCode + '"]').classList.add('active');
};

document.querySelectorAll("#rows .k-key").forEach(function (element) {
	element.onclick = function (event) {
		document.querySelectorAll("#rows .k-key").forEach(function (element) {
			element.classList.remove("active")
		});
		let letter = this.innerHTML;
		this.classList.add("active");
		console.log(event);
	}
});