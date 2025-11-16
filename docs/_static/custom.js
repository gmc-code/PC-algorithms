function toTitleCase(str) {
  return str.toLowerCase().replace(/\b\w/g, c => c.toUpperCase());
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".highlight-vcaapseudocode .n, .highlight-vcaapseudocode .k")
    .forEach(el => {
      el.textContent = toTitleCase(el.textContent.replace(/_/g, " "));
    });
});
