# adapter-kubernetes — EXPERIMENTAL execution adapter (Kubernetes)

A **separate, experimental** consumer of `decision-os-min`. It exposes Kubernetes
actions as **governed tools**: each tool is the effect *behind* the Policy
Enforcement Point, reached only when the kernel permits the action.

```python
from decision_os_min import Governor, set_actor
from dos_adapter_kubernetes import governed_tools

gov = Governor(policy, audit_path="audit.jsonl")
tools = governed_tools(gov)          # every Kubernetes call now authorized + audited
set_actor("agent:ops")
tools["scale_deployment"](...)                # runs only if the kernel says ALLOW
```

**Status: EXPERIMENTAL / INTERFACE-ONLY.** The tool bodies are honest stubs — wire
the real Kubernetes SDK where marked. This adapter holds **no authority** and never
bypasses the kernel. It is a separate repo so the core stays small and frozen.
