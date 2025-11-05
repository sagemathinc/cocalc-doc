document.addEventListener('DOMContentLoaded', function () {
  var banner = document.querySelector('.cocalcbanner');
  var navContent = document.querySelector('.wy-nav-content');

  if (!banner || !navContent) {
    return;
  }

  function updateBannerPosition() {
    var rect = navContent.getBoundingClientRect();
    var viewportWidth = document.documentElement.clientWidth || window.innerWidth;
    var offset = Math.max(viewportWidth - rect.right, 0);
    banner.style.right = offset + 'px';
  }

  updateBannerPosition();

  window.addEventListener('resize', updateBannerPosition, { passive: true });
  window.addEventListener('scroll', updateBannerPosition, { passive: true });
});
