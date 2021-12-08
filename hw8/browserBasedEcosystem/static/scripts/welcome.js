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


let github_auth_btn = document.querySelector('.githubAuth');
let base_auth_btn = document.querySelector('.baseAuth');

all_btns = document.querySelectorAll('.btn')

for(let index=0;index<all_btns.length;index++){
    // console.log(all_btns[index])
    all_btns[index].style.cursor = "pointer";
    setHighlightOnHover(all_btns[index], '#ffcc00')
}

github_auth_btn.addEventListener('click',  
    ()=>{window.location.href = GITHUB_AUTH_URL;}) //watch welcome.html for details
