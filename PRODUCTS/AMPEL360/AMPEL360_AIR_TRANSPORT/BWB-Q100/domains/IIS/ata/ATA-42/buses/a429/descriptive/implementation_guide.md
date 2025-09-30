# ARINC 429 Implementation Guide

**Document ID:** DESC-A429-IMP-003  
**Version:** 1.0  
**Date:** 2025-09-30  
**Classification:** INTERNAL–EVIDENCE-REQUIRED

## Purpose
This guide provides implementation details for integrating ARINC 429 communication into the BWB-Q100 IMA system.

## Hardware Implementation

### Interface Cards
- **Model:** ARINC 429 Multi-Channel Interface Card
- **Channels per Card:** 4 RX + 4 TX
- **Cards per System:** 2 (for redundancy)

### Wiring Requirements
- **Cable Type:** Twisted shielded pair (TSP)
- **Shield:** Connected to chassis ground at receiver only
- **Routing:** Separate from power cables
- **Minimum Bend Radius:** 10× cable diameter

### Connector Standards
- **Type:** D-subminiature or MIL-DTL-38999
- **Pin Assignment:** Per ARINC 429 specification
- **Contact Retention:** >10 N

## Software Implementation

### Driver Architecture

#### Initialization
```c
// Pseudo-code
a429_init_config_t config = {
    .channel = A429_RX1,
    .speed = A429_SPEED_100K,
    .parity = A429_PARITY_ODD,
    .label_filter = ENABLED,
    .labels = {0x203, 0x204, ...}
};

status = a429_init(&config);
```

#### Receive Processing
```c
// Pseudo-code
a429_word_t word;
status = a429_receive(A429_RX1, &word, TIMEOUT_MS);

if (status == A429_OK) {
    if (a429_check_parity(word)) {
        process_label(word.label, word.data, word.ssm);
    }
}
```

#### Transmit Processing
```c
// Pseudo-code
a429_word_t word = {
    .label = 0x312,  // CAS label
    .sdi = 0x00,
    .data = encode_bnr(airspeed_kts),
    .ssm = SSM_NORMAL_OP
};

a429_compute_parity(&word);
status = a429_transmit(A429_TX2, &word);
```

### ARINC 653 Integration

#### Port Configuration
```xml
<!-- Sampling port for periodic reception -->
<Sampling_Port Name="A429_AoA_In" 
               MaxMessageSize="4" 
               Direction="SOURCE" 
               RefreshRateSeconds="0.01"/>

<!-- Queuing port for event-driven transmission -->
<Queuing_Port Name="A429_Cmd_Out" 
              MaxMessageSize="4" 
              MaxNbMessages="10" 
              Direction="DESTINATION"/>
```

#### Partition Code
```c
// In partition source code
SAMPLING_PORT_ID_TYPE port_id;
MESSAGE_SIZE_TYPE len = sizeof(a429_word_t);
RETURN_CODE_TYPE ret;

// Read from sampling port
READ_SAMPLING_MESSAGE(port_id, &a429_word, &len, &validity, &ret);

// Process if valid
if (ret == NO_ERROR && validity == VALID) {
    process_a429_data(&a429_word);
}
```

## Label Implementation

### Standard Labels
Implement labels according to ARINC 429 specification:
- **001:** Heading
- **010:** Airspeed
- **020:** Altitude
- **030:** Vertical Speed

### Custom Labels
For application-specific data:
- Document in label dictionary
- Coordinate with system integrators
- Reserve ranges for future expansion

### Data Encoding

#### BNR (Binary) Format
```c
// Convert physical value to BNR
int32_t encode_bnr(float value, float resolution, float range_min) {
    int32_t encoded = (int32_t)((value - range_min) / resolution);
    return encoded & 0x7FFFF;  // 19-bit field
}

// Convert BNR to physical value
float decode_bnr(int32_t encoded, float resolution, float range_min) {
    return (encoded * resolution) + range_min;
}
```

#### BCD Format
```c
// Convert integer to BCD
uint32_t encode_bcd(uint32_t value) {
    uint32_t bcd = 0;
    for (int i = 0; i < 5; i++) {
        bcd |= ((value % 10) << (i * 4));
        value /= 10;
    }
    return bcd;
}
```

## Error Handling

### Parity Errors
- Discard word
- Log error with timestamp
- Increment error counter
- Trigger fault if rate exceeds threshold

### Timeout Detection
- Monitor for expected labels
- Timeout = 3× expected period
- Set data stale flag
- Notify fault manager

### Data Validation
- Check SSM for validity
- Range check values
- Cross-check with redundant channels

## Testing

### Unit Tests
- Label encoding/decoding
- Parity calculation
- Data format conversions
- Error detection

### Integration Tests
- Channel configuration
- Label filtering
- Multi-channel coordination
- Partition integration

### Hardware-in-Loop Tests
- Signal integrity
- Timing verification
- Error injection
- Long-duration reliability

## Configuration Management

### Version Control
- All configuration files in Git
- Label definitions versioned
- Change review required

### Traceability
- Labels to requirements
- Configuration to design
- Tests to specifications

## Safety Considerations

### Critical Data
- Redundant transmission
- Cross-channel comparison
- Voting algorithms
- Fault detection within 100 ms

### Partitioning
- Spatial isolation (different channels)
- Temporal isolation (ARINC 653)
- Fault containment

## Performance Optimization

### CPU Usage
- DMA for data transfer
- Interrupt-driven reception
- Label filtering in hardware
- Batch processing where possible

### Memory Usage
- Circular buffers for reception
- Shared memory for inter-partition
- Static allocation (no dynamic allocation)

## Documentation Requirements

### Configuration Data
- Label dictionary
- Channel assignments
- Update rates
- Timing requirements

### Interface Control Documents
- Partner system interfaces
- Data format specifications
- Timing diagrams
- Error handling procedures

## References

- ARINC Specification 429 Mark 33
- DO-178C Software Considerations
- ARINC Specification 653 Part 1
- [Architecture Specification](./architecture_spec.md)
- [Label Definitions](../configuration/label_definitions.yaml)
