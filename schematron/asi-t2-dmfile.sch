<?xml version="1.0" encoding="UTF-8"?>
<!--
  ASI-T2 DMC Filename Policy Schematron Rules
  
  Enforces S1000D DMC filename conventions and ATA path alignment.
  Use this alongside your BREX DM for CSDB validation.
  
  Note: These rules assume the CSDB can access document-uri().
  If not available, bind the physical filename to a meta element
  on ingest and adapt the test accordingly.
-->
<schema xmlns="http://purl.oclc.org/dsdl/schematron">
  
  <title>ASI-T2 DMC Filename Convention and ATA Path Alignment</title>
  
  <ns prefix="s1000d" uri="http://www.s1000d.org/S1000D_5-0"/>
  
  <pattern id="dmc-filename-policy">
    <title>DMC filename convention (S1000D Issue 5.0/6.0)</title>
    <rule context="/dmodule | /s1000d:dmodule">
      <!-- 
        Check physical filename via processing instruction or CSDB metadata binding.
        Pattern: DMC-<MIC>-<SDC>-<SC>-<SSC>-<SSSC>-<AC><DAC>-<IC><ICV>-<ILC>-<LANG>-<COUNTRY>.xml
      -->
      <assert test="matches(document-uri(/),
        'DMC-[A-Z0-9]{3,4}-[A-Z]-\d{2}-\d{2}-\d{2}-\d{2}[A-Z]-\d{3}[A-Z]-[A-Z]-[A-Z]{2}-[A-Z]{2}\.xml$')">
        DMC filename not compliant with S1000D pattern.
        Expected: DMC-&lt;MIC&gt;-&lt;SDC&gt;-&lt;SC&gt;-&lt;SSC&gt;-&lt;SSSC&gt;-&lt;AC&gt;&lt;DAC&gt;-&lt;IC&gt;&lt;ICV&gt;-&lt;ILC&gt;-&lt;LANG&gt;-&lt;COUNTRY&gt;.xml
      </assert>
    </rule>
  </pattern>

  <pattern id="dmc-ata-path-alignment">
    <title>Folder ATA path must match dmCode structure</title>
    <rule context="/dmodule/identAndStatusSection/dmAddress/dmIdent/dmCode | 
                   /s1000d:dmodule/s1000d:identAndStatusSection/s1000d:dmAddress/s1000d:dmIdent/s1000d:dmCode">
      <!-- 
        Extract SC/SSC/SSSC from dmCode and compare to folder path segments.
        Expected folder structure: .../SC-SSC-SSSC/...
        
        Note: This is a simplified check. Full validation should also verify
        the complete path hierarchy matches organizational structure.
      -->
      <let name="sc"   value="@systemCode"/>
      <let name="ssc"  value="@subSystemCode"/>
      <let name="sssc" value="@subSubSystemCode"/>
      
      <assert test="matches(document-uri(/),
        concat('.*/', $sc, '-', $ssc, '-', $sssc, '/'))">
        Folder ATA path and dmCode mismatch.
        Expected folder path to contain: <value-of select="concat($sc, '-', $ssc, '-', $sssc)"/>
        Actual path: <value-of select="document-uri(/)"/>
      </assert>
    </rule>
  </pattern>
  
  <pattern id="dmc-ata-chapter-57">
    <title>Validate Chapter 57 (Wings) structure</title>
    <rule context="/dmodule/identAndStatusSection/dmAddress/dmIdent/dmCode[@systemCode='57'] | 
                   /s1000d:dmodule/s1000d:identAndStatusSection/s1000d:dmAddress/s1000d:dmIdent/s1000d:dmCode[@systemCode='57']">
      <!--
        For Chapter 57 (Wings), ensure subSystemCode is valid.
        Common subcodes: 10 (Wing Structure), 20 (Wing Tips), 30 (Wing Trailing Edge), etc.
      -->
      <assert test="@subSystemCode castable as xs:integer and 
                    number(@subSystemCode) >= 0 and 
                    number(@subSystemCode) <= 99">
        ATA Chapter 57 subSystemCode must be a valid 2-digit number (00-99).
        Found: <value-of select="@subSystemCode"/>
      </assert>
    </rule>
  </pattern>

  <pattern id="dmc-mic-consistency">
    <title>Model Identification Code (MIC) consistency</title>
    <rule context="/dmodule/identAndStatusSection/dmAddress/dmIdent/dmCode | 
                   /s1000d:dmodule/s1000d:identAndStatusSection/s1000d:dmAddress/s1000d:dmIdent/s1000d:dmCode">
      <!--
        Verify MIC in filename matches modelIdentCode in dmCode.
        This ensures traceability between filename and internal metadata.
      -->
      <let name="mic" value="@modelIdentCode"/>
      <assert test="matches(document-uri(/), 
        concat('^.*/DMC-', $mic, '-'))">
        MIC in filename does not match dmCode/@modelIdentCode.
        Expected MIC: <value-of select="$mic"/>
      </assert>
    </rule>
  </pattern>

</schema>
