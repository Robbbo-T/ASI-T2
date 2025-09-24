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
    <div class="prefill-row">
      <button id="gencms-prefill">📋 Auto-fill from context</button>
    </div>
    <label>Objective <textarea id="gencms-obj" rows="3" placeholder="What should this DM cover?"></textarea></label>
    <label>Constraints <textarea id="gencms-cons" rows="2" placeholder="Standards, scope, limits"></textarea></label>
    <label>Seed outline <textarea id="gencms-seed" rows="4" placeholder="- Intro\n- Steps / checks\n- Acceptance criteria"></textarea></label>
    <label>Safety focus <input id="gencms-safe" placeholder="e.g., H₂ safety, ESD, lock-out/tag-out"></label>
    <div class="row">
      <button id="gencms-run">Generate</button>
      <button id="gencms-refine" disabled>Refine</button>
      <button id="gencms-promote" disabled>Promote to CSDB</button>
      <a id="gencms-download" download style="display:none">Download XML</a>
    </div>
    <pre id="gencms-out" class="gencms-output">Output will appear here…</pre>
  </div>`;
  document.body.appendChild(panel);

  const close = panel.querySelector("#gencms-close");
  const prefill = panel.querySelector("#gencms-prefill");
  const run   = panel.querySelector("#gencms-run");
  const refine = panel.querySelector("#gencms-refine");
  const dl    = panel.querySelector("#gencms-download");
  const promote = panel.querySelector("#gencms-promote");
  let last = null;

  const API = (path)=> (window.GENCMS_API_BASE || "http://localhost:8000") + path;
  btn.onclick = ()=> panel.classList.add("open");
  close.onclick = ()=> panel.classList.remove("open");

  // Auto-prefill functionality
  prefill.onclick = async ()=>{
    prefill.disabled = true;
    try{
      const r = await fetch(API("/prefill"), {
        method:"POST", headers:{ "Content-Type":"application/json" },
        body: JSON.stringify({ dmKey: (metaCode.textContent||"").trim() })
      });
      if (!r.ok) throw new Error(await r.text());
      const data = await r.json();
      document.getElementById("gencms-obj").value = data.objective;
      document.getElementById("gencms-cons").value = data.constraints;
      document.getElementById("gencms-seed").value = data.seed_outline;
      document.getElementById("gencms-safe").value = data.safety_focus;
    }catch(e){
      document.getElementById("gencms-out").textContent = "Prefill error: "+e;
    }finally{
      prefill.disabled = false;
    }
  };

  run.onclick = async ()=>{
    run.disabled = true; promote.disabled = true; refine.disabled = true; dl.style.display="none";
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
      refine.disabled = false;
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

  refine.onclick = async ()=>{
    if (!last) return;
    refine.disabled = true;
    try{
      // Extract just the content portion for refinement
      const contentMatch = last.xml.match(/<content>[\s\S]*<\/content>/);
      const contentToRefine = contentMatch ? contentMatch[0] : last.xml;
      
      const r = await fetch(API("/refine"), {
        method:"POST", headers:{"Content-Type":"application/json"},
        body: JSON.stringify({ 
          dmKey: (metaCode.textContent||"").trim(), 
          xml_content: contentToRefine,
          feedback: "" 
        })
      });
      if (!r.ok) throw new Error(await r.text());
      const refined = await r.json();
      
      // Replace the content in the original XML with the refined version
      const updatedXml = last.xml.replace(/<content>[\s\S]*<\/content>/, refined.xml);
      last.xml = updatedXml;
      
      document.getElementById("gencms-out").textContent = last.xml + `\n\n--- Refinement Applied ---\n${refined.improvements}`;
      dl.href = "data:text/xml;charset=utf-8,"+encodeURIComponent(last.xml);
    }catch(e){
      document.getElementById("gencms-out").textContent += `\n\nRefine failed: ${e}`;
    }finally{ refine.disabled = false; }
  };
})();