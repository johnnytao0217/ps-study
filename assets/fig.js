// 图解动画：进入视野自动播放一次，点"播放动画"重播。无 JS 或打印时显示静态完整图。
(function () {
  function play(fig) {
    fig.classList.remove('play');
    void fig.offsetWidth;
    fig.classList.add('play');
  }
  var figs = document.querySelectorAll('.fig[data-anim]');
  figs.forEach(function (fig) {
    var b = document.createElement('button');
    b.className = 'replay';
    b.type = 'button';
    b.textContent = '▶ 播放动画';
    b.addEventListener('click', function () { play(fig); });
    fig.appendChild(b);
  });
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) { play(e.target); io.unobserve(e.target); }
      });
    }, { threshold: 0.4 });
    figs.forEach(function (f) { io.observe(f); });
  }

  // 气体分子运动模拟（Day 10 / 12）：活塞来回移动，统计撞墙次数
  document.querySelectorAll('svg[data-kmt]').forEach(function (svg) {
    if (window.matchMedia && window.matchMedia('print').matches) return;
    var dots = Array.prototype.slice.call(svg.querySelectorAll('circle.p'));
    var piston = svg.querySelector('.piston');
    var readout = svg.querySelector('.hits');
    var vol = svg.querySelector('.vol');
    var L = +svg.dataset.left, T = +svg.dataset.top, B = +svg.dataset.bottom;
    var maxX = +svg.dataset.right, minX = +svg.dataset.min;
    var st = dots.map(function (d, i) {
      var a = i * 2.399;
      return { el: d, x: +d.getAttribute('cx'), y: +d.getAttribute('cy'), vx: Math.cos(a) * 1.6, vy: Math.sin(a) * 1.6 };
    });
    var t0 = performance.now(), hits = 0, last = t0, rate = 0;
    function step(now) {
      var ph = ((now - t0) / 9000) % 1;
      var k = ph < 0.5 ? ph * 2 : 2 - ph * 2;
      var px = maxX - (maxX - minX) * (0.5 - 0.5 * Math.cos(Math.PI * k));
      piston.setAttribute('x', px);
      st.forEach(function (s) {
        s.x += s.vx; s.y += s.vy;
        if (s.x < L + 4) { s.x = L + 4; s.vx = Math.abs(s.vx); hits++; }
        if (s.x > px - 4) { s.x = px - 4; s.vx = -Math.abs(s.vx); hits++; }
        if (s.y < T + 4) { s.y = T + 4; s.vy = Math.abs(s.vy); hits++; }
        if (s.y > B - 4) { s.y = B - 4; s.vy = -Math.abs(s.vy); hits++; }
        s.el.setAttribute('cx', s.x.toFixed(1)); s.el.setAttribute('cy', s.y.toFixed(1));
      });
      if (now - last > 1000) {
        rate = hits; hits = 0; last = now;
        if (readout) readout.textContent = '每秒碰撞器壁 ≈ ' + rate + ' 次';
      }
      if (vol) vol.textContent = '体积 V ≈ ' + Math.round((px - L) / (maxX - L) * 100) + '%';
      requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  });
})();
