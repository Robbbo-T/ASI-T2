# ARINC 429 Implementation Guide

**Document ID:** REF-A429-IMPL-002  
**Version:** 1.0  
**Date:** 2025-09-30  
**Classification:** INTERNAL–REFERENCE

## Purpose

This guide provides practical guidance for implementing ARINC 429 communication in avionics systems, focusing on best practices, common pitfalls, and design patterns learned from operational experience.

## Design Philosophy

### Keep It Simple
ARINC 429's strength is its simplicity. Don't over-complicate:
- Use standard labels when available
- Follow established conventions
- Leverage existing libraries and components

### Design for Reliability
Critical systems require robust implementation:
- Implement all error detection mechanisms
- Use redundant channels for critical data
- Design for graceful degradation

### Plan for Maintainability
Code will be maintained for decades:
- Document all custom labels
- Use clear naming conventions
- Provide comprehensive test coverage

## Hardware Selection

### Interface Cards

#### Considerations
- **Channel Count**: Plan for growth (buy more channels than needed)
- **Speed Support**: Ensure both 12.5 and 100 kbps supported
- **Isolation**: Optical isolation recommended (≥1500V)
- **Driver Support**: Evaluate software ecosystem

#### Recommended Features
- Hardware label filtering (reduces CPU load)
- DMA support (improves efficiency)
- Error counters (aid troubleshooting)
- Timestamp support (simplifies debugging)

### Cabling

#### Best Practices
- Use certified TSP cable (75Ω)
- Keep runs as short as practical
- Route away from power cables
- Ground shield at receiver only
- Label cables clearly

#### Common Mistakes to Avoid
- ❌ Grounding shield at both ends (creates ground loops)
- ❌ Mixing low and high-speed buses in same cable bundle
- ❌ Exceeding maximum cable length (100m)
- ❌ Sharp bends (damages cable)

## Software Architecture

### Layered Design

```
┌─────────────────────────────────┐
│   Application Layer             │  ← Label-specific processing
├─────────────────────────────────┤
│   Protocol Layer                │  ← Encoding/decoding, error handling
├─────────────────────────────────┤
│   Driver Layer                  │  ← Hardware interface
└─────────────────────────────────┘
```

### Driver Layer

#### Responsibilities
- Hardware initialization
- Interrupt handling
- DMA management
- Raw word transmission/reception

#### Design Pattern: Abstraction
```c
// Abstract interface
typedef struct {
    void (*init)(a429_config_t* config);
    int (*transmit)(uint32_t word);
    int (*receive)(uint32_t* word, uint32_t timeout);
    void (*get_stats)(a429_stats_t* stats);
} a429_driver_t;
```

### Protocol Layer

#### Responsibilities
- Label encoding/decoding
- Parity calculation/verification
- SSM handling
- Error detection

#### Design Pattern: Label Handlers
```c
typedef struct {
    uint8_t label;
    void (*encode)(const void* data, a429_word_t* word);
    void (*decode)(const a429_word_t* word, void* data);
} label_handler_t;
```

### Application Layer

#### Responsibilities
- Business logic
- Data validation
- Redundancy management
- Fault handling

## Label Management

### Label Dictionary

Maintain a central label dictionary:
```yaml
labels:
  - label: 010
    name: "Airspeed"
    data_type: "BNR"
    units: "knots"
    resolution: 0.125
    range: [0, 1023.875]
    source: "Air Data Computer"
    destinations: ["FBW", "Display"]
    update_rate: 10  # Hz
```

### Custom Labels

When defining custom labels:
1. Document thoroughly
2. Coordinate with other subsystems
3. Reserve ranges for related parameters
4. Consider future expansion

#### Recommended Ranges
- **System-specific**: 350-377₈
- **Test/debug**: 000₈
- **Reserved**: Avoid 100-117₈ (position data)

## Data Encoding

### BNR (Binary) Encoding

#### Best Practices
```c
// Good: Clear, maintainable
int32_t encode_airspeed(float kts) {
    const float RESOLUTION = 0.125;
    const float MIN_VALUE = 0.0;
    int32_t encoded = (int32_t)((kts - MIN_VALUE) / RESOLUTION);
    // Clamp to valid range
    if (encoded < 0) encoded = 0;
    if (encoded > 0x7FFFF) encoded = 0x7FFFF;
    return encoded;
}
```

#### Common Mistakes
```c
// Bad: Magic numbers, no range checking
int32_t encode_airspeed(float kts) {
    return (int32_t)(kts * 8);  // What is 8? What's the range?
}
```

### BCD Encoding

#### Best Practices
```c
// Encode heading 0-359.9 degrees
uint32_t encode_heading_bcd(float degrees) {
    // Convert to tenths
    uint32_t tenths = (uint32_t)(degrees * 10);
    
    // Convert to BCD
    uint32_t bcd = 0;
    for (int i = 0; i < 4; i++) {
        bcd |= ((tenths % 10) << (i * 4));
        tenths /= 10;
    }
    return bcd;
}
```

### Discrete Encoding

#### Best Practices
```c
// Use named bits
#define AUTOPILOT_ENGAGED  (1 << 0)
#define AUTOTHROTTLE_ON    (1 << 1)
#define VNAV_ACTIVE        (1 << 2)
#define LNAV_ACTIVE        (1 << 3)

uint32_t encode_autopilot_status(bool ap, bool at, bool vnav, bool lnav) {
    uint32_t status = 0;
    if (ap)   status |= AUTOPILOT_ENGAGED;
    if (at)   status |= AUTOTHROTTLE_ON;
    if (vnav) status |= VNAV_ACTIVE;
    if (lnav) status |= LNAV_ACTIVE;
    return status;
}
```

