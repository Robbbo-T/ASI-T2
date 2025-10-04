<schema xmlns="http://purl.oclc.org/dsdl/schematron">
  <pattern id="dmc-ata-align">
    <rule context="/dmodule/identAndStatusSection/dmAddress/dmIdent/dmCode">
      <let name="sc"   value="@systemCode"/>
      <let name="ssc"  value="@subSystemCode"/>
      <let name="sssc" value="@subSubSystemCode"/>
      <assert test="matches(base-uri(/), concat('/domains/IIS/'))">
        El DMC debe residir bajo /domains/IIS/.
      </assert>
      <assert test="matches(base-uri(/), concat('/', $sc, '-', $ssc, '-', $sssc, '/'))">
        La ruta debe reflejar el ATA del dmCode (…/<SC>-<SSC>-<SSSC>/…).
      </assert>
    </rule>
  </pattern>
</schema>
