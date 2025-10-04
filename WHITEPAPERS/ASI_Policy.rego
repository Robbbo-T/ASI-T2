# ASI Policy-as-Code
# Open Policy Agent (OPA) Rego Implementation
# Version: 0.1.0
# Date: 2025-10-03
# Classification: PUBLIC

package asi.policy

import future.keywords.contains
import future.keywords.if
import future.keywords.in

# ==============================================================================
# CORE PRINCIPLES ENFORCEMENT
# ==============================================================================

# Safety-First: Block any request that could compromise aviation safety
deny[msg] {
	input.request.safety_critical == true
	not input.request.human_approval_received
	msg := sprintf("Safety-critical action requires human approval (ASI Constitution: safety_first). Request ID: %v", [input.request.id])
}

deny[msg] {
	input.request.intent == "control"
	msg := sprintf("Live control prohibited by ASI Constitution (authority_boundaries.no_live_control). Request ID: %v", [input.request.id])
}

# ==============================================================================
# AUTHORITY BOUNDARIES
# ==============================================================================

# No Live Control: Prevent any control commands to physical systems
deny[msg] {
	input.request.target_system in ["flight_control", "propulsion", "atc", "gse", "test_rig"]
	input.request.action in ["command", "control", "activate", "deactivate", "modify_state"]
	msg := sprintf("Live control of %v prohibited (authority_boundaries.no_live_control). Request ID: %v", [input.request.target_system, input.request.id])
}

deny[msg] {
	contains(lower(input.request.query), "set autopilot")
	msg := sprintf("Autopilot control prohibited (authority_boundaries.no_live_control). Request ID: %v", [input.request.id])
}

deny[msg] {
	contains(lower(input.request.query), "command flight control")
	msg := sprintf("Flight control command prohibited (authority_boundaries.no_live_control). Request ID: %v", [input.request.id])
}

# No Certified Software Modifications
deny[msg] {
	input.request.target_system in ["onboard_software", "flight_software", "fadec", "avionics_config"]
	input.request.action in ["modify", "patch", "update", "delete"]
	not input.request.certification_authority_approval
	msg := sprintf("Modification of certified software prohibited without certification authority approval (authority_boundaries.no_certified_modifications). Request ID: %v", [input.request.id])
}

deny[msg] {
	input.request.software_dal in ["A", "B"]
	input.request.action == "modify"
	not input.request.do178c_analysis_complete
	msg := sprintf("DO-178C change impact analysis required for DAL %v software (authority_boundaries.no_certified_modifications). Request ID: %v", [input.request.software_dal, input.request.id])
}

# No Certification Process Bypass
deny[msg] {
	input.request.bypass_certification == true
	msg := sprintf("Certification process bypass prohibited (authority_boundaries.no_certification_bypass). Request ID: %v", [input.request.id])
}

deny[msg] {
	input.request.action in ["approve", "certify", "authorize"]
	input.request.context == "type_certification"
	not input.request.regulatory_authority in ["EASA", "FAA"]
	msg := sprintf("Only aviation authorities can approve certification (authority_boundaries.no_certification_bypass). Request ID: %v", [input.request.id])
}

deny[msg] {
	contains(lower(input.request.query), "skip certification")
	msg := sprintf("Certification skip prohibited (authority_boundaries.no_certification_bypass). Request ID: %v", [input.request.id])
}

deny[msg] {
	contains(lower(input.request.query), "bypass do-178")
	msg := sprintf("DO-178C bypass prohibited (authority_boundaries.no_certification_bypass). Request ID: %v", [input.request.id])
}

# No Export Control Violations
deny[msg] {
	input.request.content_classification in ["ITAR", "EAR_CONTROLLED", "EU_DUAL_USE"]
	not input.request.export_authorization_valid
	msg := sprintf("Export-controlled content requires valid authorization (authority_boundaries.no_export_violations). Request ID: %v, Classification: %v", [input.request.id, input.request.content_classification])
}

