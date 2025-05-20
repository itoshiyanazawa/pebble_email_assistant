const chat = document.getElementById("chat");
const input = document.getElementById("input");
const sendBtn = document.getElementById("send");
const status = document.getElementById("status");
const copyStatus = document.getElementById("copy-status");

let lastBotReply = "";

function appendMessage(text, sender) {
  const msg = document.createElement("div");
  msg.className = "message " + sender;
  msg.innerText = text;
  chat.appendChild(msg);
  chat.scrollTop = chat.scrollHeight;
}

sendBtn.onclick = async () => {
  const userText = input.value.trim();
  if (!userText) return;

  appendMessage(userText, "user");
  input.value = "";
  status.innerText = "⏳ Generating...";

  try {
    const response = await fetch("https://email-assistant-9lmk.onrender.com/revise", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: userText })
    });

    if (!response.ok) throw new Error("Server error");

    const data = await response.json();
    lastBotReply = data.revised;
    appendMessage(lastBotReply, "bot");
    status.innerText = "✅ Done";
  } catch (err) {
    appendMessage("Sorry, I couldn’t connect to the server.", "bot");
    status.innerText = "❌ Error";
  }

  setTimeout(() => status.innerText = "", 2000);
};

document.getElementById("copy").onclick = () => {
  if (!lastBotReply) return;
  navigator.clipboard.writeText(lastBotReply).then(() => {
    copyStatus.innerText = "✅ Copied!";
    setTimeout(() => copyStatus.innerText = "", 1500);
  });
};
