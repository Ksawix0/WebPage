let cookies={}
if (document.cookie.length > 0){
    document.cookie.split('; ').forEach( cookie  => {
        let values = cookie.split('=')
        cookies[values[0]] = values.slice(1).join('')
    })
}

let site_name
url = location.href.split('?')[0].split('/')
site_name = url[url.length - 2]
document.addEventListener('DOMContentLoaded', () => {
    let list = document.getElementById('list')
    listing(cookies['old_list'].split(','), list)
})

fetch("../scripts/list.json")
    .then(response => response.json())
    .then(json => {
        let list = document.getElementById('list')
        console.log(json, list)
        listing(json['list'][site_name],list)
        cookies['old_list'] = json["list"][site_name].join(",")
        save_cookies()
    })

function save_cookies() {
    let cookiess = []
    Object.keys(cookies).forEach(key => {
        cookiess.push(key + "=" + cookies[key])
        document.cookie = cookiess.join("; ")
    })
}

function listing(list_f, list){
    list.innerHTML = ''
    for (let i=0 ;i < list_f.length ;i++){
        list.innerHTML += "<li style=\"text-align: left; padding-left: var(--rem_padding);\"><a href=\"" + list_f[i] + "\" style=\"font-size: larger; color: white\">" + list_f[i] + "</a></li>"
    }
}