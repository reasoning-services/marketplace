# Context Switcher: Perspective Combinations by Domain

Reference for selecting perspectives that produce productive tension.

## Core Selection Principle

A set of perspectives is well-chosen when:
- At least two perspectives are likely to disagree on the key question
- Each perspective has genuine stake in the outcome
- No two perspectives are so similar they produce the same analysis
- The most likely critic or skeptic is represented

Perspectives produce theater when they're chosen for coverage rather than tension.

---

## Combinations by Decision Domain

### Product Decisions

**Standard (4 perspectives):**
- User Experience — what does the person using this need, and what will they actually do vs. what they're supposed to do?
- Engineering — what is buildable within real constraints, and what are the hidden technical costs?
- Business — what creates sustainable value, and what are the revenue and cost implications?
- Operations — what can be supported, monitored, and maintained long-term?

**Deep (add 2 more):**
- Security — what attack surface does this create, and who might misuse it?
- Compliance — are there regulatory or legal constraints that bound the options?

**Why these work:** Each perspective has genuine stake and genuine blind spots. UX wants ease; Engineering wants correctness; Business wants return; Ops wants stability. The tensions between them are structural, not forced.

---

### Technical Architecture Decisions

**Standard (4 perspectives):**
- Application Developer — using the system daily; cares about API ergonomics, local development, and deployment friction
- Infrastructure / Platform — running and scaling the system; cares about observability, cost, and failure isolation
- Security — threat surface and access control; cares about least-privilege, blast radius, and auditability
- Future Maintainer — inheriting this in 18 months; cares about documentation, dependency health, and changeability

**Deep (add 1):**
- Performance at Scale — what degrades first under 10x load? What is the worst-case failure mode?

**Why these work:** Developers and infrastructure teams conflict on coupling and abstraction layers. Security and velocity are in tension on almost every design decision. Future Maintainer is systematically underweighted — include them explicitly.

---

### API or Interface Design

**Standard (4 perspectives):**
- Primary consumer — the team or system using this interface first; cares about expressiveness and convenience
- Secondary consumer — the next team or system to integrate; cares about discoverability and stability
- API author — the team maintaining the contract long-term; cares about simplicity, stability, and avoiding breaking changes
- External integrator — if third-party integrations are possible; cares about documentation quality and error clarity

**Why these work:** Consumer and author interests conflict structurally. Consumers want maximum expressiveness; authors want minimal surface area. This tension is the core of every API design decision.

---

### Organizational or Process Change

**Standard (4 perspectives):**
- Individual contributor — daily workflow impact; cares about friction, clarity, and whether the change actually helps
- Team lead / manager — coordination overhead and team dynamics; cares about adoption pace and edge cases
- Adjacent team — cross-team dependencies and interfaces; cares about what changes in how they interact with this team
- Executive sponsor — strategic alignment and visibility; cares about outcomes, not process

**Deep (add 2):**
- Skeptic — the person most likely to resist this change; what is their actual objection?
- Late adopter — who comes last, and what do they need that early adopters don't?

**Why these work:** Change initiatives fail because skeptics and late adopters are not consulted. Including them explicitly surfaces the friction points before implementation rather than after.

---

### Infrastructure and Cloud Platform Decisions

**Standard (4 perspectives):**
- Developer experience — ease of local development, deployment, and debugging day-to-day
- Cost at scale — what does this cost at 10x current load? Where are the non-linear cost jumps?
- Reliability / SRE — failure modes, recovery time, and what gets paged at 3am
- Security — IAM boundaries, network exposure, data classification, and encryption requirements

**Deep (add 1):**
- Vendor lock-in — what is the migration cost if this vendor relationship ends in 3 years?

---

## Perspective Naming

Name perspectives by role plus specific concern, not just role title.

| Weak | Strong |
|------|--------|
| "Developer" | "Developer who owns this service for the next 2 years" |
| "User" | "Mobile user on a slow connection with limited time" |
| "Business" | "Business stakeholder responsible for Q3 revenue targets" |
| "Security" | "Security engineer responsible for the compliance audit" |

Specific framing produces grounded analysis. Generic titles produce generic analysis.

---

## Perspective Quality Checklist

Before running the analysis:
- [ ] At least two perspectives are likely to disagree on the central question
- [ ] Every perspective has genuine stake in the outcome
- [ ] No two perspectives are so similar they will produce the same analysis
- [ ] The most important critic or skeptic is represented
- [ ] Each perspective is grounded in a real role or constraint, not an abstraction
- [ ] The question is framed as a decision, not a topic
