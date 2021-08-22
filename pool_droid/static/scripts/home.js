document.querySelector('.relays').addEventListener('click', relayClick);

function relayClick(e) {
  let node = e.target;
  let tgt = null;
  while(node !== this){
      if(node.classList.contains("relay")){
          tgt = node.children[0];
          break;
      }
      node = node.parentNode;
  }
  if(tgt !== null) {
      if (tgt.classList.contains('fa-toggle-on')) {
          console.log('Turn off relay: ' + tgt.parentNode.id);
          tgt.classList.replace('fa-toggle-on', 'fa-toggle-off');
      } else if (tgt.classList.contains('fa-toggle-off')) {
          console.log('Turn on relay: ' + tgt.parentNode.id);
          tgt.classList.replace('fa-toggle-off', 'fa-toggle-on');
      }
  }
}

document.querySelector('.pump-modes').addEventListener('click', pumpModeClick);

function pumpModeClick(e) {
  let node = e.target;
  let tgt = null;
  while(node !== this){
      if(node.classList.contains("pump-mode")){
          tgt = node;
          break;
      }
      node = node.parentNode;
  }
  if(tgt !== null) {
      changePumpMode(tgt.id.slice(10))
      document.querySelectorAll(".pump-mode").forEach(function(pumpMode) {
          if (tgt === pumpMode) {
              console.log('Turn on pump mode: ' + pumpMode.id);
              pumpMode.classList.replace('pump-mode-inactive', 'pump-mode-active');
          }
          else {
              console.log('Turn off pump mode: ' + pumpMode.id);
              pumpMode.classList.replace('pump-mode-active', 'pump-mode-inactive');
          }
      })
  }
}

async function postData(url = '', data = {}) {
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
    });
    return response.json();
}

function changePumpMode(pumpMode) {
    postData('{% url "ajax-pump-mode" %}', {'pump-mode': pumpMode})
    .then(data => {
        console.log(data);
    })
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
