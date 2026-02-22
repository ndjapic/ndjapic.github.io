---
layout: default
title: "Почетна"
---
<h1>Почетна страница</h1>

<p><a href="http://jsbin.com/zayopa">Каталог</a> линкова из математике.</p>

<p>Наставни план и програм за предмет Математика за
<a href="https://github.com/ndjapic/ndjapic.github.io/wiki/mat5">5</a>,
<a href="https://github.com/ndjapic/ndjapic.github.io/wiki/mat6">6</a>,
<a href="https://github.com/ndjapic/ndjapic.github.io/wiki/mat7">7</a>,
<a href="https://github.com/ndjapic/ndjapic.github.io/wiki/mat8">8</a>
разред.</p>

<p>Наставни план и програм за предмет Информатика и рачунарство за
<a href="https://github.com/ndjapic/ndjapic.github.io/wiki/inf7">7</a>,
<a href="https://github.com/ndjapic/ndjapic.github.io/wiki/inf8">8</a>
разред.</p>

<p>Куцано у маркдаун фајлу.</p>

<h2>Моје објаве:</h2>
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a> 
      ({{ post.date | date: "%d.%m.%Y." }})
    </li>
  {% endfor %}
</ul>

<script>
window.onload = function(){

}
</script>
