(function(){
  // category chip filtering
  const chips = document.querySelectorAll(".chip");
  const listItems = document.querySelectorAll(".dm");
  chips.forEach(c => c.addEventListener("click", () => {
    chips.forEach(x => x.setAttribute("aria-pressed","false"));
    c.setAttribute("aria-pressed","true");
    const f = c.dataset.filter;
    listItems.forEach(li => {
      li.style.display = (f==="ALL" || li.dataset.bucket===f) ? "" : "none";
    });
  }));

  // simple search (title + key)
  const q = document.getElementById("q");
  if (q) {
    let data = [];
    fetch("../site_index.json").then(r => r.json()).then(j => data = j).catch(()=>{});
    q.addEventListener("input", () => {
      const s = q.value.trim().toLowerCase();
      document.querySelectorAll(".dm-list .dm").forEach(el => el.style.display = "");
      if (!s) return;
      // hide items not matching
      document.querySelectorAll(".dm-list .dm").forEach(el => {
        const key = (el.querySelector("code")?.textContent || "").toLowerCase();
        const title = (el.querySelector("strong")?.textContent || "").toLowerCase();
        if (!key.includes(s) && !title.includes(s)) el.style.display = "none";
      });
    });
  }
})();