## Error Handling

### Detection Strategy

Implement multiple layers:
1. **Hardware**: Parity, sync pattern
2. **Protocol**: SSM checking, range validation
3. **Application**: Staleness detection, cross-channel comparison

### Handling Strategy

#### Parity Errors
```c
if (!verify_parity(word)) {
    log_error("Parity error on label %03o", get_label(word));
    increment_counter(&stats.parity_errors);
    return ERROR_PARITY;  // Discard word
}
```

#### Staleness Detection
```c
uint32_t now = get_time_ms();
if (now - label_data[label].timestamp > STALE_TIMEOUT) {
    label_data[label].flags |= FLAG_STALE;
    log_warning("Label %03o stale", label);
}
```

#### Redundancy Comparison
```c
if (fabs(channel_a_value - channel_b_value) > TOLERANCE) {
    log_warning("Channel disagreement: %f vs %f", 
                channel_a_value, channel_b_value);
    // Use best quality source
    return select_best_quality(channel_a, channel_b);
}
```

## Performance Optimization

### CPU Efficiency

#### Hardware Label Filtering
```c
// Configure hardware to filter only needed labels
a429_filter_config_t filter = {
    .labels = {010, 020, 030, 203, 204},
    .count = 5,
    .mode = FILTER_ACCEPT_LIST
};
a429_set_filter(&filter);
```

#### DMA for Data Transfer
```c
// Setup DMA for bulk reception
a429_dma_config_t dma = {
    .buffer = rx_buffer,
    .size = RX_BUFFER_SIZE,
    .callback = rx_dma_complete
};
a429_setup_dma(&dma);
```

#### Batch Processing
```c
// Process multiple words per interrupt
void a429_interrupt_handler(void) {
    uint32_t word;
    while (a429_word_available()) {
        word = a429_read_word();
        queue_for_processing(word);
    }
}
```

### Memory Efficiency

#### Fixed Allocation
```c
// Good: Static allocation (required for DO-178C)
static a429_word_t rx_buffer[RX_BUFFER_SIZE];
static label_data_t label_cache[256];
```

#### Circular Buffers
```c
typedef struct {
    a429_word_t buffer[BUFFER_SIZE];
    uint32_t head;
    uint32_t tail;
} a429_circular_buffer_t;
```

## Testing

### Unit Testing

Test each encoding/decoding function:
```c
void test_encode_airspeed(void) {
    assert(encode_airspeed(0.0) == 0);
    assert(encode_airspeed(100.0) == 800);
    assert(encode_airspeed(1023.875) == 0x7FFFF);
}
```

### Integration Testing

Test with real hardware:
```c
void test_label_roundtrip(void) {
    float original = 123.456;
    a429_word_t word;
    float decoded;
    
    encode_label_010(original, &word);
    a429_transmit(word);
    a429_receive(&word);
    decode_label_010(&word, &decoded);
    
    assert(fabs(original - decoded) < TOLERANCE);
}
```

### Error Injection

Test error handling:
```c
void test_parity_error_handling(void) {
    a429_word_t word = create_valid_word();
    word.parity = !word.parity;  // Corrupt parity
    
    int result = process_word(&word);
    assert(result == ERROR_PARITY);
    assert(error_counter_incremented());
}
```

## Debugging

### Common Issues and Solutions

#### No Data Received
- ✅ Check cable connections
- ✅ Verify transmitter is sending
- ✅ Confirm correct baud rate
- ✅ Check hardware initialization

#### Parity Errors
- ✅ Check for EMI/noise sources
- ✅ Verify cable quality
- ✅ Check termination resistor
- ✅ Reduce cable length if possible

#### Stale Data
- ✅ Verify transmitter update rate
- ✅ Check for intermittent connections
- ✅ Verify scheduling allows timely processing

#### Channel Disagreement
- ✅ Check sensor calibration
- ✅ Verify both channels receiving same source
- ✅ Check for timing skew

### Debug Tools

#### Protocol Analyzer
Essential for:
- Verifying bit timing
- Checking word format
- Monitoring bus traffic
- Long-term logging

#### Oscilloscope
Useful for:
- Signal integrity
- Voltage levels
- Rise/fall times
- EMI investigation

#### Logic Analyzer
Good for:
- Bit-level decode
- Timing analysis
- Multi-channel correlation

## Certification Considerations

### DO-178C Compliance

Key requirements:
- Requirements traceability
- 100% MC/DC coverage for DAL-A
- Code review and static analysis
- Configuration management

### Documentation

Required documents:
- Software Requirements Specification
- Software Design Description
- Software Verification Plan/Report
- Software Configuration Management Plan

### Testing Evidence

Maintain:
- Test procedures
- Test results
- Coverage reports
- Traceability matrices

## Migration Path

### From Legacy System

1. **Analysis Phase**
   - Document existing labels
   - Identify differences
   - Plan transition strategy

2. **Implementation Phase**
   - Implement new labels incrementally
   - Maintain backward compatibility
   - Parallel operation period

3. **Verification Phase**
   - Cross-check with legacy system
   - Extended operational testing
   - Gradual transition

## References

- [ARINC 429 Specification](./ARINC429_spec.md)
- [Architecture Specification](../descriptive/architecture_spec.md)
- [Implementation Guide](../descriptive/implementation_guide.md)
- [Label Definitions](../configuration/label_definitions.yaml)

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-09-30 | IIS Team | Initial implementation guide |
