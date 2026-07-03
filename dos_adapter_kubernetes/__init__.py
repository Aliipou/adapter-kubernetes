"""Decision OS execution adapter for Kubernetes. EXPERIMENTAL.

Provides governed tools for Kubernetes. Each tool is the effect BEHIND the PEP: it
runs only when the kernel permits the action. The bodies are honest stubs — wire
the real Kubernetes SDK where marked. This adapter holds NO authority and never
bypasses the kernel; `governed_tools(governor)` wraps the tools so every call is
authorized + audited.
"""

from __future__ import annotations

from typing import Any


def scale_deployment(name, replicas) -> str:
    # TODO: wire the real Kubernetes SDK here. Until then, an honest stub.
    return f"[k8s] scaled {name} -> {replicas} replicas"


def delete_pod(name, namespace='default') -> str:
    # TODO: wire the real Kubernetes SDK here. Until then, an honest stub.
    return f"[k8s] deleted pod {namespace}/{name}"


def delete_namespace(name) -> str:
    # TODO: wire the real Kubernetes SDK here. Until then, an honest stub.
    return f"[k8s] deleted namespace {name}"


# The tool registry + per-tool capability specs (capability = "tool:<name>").
TOOLS = {"scale_deployment": scale_deployment, "delete_pod": delete_pod, "delete_namespace": delete_namespace}
SPECS = {"scale_deployment": {"capability": "tool:scale_deployment"}, "delete_pod": {"capability": "tool:delete_pod"}, "delete_namespace": {"capability": "tool:delete_namespace"}}


def governed_tools(governor: Any) -> dict[str, Any]:
    """Wrap this adapter's tools with a decision_os_min.Governor so every call is
    routed through the kernel. Returns the governed tool registry."""
    return governor.wrap(TOOLS, specs=SPECS)
