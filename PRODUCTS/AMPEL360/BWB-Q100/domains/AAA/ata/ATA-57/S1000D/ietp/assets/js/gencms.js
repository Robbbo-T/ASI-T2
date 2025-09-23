(function(){
  // Attach to DM pages only (we look for the DM key <code>…)
  const metaCode = document.querySelector(".dm-article .meta code");
  if (!metaCode) return;

  // Add button + panel
  const btn = document.createElement("button");
  btn.id = "gencms-btn"; btn.textContent = "✳︎ Generate draft with GenCMS";
  btn.className = "chip";
  document.querySelector(".topbar").appendChild(btn);

  const panel = document.createElement("div");
  panel.id = "gencms-panel";
  panel.innerHTML = `
  <div class="gencms-box">
    <header><strong>GenCMS</strong><span id="gencms-close">×</span></header>
    <label>Objective <textarea id="gencms-obj" rows="3" placeholder="What should this DM cover?"></textarea></label>
    <label>Constraints <textarea id="gencms-cons" rows="2" placeholder="Standards, scope, limits"></textarea></label>
    <label>Seed outline <textarea id="gencms-seed" rows="4" placeholder="- Intro\n- Steps / checks\n- Acceptance criteria"></textarea></label>
    <label>Safety focus <input id="gencms-safe" placeholder="e.g., H₂ safety, ESD, lock-out/tag-out"></label>
    <div class="row">
      <button id="gencms-run">Generate</button>
      <button id="gencms-promote" disabled>Promote to CSDB</button>
      <a id="gencms-download" download style="display:none">Download XML</a>
    </div>
    <pre id="gencms-out" class="gencms-output">Output will appear here…</pre>
  </div>`;
  document.body.appendChild(panel);

  const close = panel.querySelector("#gencms-close");
  const run   = panel.querySelector("#gencms-run");
  const dl    = panel.querySelector("#gencms-download");
  const promote = panel.querySelector("#gencms-promote");
  let last = null;

  const API = (path)=> (window.GENCMS_API_BASE || "http://localhost:8000") + path;
  btn.onclick = ()=> panel.classList.add("open");
  close.onclick = ()=> panel.classList.remove("open");

  run.onclick = async ()=>{
    run.disabled = true; promote.disabled = true; dl.style.display="none";
    const payload = {
      dmKey: (metaCode.textContent||"").trim(),
      objective: document.getElementById("gencms-obj").value,
      constraints: document.getElementById("gencms-cons").value,
      seed_outline: document.getElementById("gencms-seed").value,
      safety_focus: document.getElementById("gencms-safe").value
    };
    try{
      const r = await fetch(API("/generate"), {
        method:"POST", headers:{ "Content-Type":"application/json" },
        body: JSON.stringify(payload)
      });
      if (!r.ok) throw new Error(await r.text());
      last = await r.json();
      document.getElementById("gencms-out").textContent = last.xml;
      dl.href = "data:text/xml;charset=utf-8,"+encodeURIComponent(last.xml);
      dl.download = last.filename; dl.style.display="inline-block";
      promote.disabled = false;
    }catch(e){
      document.getElementById("gencms-out").textContent = "Error: "+e;
    }finally{
      run.disabled = false;
    }
  };

  promote.onclick = async ()=>{
    if (!last) return;
    promote.disabled = true;
    try{
      const r = await fetch(API("/promote"), {
        method:"POST", headers:{"Content-Type":"application/json"},
        body: JSON.stringify({ dmKey: (metaCode.textContent||"").trim(), draft_path: last.draft_path })
      });
      const j = await r.json();
      document.getElementById("gencms-out").textContent += `\n\nPromoted → ${j.path}`;
    }catch(e){
      document.getElementById("gencms-out").textContent += `\n\nPromote failed: ${e}`;
    }finally{ promote.disabled = false; }
  };
})();