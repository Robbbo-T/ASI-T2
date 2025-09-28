# AOA Core System

Core components of the PRODUCTS/INFRANET/AOA App-of-Apps system.

## Components

### app.py
Main FastAPI application providing the AOA REST API with endpoints for:
- Capability registry management
- Composition orchestration and dry-run planning
- Policy validation engine
- Evidence envelope generation with UTCS/QS anchors
- In-memory storage for MVP phase

### registry.py
Placeholder for future persistent registry implementation (SQL/DocStore).
Currently uses in-memory storage in app.py.

### planner.py
Placeholder for advanced DAG planning logic.
Basic topological sorting is implemented in app.py.

### policy.py
Placeholder for OPA (Rego) integration via REST or WASM.
Simple policy checks are implemented in app.py for ethics and data residency.

### evidence.py
Placeholder for real UTCS/QS anchor integration with KMS signing.
Basic evidence envelope generation is implemented in app.py.

### scheduler.py
Placeholder for execution adapters (k8s/ROS2/RTOS) to be added at Day 60.

## Running the Server

```bash
# From repository root
uvicorn INFRANET.AOA.core.app:app --reload --host 127.0.0.1 --port 8000
```

## API Endpoints

- `GET /api/v1/registry/capabilities` - List capabilities
- `POST /api/v1/registry/capabilities` - Publish capability
- `POST /api/v1/registry/compositions` - Publish composition
- `POST /api/v1/policy/admit` - Policy validation
- `POST /api/v1/compose/dry-run` - Composition planning