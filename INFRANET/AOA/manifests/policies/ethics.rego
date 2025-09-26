package aoa.ethics

deny[msg] {
  input.intent == "Assess marine habitat health during BWB-Q100 coastal approach"
  not input.flags.MARINE_PROTECTED
  msg := "Ethics gate: MARINE_PROTECTED must be true in protected zones"
}

deny[msg] {
  input.dataResidency != "EU"
  msg := "Data residency must remain in EU for this mission"
}