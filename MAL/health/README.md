# MAL Health Monitoring

Health monitoring and watchdog system for all ASI-T2 components.

## Purpose

Provides continuous health monitoring for:
- Services and components
- Hardware systems
- Network connectivity
- Resource utilization
- Mission status

## Health Checks

### Component Health
- Service heartbeat
- API endpoint availability
- Response time monitoring
- Error rate tracking

### System Health
- CPU, memory, disk usage
- Temperature monitoring
- Power status
- Network connectivity

### Mission Health
- Mission objectives status
- SLO (Service Level Objective) compliance
- Safety constraints validation
- MAL-EEM rule compliance

## Health Status Levels

```
✅ HEALTHY    - All checks passing
⚠️  DEGRADED  - Some non-critical issues
❌ UNHEALTHY  - Critical issues detected
🔴 FAILED     - System failure, safety response triggered
```

## Watchdog System

### Watchdog Types

**Software Watchdog**:
- Process monitoring
- Thread deadlock detection
- Memory leak detection
- Response timeout monitoring

**Hardware Watchdog**:
- External watchdog timer
- Automatic reset on failure
- Safe state enforcement

### Watchdog Actions

1. **Alert**: Notification to operators
2. **Restart**: Automatic service restart
3. **Failover**: Switch to backup system
4. **Safe State**: Engage safe mode (MAL-EEM)
5. **Emergency Stop**: Complete system shutdown

## Monitoring Dashboard

Real-time dashboard showing:
- Overall system health
- Component status grid
- Recent alerts and events
- Resource utilization
- Mission progress

## Alerting

Alert channels:
- Console logs
- Email notifications
- SMS/phone for critical
- Dashboard notifications
- Message bus (MAL.v1.health)

## Implementation Roadmap

**H0**: Basic health checks and logging  
**H1**: Automated recovery and failover  
**H2**: Predictive health monitoring and ML-based anomaly detection
