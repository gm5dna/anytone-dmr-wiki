// Add an Internet Archive fallback after every external link in page content.
document$.subscribe(() => {
  document.querySelectorAll(".md-content a[href^='http']").forEach(a => {
    if (a.closest(".md-content__button, .md-source, .md-tag") || /github\.com\/gm5dna/.test(a.href) || a.host === location.host || a.host.endsWith("archive.org") || a.dataset.arch || a.querySelector("img")) return;
    a.dataset.arch = 1;
    const w = document.createElement("a");
    w.href = "https://web.archive.org/web/2/" + a.href;
    w.textContent = "archive";
    w.className = "archive-link";
    w.title = "Internet Archive copy";
    a.after(" ", w);
  });
});
