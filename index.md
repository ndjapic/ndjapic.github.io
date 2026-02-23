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

<h2>Објаве</h2>

{% assign current_year = "now" | date: "%Y" | plus: 0 %}
{% assign current_month = "now" | date: "%m" | plus: 0 %}
{% assign prev_year = current_year | minus: 1 %}
{% assign counter = 0 %}

<ul style="list-style: none; padding: 0;">
  {% for post in site.posts %}
    {% assign post_year = post.date | date: "%Y" | plus: 0 %}
    {% assign post_month = post.date | date: "%m" | plus: 0 %}

    {% comment %} Провера услова за приказ (текућа год или прошла год + месец) {% endcomment %}
    {% if post_year == current_year or (post_year == prev_year and post_month >= current_month) %}
      {% if counter < 20 %}
        
        <li style="margin-bottom: 30px;">
          <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>

          <!-- Исечак текста (чист текст до 30 речи) -->
          <div class="excerpt" style="color: #555; font-size: 0.9em; margin-bottom: 10px;">
            {{ post.content | strip_html | truncatewords: 30 }}
          </div>

          <small>
            {% assign m = post.date | date: "%-m" %}
            {{ post.date | date: "%-d." }}
            {% case m %}
              {% when '1' %}јануар {% when '2' %}фебруар {% when '3' %}март
              {% when '4' %}април {% when '5' %}мај {% when '6' %}јун
              {% when '7' %}јул {% when '8' %}август {% when '9' %}септембар
              {% when '10' %}октобар {% when '11' %}новембар {% when '12' %}децембар
            {% endcase %}
            {{ post.date | date: "%Y." }}
          </small>
        </li>

        {% assign counter = counter | plus: 1 %}
      {% endif %}
    {% endif %}
  {% endfor %}
</ul>

<script>
window.onload = function(){

}
</script>
