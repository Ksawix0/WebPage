
let site_name
url = location.href.split('?')[0].split('/')
if (url[url.length - 1].endsWith('.html')) {
    site_name = url[url.length - 2]
}
else{
    site_name = url[url.length - 1]
}

fetch("../scripts/list.json")
    .then(response => response.json())
    .then(json => {


        let list = document.getElementById('list')
        list.innerHTML = ""
        console.log(json)
        for (let i=0 ;i < json["list"][site_name].length ;i++){
            list.innerHTML += "<li style=\"text-align: left; padding-left: 5%;\"><a href=\"" + json["list"][site_name][i] + "\" style=\"font-size: larger; color: white\">" + json["list"][site_name][i] + "</a></li>"
        }

    })
