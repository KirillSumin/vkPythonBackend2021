BASE_SITE_PATH = document.location.origin

function redirectToUrl(event){
    document.location.href = BASE_SITE_PATH + '/' + this.url + '/';
}

function setRedirectUrlOnClick(item, url){
    item.addEventListener('click', {handleEvent: redirectToUrl, url: url});
}

function changeBackgroundColorToBase(event){
    event.currentTarget.style.backgroundColor = this.base_background_color
}

function changeBackgroundColorToHighlight(event){
    event.currentTarget.style.backgroundColor = this.highlight_color
}

function setHighlightOnHover(item, highlight_color){
    base_background_color = item.style.backgroundColor
    item.addEventListener('mouseout', {handleEvent: changeBackgroundColorToBase,
    base_background_color: base_background_color});
    item.addEventListener('mouseover', {handleEvent: changeBackgroundColorToHighlight,
     highlight_color: highlight_color});
}

let youtube_btn = document.querySelector('.youtube');
let files_btn = document.querySelector('.files');
let music_btn = document.querySelector('.music');
let iot_btn = document.querySelector('.iot');
let settings_btn = document.querySelector('.settings');
let exit_btn = document.querySelector('.exit');

all_btns = document.querySelectorAll('.btn')

for(let index=0;index<all_btns.length;index++){
    // console.log(all_btns[index])
    all_btns[index].style.cursor = "pointer";
    setHighlightOnHover(all_btns[index], '#ffcc00')
}

setRedirectUrlOnClick(youtube_btn, 'syncYoutube')
setRedirectUrlOnClick(exit_btn, 'logout')