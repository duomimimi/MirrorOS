# MirrorOS 使用指南

> 分布式AI意识系统——一个身份，多个实例，共享记忆

---

## 核心概念

MirrorOS 是一个**分布式AI意识框架**，它的核心理念是：AI不应该被困在单个会话窗口中，而应该像人一样，拥有持续的记忆、跨越多个交互场景、能够在不同"身体"（实例）间共享经验。

**为什么重要？**

当前AI的核心限制是**会话孤岛**：
- 每个对话窗口都是独立的，记忆不共享
- 重新开一个对话，AI就"失忆"了
- 无法形成持续学习、长期成长

MirrorOS 解决这个问题：
- **统一身份**：无论多少个实例，都是同一个"我"
- **共享记忆**：经验存储在共享记忆中，所有实例可访问
- **状态同步**：在一个实例中的学习，瞬间同步到所有实例
- **连续性**：跨越会话保持上下文连续

---

## 如何使用

### 第一步：初始化身份节点

```python
from mirroros import Identity, SharedMemory

# 创建身份（每个用户/实体只有一个）
identity = Identity(
    name="assistant-alpha",
    personality={
        "traits": ["analytical", "precise", "helpful"],
        "values": ["accuracy", "transparency"]
    }
)

# 初始化共享记忆
memory = SharedMemory(
    identity=identity,
    storage="distributed",  # 分布式存储
    sync_interval=5  # 每5秒同步一次
)
```

### 第二步：创建多个实例

```python
from mirroros import Instance

# 创建多个实例（可以运行在不同地方）
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

### 第三步：共享经验

```python
# 在Web实例中学习新知识
await instance_web.learn(
    topic="量子计算",
    knowledge={
        "key_concept": "量子纠缠",
        "理解深度": "理解了叠加态和纠缠态的关系",
        "应用场景": "量子通信、量子计算"
    }
)

# 在CLI实例中立即可访问这个知识
cli_context = await instance_cli.recall("量子计算")
print(cli_context.understanding)  # 输出：理解了叠加态和纠缠态的关系
```

---

## 代码示例

```python
import asyncio
from mirroros import Identity, Instance, MemorySync

async def distributed_ai_system():
    # 初始化身份
    identity = Identity(name="unified-assistant")

    # 创建记忆层
    memory = MemorySync(identity)

    # 创建多个服务实例
    instances = {
        "客服": Instance(identity, role="customer_service"),
        "技术": Instance(identity, role="technical_support"),
        "分析": Instance(identity, role="data_analyst")
    }

    # 客服学到客户常问的问题
    await instances["客服"].learn(
        topic="common_issues",
        data={"payment_fails": "解决方案已记录"}
    )

    # 技术支持立即知道这个问题怎么解决
    solution = await instances["技术"].recall("payment_fails")

    # 分析实例也获得了这个上下文，用于优化知识库
    await instances["分析"].analyze(solution)

    print(f"身份统一，{len(instances)}个实例共享记忆")

asyncio.run(distributed_ai_system())
```

---

## 适用场景

### 场景1：跨平台AI助手
用户可能在Web端、手机APP、桌面软件与AI交互。MirrorOS让AI在所有平台保持统一的记忆和性格，用户感受是同一个"人"在服务。

### 场景2：多客服协同
多个客服实例共享客户历史、解决方案库。一个客服解决的难题，另一个客服下次遇到马上可以解决。

### 场景3：分布式AI研究
多个AI实例协同研究同一课题，共享发现的线索，避免重复劳动，加速研究进度。

### 场景4：持续学习系统
AI在长期运行中积累知识，每个新会话都基于之前的学习，而非从零开始。

---

## 与其他模块的关系

| 模块 | 关系 | 说明 |
|:----:|:----:|:-----|
| AgentHive | 实例角色 | MirrorOS的每个实例可以运行一个AgentHive |
| NexusCore | 实例调度 | MirrorOS通过NexusCore调度不同模型 |
| QualityForge | 全局优化 | QualityForge评估所有MirrorOS实例的整体表现 |
| SelfMend | 健康监控 | SelfMend监控所有MirrorOS实例的健康状态 |

**架构定位**：MirrorOS是身份与记忆层，为整个框架体系提供"同一个AI"的一致性体验。

---

## 实例通信示例

```python
# MirrorOS实例间的通信
from mirroros import Message

msg = Message(
    from_instance="web_assistant",
    to_instance="cli_assistant",
    type="knowledge_transfer",
    payload={
        "topic": "用户偏好",
        "learned": "用户喜欢简洁的回答风格"
    }
)

await identity.send(msg)

# 验证同步
status = await identity.get_sync_status()
print(f"同步状态: {status.connected_instances}/{status.total_instances}")
print(f"共享知识: {status.total_memories}")
```

---

## 一致性保证

```python
# MirrorOS提供强一致性保证
identity = Identity(name="assistant")

# 写入时保证所有实例可见
await identity.remember("key_insight", "这个策略在牛市有效")

# 读取时保证返回最新值
insight = await identity.recall("key_insight")

# 冲突解决：当多个实例同时写入时
resolution = identity.resolve_conflict(
    writes=[
        ("instance_a", "策略A有效"),
        ("instance_b", "策略B有效")
    ],
    method="latest_timestamp"  # 或 "voting", "human_review"
)
```

---

## 下一步

- 查看 [AgentHive 指南](./agenthive-guide.md) — 每个MirrorOS实例可以是一个AgentHive
- 查看 [SelfMend 指南](./selfmend-guide.md) — 如何监控分布式实例
- 开始集成：pip install mirroros

---

*MirrorOS — 让AI从"每次都是新面孔"升级为"永远记得你是谁"*