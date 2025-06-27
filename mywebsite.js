let = username;

document.getElementById("mysubmit").onclick = function(){
    username = document.getElementById("myname").value
    document.getElementById("myH1").textContent = `Hi you are +${username}`
}