window.onload = function(){
  var node;
  function eventFire(el, etype){
    if (el.fireEvent) {
      el.fireEvent('on' + etype);
    } else {
      var evObj = document.createEvent('Events');
      evObj.initEvent(etype, true, false);
      el.dispatchEvent(evObj);
    }
  }
  function handler(evt) {
    evt = evt || window.event;
    var targ = evt.target || evt.srcElement;
    if (targ.nodeType == 3) targ = targ.parentNode; // defeat Safari bug
    var sty = targ.nextSibling.style;
    sty.display = (sty.display != 'none') ? 'none' : 'block';
  }
  var ols = document.getElementsByTagName('ol');
  for(var rbr = 0; rbr < ols.length; rbr++){
    node = ols[rbr].previousSibling;
    node.onclick = handler;
    eventFire(node, 'click');
  }
};
