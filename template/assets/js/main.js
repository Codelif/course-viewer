(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    if (all) {
      select(el, all).forEach(e => e.addEventListener(type, listener))
    } else {
      select(el, all).addEventListener(type, listener)
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Sidebar toggle
   */
  if (select('.toggle-sidebar-btn')) {
    on('click', '.toggle-sidebar-btn', function(e) {
      select('body').classList.toggle('toggle-sidebar')
    })
  }

  /**
   * Search bar toggle
   */
  if (select('.search-bar-toggle')) {
    on('click', '.search-bar-toggle', function(e) {
      select('.search-bar').classList.toggle('search-bar-show')
    })
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select('#header')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add('header-scrolled')
      } else {
        selectHeader.classList.remove('header-scrolled')
      }
    }
    window.addEventListener('load', headerScrolled)
    onscroll(document, headerScrolled)
  }
 

})();

function removeAllChildNodes(parent) {
  while (parent.firstChild) {
      parent.removeChild(parent.firstChild);
  };
};

function showVideo(video_path){
  if ($("#course-video").length != 0){
  videojs("course-video").dispose();
  }
  let section = document.querySelector(".section");
  removeAllChildNodes(section);

  let container = document.createElement('div');
  container.setAttribute("class", "container");

  let video = document.createElement('video');
  video.setAttribute("id", "course-video");
  video.setAttribute("class", "video-js vjs-theme-forest");

  container.appendChild(video);
  section.appendChild(container);

  let vjs = videojs("course-video", {
    playbackRates: [0.5, 1, 1.5, 2],
    fluid: true,
    controls: true,
    preload: true,
    autoplay: true
  });

  vjs.src({
    type: "video/mp4",
    src: video_path
  });
};

function showHTML(html_path){
  if ($("#course-video").length != 0){
    videojs("course-video").dispose();
    }
  let section = document.querySelector(".section");
  removeAllChildNodes(section);

  let container = document.createElement('div');
  container.setAttribute("class", "iframe-container");

  let iframe = document.createElement('iframe');
  iframe.setAttribute("class", "responsive-iframe");
  iframe.setAttribute("src", html_path);
  iframe.setAttribute("frameborder", "0");

  container.appendChild(iframe);
  section.appendChild(container);
};

function changeScene(element){
  if (!element.classList.contains('active')){

  // remove active element
  let activeList = document.getElementsByClassName('active')
    if (activeList.length !== 0){
    activeList[0].classList.remove('active')
  }

  // add active class to current element
  element.classList.add('active')

  var trace = [];
  var end = false;
  var node = element

  trace.push(element.getAttribute("path"))

  while (!end){
    if (node.parentElement.parentElement.getAttribute("id") == "sidebar-nav"){
      end = true;
      break;
    }
    node = node.parentElement.parentElement.parentElement.parentElement
    trace.push(node.firstElementChild.innerText)
  }
  trace.reverse()

  let path = parentFolder+trace.join("/")
  let type = element.getAttribute("type")
  let title = element.getAttribute("title")

  $(".pagetitle > h1").text(title)

  if (type == "video"){
    showVideo(path)
  }else{
    showHTML(path)
  }
  element.scrollIntoView({behavior: "smooth", block: "end", inline: "nearest"});
  }
}




function prevScene() {
  let active = document.getElementsByClassName('active')[0]

  if (active != undefined){
    let prevElement = active.previousElementSibling;
    if (prevElement != null){
      changeScene(prevElement)
    }
  }
}

function nextScene() {
  let active = document.getElementsByClassName('active')[0]

  if (active != undefined){
    let nextElement = active.nextElementSibling;
    if (nextElement != null){
      changeScene(nextElement)
    }
  }
}


document.onkeypress = function (e) {
    var evt = window.event || e;
    switch (evt.keyCode) {
      case 110:  
        nextScene();
        break;
      case 112:
        prevScene();
        break;

    }
}


// showVideo("/tmp/NiceAdmin/1 - Table of Contents.mp4");
// showHTML("/project/template/1.html")

