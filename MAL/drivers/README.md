# MAL Drivers

Low-level hardware and system drivers for ASI-T2 products.

## Purpose

Provides hardware abstraction and device drivers for:
- Sensors and actuators
- Communication interfaces
- Storage devices
- External systems

## Components

### Hardware Abstraction Layer (HAL)
- Unified interface for different hardware platforms
- Platform-specific implementations
- Driver lifecycle management

### Communication Drivers
- CAN bus
- ARINC 429/664
- Ethernet (AFDX)
- Serial (UART, SPI, I2C)
- USB

### Sensor Drivers
- IMU (Inertial Measurement Units)
- GPS/GNSS
- Pressure sensors
- Temperature sensors
- Flow sensors (H₂/LH₂)

### Actuator Drivers
- Flight control surfaces
- Propulsion systems
- Fuel systems
- Landing gear

## Interface

All drivers implement standard MAL driver interface:
```c
struct mal_driver {
    int (*init)(void);
    int (*read)(void *buf, size_t len);
    int (*write)(const void *buf, size_t len);
    int (*ioctl)(int cmd, void *arg);
    void (*cleanup)(void);
};
```

## Status

**H0 (0-90 days)**: Basic driver framework and mock drivers  
**H1 (3-9 months)**: Real hardware drivers for HIL  
**H2 (9-24 months)**: Production-ready drivers
