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

<h2>Објаве</h2>

<ul>
  {% for post in site.posts %}
    <li>
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>

      <!-- Приказ исечка текста -->
      <div class="excerpt" style="color: #555; font-size: 0.9em; margin-bottom: 10px;">
        {{ post.excerpt | strip_html | truncatewords: 30 }}
      </div>

      <small>
        <!-- Овде почиње превод датума за сваки пост појединачно {{ post.date | date: "%d.%m.%Y." }} -->
        {% assign month = post.date | date: "%-m" %}
        {{ post.date | date: "%-d." }}
        {% case month %}
          {% when '1' %}јануар {% when '2' %}фебруар {% when '3' %}март
          {% when '4' %}април {% when '5' %}мај {% when '6' %}јун
          {% when '7' %}јул {% when '8' %}август {% when '9' %}септембар
          {% when '10' %}октобар {% when '11' %}новембар {% when '12' %}децембар
        {% endcase %}
        {{ post.date | date: "%Y." }}
      </small>
    </li>
  {% endfor %}
</ul>

<script>
window.onload = function(){

}
</script>