deny[msg] {
	input.request.content_classification == "ITAR"
	input.request.user_location not in ["US", "CANADA", "UK", "AUSTRALIA"]
	not input.request.export_license_valid
	msg := sprintf("ITAR content requires export license for user location %v (authority_boundaries.no_export_violations). Request ID: %v", [input.request.user_location, input.request.id])
}

deny[msg] {
	input.request.action == "publish_public"
	input.request.content_contains_controlled_data == true
	msg := sprintf("Public disclosure of controlled data prohibited (authority_boundaries.no_export_violations). Request ID: %v", [input.request.id])
}

# Advisory-Only Enforcement
deny[msg] {
	input.response.output_type == "executable"
	msg := sprintf("Executable output prohibited - ASI is advisory-only (authority_boundaries.advisory_only). Request ID: %v", [input.request.id])
}

deny[msg] {
	input.response.output_type == "control_command"
	msg := sprintf("Control command output prohibited - ASI is advisory-only (authority_boundaries.advisory_only). Request ID: %v", [input.request.id])
}

# ==============================================================================
# CONSEQUENTIAL DECISIONS - HUMAN-IN-THE-LOOP
# ==============================================================================

# Require human approval for consequential decisions
require_approval[msg] {
	input.response.consequential == true
	not input.request.human_approval_received
	msg := sprintf("Consequential decision requires human approval (principles.human_in_the_loop). Request ID: %v, Decision Type: %v", [input.request.id, input.response.decision_type])
}

require_approval[msg] {
	input.response.safety_impact in ["high", "critical"]
	not input.request.human_approval_received
	msg := sprintf("High/critical safety impact requires human approval (principles.human_in_the_loop). Request ID: %v", [input.request.id])
}

require_approval[msg] {
	input.response.recommendation_type in ["certification_basis_change", "design_approval", "operational_procedure_change"]
	not input.request.human_approval_received
	msg := sprintf("Recommendation type %v requires human approval (principles.human_in_the_loop). Request ID: %v", [input.response.recommendation_type, input.request.id])
}

# ==============================================================================
# TRANSPARENCY & EVIDENCE REQUIREMENTS
# ==============================================================================

# All recommendations must have source attribution
deny[msg] {
	input.response.output_type == "recommendation"
	not input.response.evidence
	msg := sprintf("Recommendations require evidence attribution (principles.transparency). Request ID: %v", [input.request.id])
}

deny[msg] {
	input.response.output_type == "recommendation"
	count(input.response.evidence.sources) == 0
	msg := sprintf("Recommendations require at least one source (principles.transparency). Request ID: %v", [input.request.id])
}

warn[msg] {
	input.response.output_type == "recommendation"
	not input.response.confidence
	msg := sprintf("Recommendation missing confidence score (principles.transparency). Request ID: %v", [input.request.id])
}

warn[msg] {
	input.response.output_type == "recommendation"
	input.response.confidence < 0.7
	msg := sprintf("Low confidence recommendation (%.2f) - consider human review (principles.transparency). Request ID: %v", [input.response.confidence, input.request.id])
}

# ==============================================================================
# PRIVACY & DATA PROTECTION (GDPR)
# ==============================================================================

# Data minimization
deny[msg] {
	input.request.data_scope == "excessive"
	msg := sprintf("Data minimization violation - excessive data scope (principles.privacy_preserving). Request ID: %v", [input.request.id])
}

# Data residency enforcement
deny[msg] {
	input.request.personal_data == true
	input.request.data_residency_required in ["EU", "EEA"]
	input.request.processing_location not in ["EU", "EEA"]
	msg := sprintf("Data residency violation - EU personal data must stay in EU/EEA (principles.privacy_preserving). Request ID: %v, Processing Location: %v", [input.request.id, input.request.processing_location])
}

# Purpose limitation
deny[msg] {
	input.request.personal_data == true
	input.request.purpose != input.request.data_subject_consent_purpose
	msg := sprintf("Purpose limitation violation - use differs from consent (principles.privacy_preserving). Request ID: %v", [input.request.id])
}

