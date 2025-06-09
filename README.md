# FDSL - Feature Definition DSL

**FDSL** is a domain-specific language for defining machine learning features in a clean, reusable, and consistent way. It enables teams to declare features once and automatically generate production-ready code across multiple environments, including Python (Pandas), SQL, monitoring configs, and real-time API schemas.

---

## 🚀 Key Features

- **Human-readable syntax** for feature definitions
- **Automatic code generation** for:
  - Python (Pandas)
  - SQL
  - YAML (Monitoring configs)
  - JSON (API schemas)
- **Single source of truth** for feature logic
- Promotes **collaboration, auditability, and consistency**

---

## 📘 Example

### DSL Input

```dsl
feature: is_active = days_since_last_login < 30
feature: low_spender = total_spent < 100
feature: no_recent_support = support_tickets_last_90d == 0
