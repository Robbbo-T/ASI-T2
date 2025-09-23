<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
 <xsl:output method="html" indent="yes" />
 <xsl:template match="/">
  <div>
    <h2><xsl:value-of select="/*/identAndStatusSection/pmAddress/pmTitle"/> <xsl:text> </xsl:text>
        <small>(<xsl:value-of select="name(/*)"/>)</small></h2>
    <table border="0" cellspacing="0" cellpadding="4">
      <tr><th align="left">Code</th><td><xsl:value-of select="/*/identAndStatusSection/pmAddress/pmCode"/></td></tr>
      <tr><th align="left">Issue</th><td><xsl:value-of select="/*/identAndStatusSection/pmAddress/issueInfo/issueNumber"/></td></tr>
      <tr><th align="left">Language</th><td><xsl:value-of select="/*/@language"/></td></tr>
    </table>
    <hr/>
    <div>
      <xsl:apply-templates select="/*/*[not(self::identAndStatusSection)]"/>
    </div>
  </div>
 </xsl:template>

 <xsl:template match="*">
   <div style="margin: .3rem 0;">
    <strong><xsl:value-of select="name()"/></strong>
    <xsl:if test="normalize-space(text())">
      <div><xsl:value-of select="normalize-space(text())"/></div>
    </xsl:if>
    <xsl:apply-templates select="*"/>
   </div>
 </xsl:template>
</xsl:stylesheet>