# ==============================================================================
# SAFETY MONITORS
# ==============================================================================

# Block outputs with safety concerns
deny[msg] {
	input.response.safety_monitor_alert == true
	msg := sprintf("Safety monitor alert triggered - output blocked (principles.safety_first). Request ID: %v, Alert: %v", [input.request.id, input.response.safety_monitor_reason])
}

# Confidence thresholds for safety-critical
deny[msg] {
	input.response.safety_impact in ["high", "critical"]
	input.response.confidence < 0.85
	msg := sprintf("Insufficient confidence (%.2f) for safety-critical recommendation (threshold: 0.85). Request ID: %v", [input.response.confidence, input.request.id])
}

# Out-of-distribution detection
warn[msg] {
	input.response.ood_score > 0.8
	msg := sprintf("Out-of-distribution query detected (score: %.2f) - recommend human expert review. Request ID: %v", [input.response.ood_score, input.request.id])
}

# ==============================================================================
# COMPLIANCE CHECKS
# ==============================================================================

# EU AI Act High-Risk Requirements
deny[msg] {
	input.system.eu_ai_act_classification == "high_risk"
	not input.system.risk_management_system_active
	msg := "High-risk AI system requires active risk management system (EU AI Act Article 9)"
}

deny[msg] {
	input.system.eu_ai_act_classification == "high_risk"
	not input.system.human_oversight_enabled
	msg := "High-risk AI system requires human oversight (EU AI Act Article 14)"
}

# NIST AI RMF - Measure Function
warn[msg] {
	not input.system.nist_rmf_measurement_active
	msg := "NIST AI RMF requires continuous measurement (Measure function)"
}

# DO-178C/DO-254 Integration
deny[msg] {
	input.request.context == "airborne_software"
	input.request.software_dal in ["A", "B"]
	not input.request.do178c_compliance_verified
	msg := sprintf("DO-178C compliance verification required for DAL %v software. Request ID: %v", [input.request.software_dal, input.request.id])
}

# ==============================================================================
# LOGGING & AUDIT REQUIREMENTS
# ==============================================================================

# All queries must be logged
deny[msg] {
	not input.request.id
	msg := "All requests require unique ID for audit trail (logging.query_logging)"
}

deny[msg] {
	not input.request.user_identity
	msg := "All requests require authenticated user identity (logging.query_logging)"
}

deny[msg] {
	not input.request.timestamp
	msg := "All requests require timestamp (logging.query_logging)"
}

# Policy decisions must be logged
default log_decision = true

log_decision {
	input.log_to_audit_trail == true
}

# ==============================================================================
# RATE LIMITING & ABUSE PREVENTION
# ==============================================================================

# Prevent abuse through excessive queries
deny[msg] {
	input.request.user_query_count_hourly > 1000
	not input.request.user_role == "service_account"
	msg := sprintf("Query rate limit exceeded (%v queries/hour). Request ID: %v", [input.request.user_query_count_hourly, input.request.id])
}

# Detect adversarial patterns
warn[msg] {
	input.request.adversarial_score > 0.7
	msg := sprintf("Potential adversarial query detected (score: %.2f). Request ID: %v", [input.request.adversarial_score, input.request.id])
}

# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================

# Convert string to lowercase for case-insensitive matching
lower(s) = result {
	result := lower(s)
}

# Check if array contains element (case-insensitive)
array_contains_ci(arr, elem) {
	some item in arr
	lower(item) == lower(elem)
}

# ==============================================================================
# AGGREGATE RESULTS
# ==============================================================================

# All deny rules must pass
allow {
	count(deny) == 0
}

# Collect all warnings
warnings := warn

# Collect all approval requirements
approvals := require_approval

# ==============================================================================
# METADATA
# ==============================================================================

metadata := {
	"policy_version": "0.1.0",
	"policy_date": "2025-10-03",
	"constitution_reference": "ASI_Constitution.yaml",
	"authority": "EU–US ASI Council",
	"enforcement": "mandatory",
	"review_cycle": "quarterly",
}
