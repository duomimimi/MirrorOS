# MirrorOS User Guide

> Distributed AI Consciousness System — One Identity, Multiple Instances, Shared Memory

---

## Core Concept

MirrorOS is a **distributed AI consciousness framework** whose core philosophy is: AI should not be trapped in a single conversation window. Instead, like humans, it should have persistent memory, span multiple interaction scenarios, and be able to share experiences across different "bodies" (instances).

**Why does it matter?**

The core limitation of current AI is **conversation isolation**:
- Each conversation window is independent; memories don't share
- Opening a new conversation, and the AI "forgets" everything
- Cannot form continuous learning or long-term growth

MirrorOS solves this:
- **Unified Identity**: However many instances, it's still the same "me"
- **Shared Memory**: Experience is stored in shared memory, accessible by all instances
- **State Sync**: Learning in one instance instantly syncs to all instances
- **Continuity**: Maintains context continuity across conversations

---

## How to Use

### Step 1: Initialize Identity Node

```python
from mirroros import Identity, SharedMemory

# Create identity (one per user/entity)
identity = Identity(
    name="assistant-alpha",
    personality={
        "traits": ["analytical", "precise", "helpful"],
        "values": ["accuracy", "transparency"]
    }
)

# Initialize shared memory
memory = SharedMemory(
    identity=identity,
    storage="distributed",  # Distributed storage
    sync_interval=5  # Sync every 5 seconds
)
```

### Step 2: Create Multiple Instances

```python
from mirroros import Instance

# Create multiple instances (can run in different places)
instance_web = Instance(
    identity=identity,
    role="web_assistant",
    capabilities=["browsing", "search"]
)

instance_cli = Instance(
    identity=identity,
    role="cli_assistant",
    capabilities=["coding", "file_ops"]
)

instance_mobile = Instance(
    identity=identity,
    role="mobile_assistant",
    capabilities=["reminders", "communication"]
)
```

### Step 3: Share Experiences

```python
# Learn new knowledge in the Web instance
await instance_web.learn(
    topic="quantum computing",
    knowledge={
        "key_concept": "quantum entanglement",
        "depth_of_understanding": "understood the relationship between superposition and entanglement",
        "application_scenarios": "quantum communication, quantum computing"
    }
)

# Immediately accessible in the CLI instance
cli_context = await instance_cli.recall("quantum computing")
print(cli_context.understanding)  # Output: understood the relationship between superposition and entanglement
```

---

## Code Example

```python
import asyncio
from mirroros import Identity, Instance, MemorySync

async def distributed_ai_system():
    # Initialize identity
    identity = Identity(name="unified-assistant")

    # Create memory layer
    memory = MemorySync(identity)

    # Create multiple service instances
    instances = {
        "customer_service": Instance(identity, role="customer_service"),
        "technical": Instance(identity, role="technical_support"),
        "analysis": Instance(identity, role="data_analyst")
    }

    # Customer service learns common customer questions
    await instances["customer_service"].learn(
        topic="common_issues",
        data={"payment_fails": "solution already recorded"}
    )

    # Technical support immediately knows how to solve this problem
    solution = await instances["technical"].recall("payment_fails")

    # Analysis instance also gains this context for knowledge base optimization
    await instances["analysis"].analyze(solution)

    print(f"Unified identity, {len(instances)} instances sharing memory")

asyncio.run(distributed_ai_system())
```

---

## Use Cases

### Case 1: Cross-Platform AI Assistant
Users might interact with AI on web, mobile app, and desktop software. MirrorOS keeps AI's memory and personality consistent across all platforms — users feel they're interacting with the same "person."

### Case 2: Multi-Customer-Service Collaboration
Multiple customer service instances share customer history and solution repositories. When one customer service agent solves a difficult problem, another agent can immediately solve it the next time.

### Case 3: Distributed AI Research
Multiple AI instances collaboratively research the same topic, sharing discovered clues, avoiding duplicated effort, accelerating research progress.

### Case 4: Continuous Learning System
AI accumulates knowledge during long-term operation. Each new conversation builds on previous learning — not starting from scratch.

---

## Relationship with Other Modules

| Module | Relationship | Description |
|:----:|:----:|:-----|
| AgentHive | Instance Roles | Each MirrorOS instance can run an AgentHive |
| NexusCore | Instance Scheduling | MirrorOS schedules different models via NexusCore |
| QualityForge | Global Optimization | QualityForge evaluates overall performance of all MirrorOS instances |
| SelfMend | Health Monitoring | SelfMend monitors health of all MirrorOS instances |

**Architecture Position**: MirrorOS is the identity and memory layer, providing the entire framework with the consistent experience of "the same AI."

---

## Instance Communication Example

```python
# Communication between MirrorOS instances
from mirroros import Message

msg = Message(
    from_instance="web_assistant",
    to_instance="cli_assistant",
    type="knowledge_transfer",
    payload={
        "topic": "user preferences",
        "learned": "user prefers concise response style"
    }
)

await identity.send(msg)

# Verify synchronization
status = await identity.get_sync_status()
print(f"Sync Status: {status.connected_instances}/{status.total_instances}")
print(f"Shared Knowledge: {status.total_memories}")
```

---

## Consistency Guarantees

```python
# MirrorOS provides strong consistency guarantees
identity = Identity(name="assistant")

# On write, guarantee all instances can see it
await identity.remember("key_insight", "this strategy works in bull markets")

# On read, guarantee returns latest value
insight = await identity.recall("key_insight")

# Conflict resolution: when multiple instances write simultaneously
resolution = identity.resolve_conflict(
    writes=[
        ("instance_a", "Strategy A works"),
        ("instance_b", "Strategy B works")
    ],
    method="latest_timestamp"  # or "voting", "human_review"
)
```

---

## Next Steps

- See the [AgentHive Guide](./agenthive-guide_en.md) — Each MirrorOS instance can be an AgentHive
- See the [SelfMend Guide](./selfmend-guide_en.md) — How to monitor distributed instances
- Get started: `pip install mirroros`

---

*MirrorOS — Upgrade AI from "every time is a new face" to "always remembers who you are"*