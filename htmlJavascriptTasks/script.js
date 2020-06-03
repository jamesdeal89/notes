
function credit() {
	alert("made by Jamie Deal");
	}

function result() {
	alert(5*7);
	}

function result2() {
	alert(5+6+7+8+9);
	}

function concatenate() {
	var word = " hello";
	var word1 = " there";
	var word2 = " user";
	alert(word + word1 + word2);
	}

function pocahontas(event) {
	var box = event.currentTarget;
	var x = event.clientX;
	var color = "hsl(" + x + ", 100%, 50%)";
	box.style.backgroundColor = color;
	}

function squared() {
	var num = document.getElementById("num").value;
	alert(num ** 2);
	}

function submit2() {
	var height = document.getElementById("height").value;
	var width = document.getElementById("width").value;
	var length = document.getElementById("length").value;
	alert("area is " + height*width*length);
	}

function register() {
	var name = prompt("what is your name?");
	if (name == "Jamie") {
		alert("welcome good sir");
		}
	else if (name == "john") {
		alert("where's the pizza, John?");
		}
	else {
		alert("who are you?");
		}
	}

function story() {
	var name = prompt("what is your name?");
	var adverb = prompt("an adverb:");
	var verb = prompt("a verb:");
	prompt("the boy " + name + " " + verb + adverb);
	}