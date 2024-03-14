let tasks = document.querySelectorAll(".task-container");

document.querySelectorAll("#done").forEach((element) => {
	element.onclick = function () {
		this.parentNode.parentNode.parentNode.classList.add("active");
	}
});