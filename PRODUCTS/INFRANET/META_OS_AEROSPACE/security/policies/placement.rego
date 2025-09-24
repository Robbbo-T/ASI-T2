package placement

deny[msg] {
  input.asset.constraints.partition == "DAL-A"
  not input.asset.image.sbom.contains("MISRA-C")
  msg := sprintf("Asset %s requiere MISRA-C verificado para DAL-A", [input.asset.id])
}