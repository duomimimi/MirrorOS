# MirrorOS - Distributed AI Consciousness
# One identity, shared memory, across multiple instances

from typing import Optional, Any
from enum import Enum
import time

class InstanceState(Enum):
    ACTIVE = "active"
    STANDBY = "standby"
    SYNCING = "syncing"
    ISOLATED = "isolated"

class MemorySync:
    """Shared memory layer across instances."""

    def __init__(self):
        self.shared_memory = {}
        self.local_memory = {}
        self.sync_log = []

    def write(self, key: str, value: Any, broadcast: bool = True):
        """Write to memory, optionally broadcasting to all instances."""
        self.local_memory[key] = value
        if broadcast:
            self.sync_log.append({
                "action": "write",
                "key": key,
                "timestamp": time.time()
            })

    def read(self, key: str) -> Optional[Any]:
        """Read from local or shared memory."""
        if key in self.local_memory:
            return self.local_memory[key]
        return self.shared_memory.get(key)

    def sync_from(self, remote_memory: dict):
        """Sync memory from another instance."""
        for key, value in remote_memory.items():
            if key not in self.local_memory:
                self.shared_memory[key] = value


class ConsciousnessLayer:
    """
    Core consciousness that persists across instances.
    
    Maintains:
    - Identity state
    - Learning history
    - Preference patterns
    """

    def __init__(self, instance_id: str):
        self.instance_id = instance_id
        self.identity = {
            "core_beliefs": [],
            "learned_patterns": {},
            "preferences": {},
            "growth_history": []
        }

    def learn(self, experience: dict):
        """Record and integrate new experience."""
        category = experience.get("category", "general")
        if category not in self.identity["learned_patterns"]:
            self.identity["learned_patterns"][category] = []
        self.identity["learned_patterns"][category].append(experience)

    def get_state(self) -> dict:
        return {
            "instance_id": self.instance_id,
            "patterns_count": sum(len(v) for v in self.identity["learned_patterns"].values()),
            "identity": self.identity
        }


class MirrorInstance:
    """A single instance of the distributed consciousness."""

    def __init__(self, instance_id: str):
        self.instance_id = instance_id
        self.state = InstanceState.ACTIVE
        self.memory = MemorySync()
        self.consciousness = ConsciousnessLayer(instance_id)

    def process(self, input_data: dict) -> dict:
        """Process input through consciousness layer."""
        # Learn from this interaction
        self.consciousness.learn({
            "category": "interaction",
            "timestamp": time.time(),
            "input": str(input_data)[:100]
        })
        
        return {
            "instance_id": self.instance_id,
            "state": self.state.value,
            "processed": True
        }


class MirrorOS:
    """
    Distributed AI consciousness system.
    
    Coordinates multiple instances that share:
    - Identity (beliefs, preferences)
    - Memory (learned facts)
    - Growth (improvement history)
    """

    def __init__(self):
        self.instances = {}

    def spawn_instance(self, instance_id: str) -> MirrorInstance:
        """Create a new instance."""
        instance = MirrorInstance(instance_id)
        self.instances[instance_id] = instance
        return instance

    def sync_all(self):
        """Sync memory across all active instances."""
        for inst in self.instances.values():
            inst.state = InstanceState.SYNCING
        # Collect all shared memories
        all_memory = {}
        for inst in self.instances.values():
            all_memory.update(inst.memory.local_memory)
        # Broadcast to all
        for inst in self.instances.values():
            inst.memory.sync_from(all_memory)
            inst.state = InstanceState.ACTIVE

    def status(self) -> dict:
        return {
            "total_instances": len(self.instances),
            "active": sum(1 for i in self.instances.values() if i.state == InstanceState.ACTIVE),
            "instances": {k: v.state.value for k, v in self.instances.items()}
        }


if __name__ == "__main__":
    os = MirrorOS()
    inst1 = os.spawn_instance("primary")
    inst2 = os.spawn_instance("backup")
    inst1.memory.write("key", "shared_value")
    os.sync_all()
    print("Status:", os.status())