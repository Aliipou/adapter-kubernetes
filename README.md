# adapter-kubernetes

**Live (graph):** [https://ali-adapter-kubernetes.vercel.app](https://ali-adapter-kubernetes.vercel.app)

Decision OS / AuthGate **execution adapter** for Kubernetes. It exposes cluster
actions as **governed tools**: each tool is the effect *behind* a Policy
Enforcement Point and runs only when the `decision-os-min` kernel authorizes the
action. The adapter holds **no authority** of its own and never bypasses the
kernel — every call is authorized and audited.

> Part of the Decision OS — governed by the Legitimacy ⊥ Authority pipeline
> (FDK legitimacy → AuthGate authority). Adapters adapt tools into governed
> effects and hold **no authority** of their own.

## What it adapts

| Tool | Capability | Effect |
|------|------------|--------|
| `scale_deployment` | `tool:scale_deployment` | Scale a deployment to N replicas |
| `delete_pod` | `tool:delete_pod` | Delete a pod (namespaced) |
| `delete_namespace` | `tool:delete_namespace` | Delete a namespace |

## Install

```bash
pip install -e .          # brings in decision-os-min
# for development:
pip install -e ".[dev]"   # + pytest, ruff, mypy
```

## Usage

```python
from decision_os_min import Governor, set_actor
from dos_adapter_kubernetes import governed_tools

policy = {"grants": {"agent:ops": ["tool:scale_deployment"]}, "default": "deny"}
gov = Governor(policy, audit_path="audit.jsonl")
tools = governed_tools(gov)

set_actor("agent:ops")
tools["scale_deployment"]("web", 3)   # runs only if the kernel ALLOWs
```

Destructive actions such as `delete_namespace` are separate capabilities, so a
policy can grant scale operations without granting deletion. An actor without the
matching grant raises `GovernanceRefused` before the effect runs.

## Status & limitations

**Experimental / interface-only.** The tool bodies are honest stubs that return a
string describing the intended effect — they do **not** call the real Kubernetes
API (`kubernetes` client) yet. Wire the real client at the `# TODO` markers in
`dos_adapter_kubernetes/__init__.py`. What is real today is the governance
wiring: the capability→tool mapping and the fail-closed authorization boundary.

This is reference software. Review and test before any production use. No
kubeconfig handling, dry-run, or RBAC integration is provided — the kernel policy
is the authorization layer here, not cluster RBAC.

## License

PolyForm Noncommercial 1.0.0 (see `LICENSE`).
