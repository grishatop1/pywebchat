var input = document.getElementById("msg-txt");

input.addEventListener("keyup", function(event) {
	if (event.keyCode === 13) {
		event.preventDefault();
		sendMessage(getValueFromInput(true));
	}
});

var sndbtn = document.getElementById("snd-btn");
sndbtn.addEventListener("click", function(){
	sendMessage(getValueFromInput(true));
});

function getValueFromInput(clear) {
	msg = document.getElementById("msg-txt");
	data = msg.value;
	if (clear) {
		msg.value = "";
	};
	return data;
};

function addMessage(message, mine, date, sender) {
	if (isEmpty(message)) return;
	var log = document.getElementsByClassName("log")[0];
	var box = document.getElementsByClassName("text-area")[0];

	var messagecontainer = document.createElement("div");
	if (mine == "true") {
		messagecontainer.className = "message-container message-mine";
	} else {
		messagecontainer.className = "message-container message-other";
		var h4 = document.createElement("h4");
		h4.innerHTML = sender;
		messagecontainer.appendChild(h4);
	};
	

	var messagebox = document.createElement("div");
	messagebox.className = "message";
	messagebox.innerHTML = message;

	messagecontainer.appendChild(messagebox);
	log.appendChild(messagecontainer);

	box.scrollTop = box.scrollHeight;
};

function isEmpty(str) {
	return (!str || 0 === str.length);
};