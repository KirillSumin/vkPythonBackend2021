let tag = document.createElement("script");

tag.src = "https://www.youtube.com/iframe_api";
let firstScriptTag = document.getElementsByTagName("script")[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

let player;
function onYouTubeIframeAPIReady() {
  player = new YT.Player("player", {
    width: "1280",
    height: "720",
    videoId: video_id,
    playerVars: { autoplay: 1 },
    events: {
      onReady: onPlayerReady,
      onStateChange: onPlayerStateChange,
    },
  });
}

function onPlayerReady(event) {
  //player.getAvailableQualityLevels()[0]
  event.target.setPlaybackQuality("hd720");
  //player.setSize(1280, 720)
  //event.target.playVideo();
  //event.target.playVideo();
  let timerId = setInterval(showTime, 2);
}

// let done = false;
function onPlayerStateChange(event) {
  //   if (event.data == YT.PlayerState.PLAYING && !done) {
  // setTimeout(stopVideo, 6000);
  // done = true;
  //   }
}
function stopVideo() {
  player.stopVideo();
}

function showTime() {
//   console.log(player.getCurrentTime());
}

BASE_SITE_PATH = 'http://127.0.0.1:8000/'

function redirectToUrl(event){
 window.location.href =
      BASE_SITE_PATH +
      this.url + '/';
}

function setRedirectUrlOnClick(item, url){
    item.addEventListener('click', {handleEvent: redirectToUrl, url: url});
}

function changeBackgroundColorToBase(event){
    event.currentTarget.style.backgroundColor = this.base_background_color;
}

function changeBackgroundColorToHighlight(event){
    event.currentTarget.style.backgroundColor = this.highlight_color;
}

function setHighlightOnHover(item, highlight_color){
    base_background_color = item.style.backgroundColor
    item.addEventListener('mouseout', {handleEvent: changeBackgroundColorToBase,
    base_background_color: base_background_color});
    item.addEventListener('mouseover', {handleEvent: changeBackgroundColorToHighlight,
     highlight_color: highlight_color});
}

let choose_youtube_btn = document.querySelector('.choose-youtube');
let return_control_btn = document.querySelector('.return-control');

all_btns = document.querySelectorAll('.btn');

for(let index=0;index<all_btns.length;index++){
    console.log(all_btns[index]);
    all_btns[index].style.cursor = "pointer";
    setHighlightOnHover(all_btns[index], '#ffcc00');
}

choose_youtube_btn.addEventListener('click', (event)=>{
    window.location.href = 'https://www.youtube.com';})

setRedirectUrlOnClick(return_control_btn, 'control');
