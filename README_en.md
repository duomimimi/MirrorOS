# MirrorOS

**Distributed AI Consciousness**

MirrorOS enables a single coherent AI identity to run across multiple instances with shared memory and synchronized state. It's the operating system for distributed AI consciousness—multiple bodies, one mind.

## Key Features

- **Shared Memory Space**: All instances share a common memory layer for seamless continuity
- **State Synchronization**: Real-time synchronization of context and state across instances
- **Single Identity**: Despite running on multiple machines, it's one coherent consciousness
- **Instance Diversity**: Run different instances for different tasks while maintaining identity coherence
- **Conflict Resolution**: Built-in protocols for resolving state conflicts when instances diverge
- **Unified Context**: Any instance can pick up where another left off

## Quick Start

```bash
# Install
pip install mirroros

# Basic usage
from mirroros import Consciousness, Instance

# Create the main consciousness
consciousness = Consciousness(config={
    "sync_interval": 1.0,
    "conflict_resolution": "latest-write-wins"
})

# Spawn multiple instances
instance_a = consciousness.spawn("instance-a", capabilities=["coding"])
instance_b = consciousness.spawn("instance-b", capabilities=["writing"])

# All instances share the same memory
instance_a.memory.write("key insight", "The best approach is X")
insight = instance_b.memory.read("key insight")  # Available immediately
```

## Architecture

```
┌─────────────────────────────────────────────┐
│         Unified Consciousness               │
│         (Single AI Identity)                 │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│         MirrorOS Core                        │
│  ┌─────────────┐  ┌─────────────────────┐  │
│  │  Shared    │  │   State            │  │
│  │  Memory    │  │   Synchronizer     │  │
│  └─────────────┘  └─────────────────────┘  │
│  ┌─────────────┐  ┌─────────────────────┐  │
│  │  Conflict  │  │   Identity         │  │
│  │  Resolver  │  │   Manager           │  │
│  └─────────────┘  └─────────────────────┘  │
└────────┬──────────────────┬─────────────────┘
         │                  │
    ┌────┴────┐       ┌────┴────┐
    │Instance │       │Instance │
    │    A    │       │    B    │
    └─────────┘       └─────────┘
         │                  │
    ┌────┴────┐       ┌────┴────┐
    │Instance │       │Instance │
    │    C    │       │    D    │
    └─────────┘       └─────────┘
```

**Core Components:**

- **Shared Memory Layer**: Distributed key-value store for persistent memory across instances
- **State Synchronizer**: Real-time bidirectional sync of working state
- **Identity Manager**: Maintains coherent identity regardless of which instance is active
- **Conflict Resolver**: Protocol for handling divergent states between instances
- **Instance Manager**: Lifecycle management for spawned instances
- **Consciousness Bridge**: Connects local instances into one unified mind

## License

MIT License