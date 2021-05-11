console.log('connected!!!')
let test = 'HIHIHIHi'

function scrollToBottom() {
  let messages = document.querySelector('#chat-log').lastElementChild
  console.log(messages)
  messages.scrollIntoView()
}