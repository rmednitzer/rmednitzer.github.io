# Site Patch Changelog -- 2026-05-28 (batch 8: honesty & concision realignment)

Reverted the batch-7 "High-Assurance Infrastructure Architecture & Systems
Validation" positioning to an honest, concise profile at the site owner's
request: Senior Linux & Platform Engineer, autodidact, open source by default.
Copy was aligned with the owner's CVs (day-to-day production ops) without
overindexing on them, and the AI/agent-governance and EU-regulatory material was
reframed as homelab, open-source, and learning rather than professional
high-assurance services. The audit also fixed two real defects (a broken link
and a license mismatch). No build step, no JS added, no trackers; fonts stay
self-hosted; all new CSS stays page-unique in the `index.html` `<head>`.

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Retitled across `<title>`, description, OG/Twitter, and JSON-LD `jobTitle`/`description` to "Senior Linux & Platform Engineer" | Honest identity per the owner |
| 2 | Removed the "Regulatory Trust Boundaries", "Invariant Matrix", and "Observability & Verification" sections | Cut overclaim; "keep it short." New flow: hero -> About -> Open-source projects -> Homelab -> Skills |
| 3 | De-jargoned the hero: dropped thesis/register/deterministic-envelope copy; honest `.hero-meta` (focus / experience / approach) | Plain language |
| 4 | Featured only relay-shell + agents (README-grounded, pre-1.0, Apache-2.0); linked the rest via github.com/rmednitzer | Owner: these two are the most mature; de-emphasise the simulators |
| 5 | Replaced the 47-tag keyword dump with grouped Skills aligned to CV proficiency | Scannable, honest |
| 6 | Trimmed JSON-LD `knowsAbout` to a defensible set; reduced `memberOf` to OCG + IEEE | Remove aspirational claims |
| 7 | Fixed broken link: `sentinel` pointed at `/sentinel/` (404 -- no such directory) -> removed | Bug |
| 8 | Footer code license GPLv3 -> Apache-2.0 (matches the LICENSE file) | Bug |
| 9 | Trimmed page-unique CSS (removed `.boundaries`/`.boundary` and `.repo-item`; added the `.skills` grid) | Match new markup |

## Other files

| File | Change |
|------|--------|
| `legal.html` | Code license GPLv3 -> Apache-2.0; editorial-direction wording matched to a profile site |
| `site.webmanifest` | `name`/`description` -> Senior Linux & Platform Engineer |
| `README.md` | Tagline -> honest profile summary |
| `CLAUDE.md` | Topic line updated to the new positioning |

# Site Patch Changelog -- 2026-05-28 (batch 7: high-assurance position realignment)

Structural realignment from generic "platform/infrastructure engineer" to
"High-Assurance Infrastructure Architecture & Systems Validation," targeting
principal engineers and technical scouts in defence tech, critical
infrastructure, and EU high-assurance validation. Core thesis surfaced
throughout: gating non-deterministic/stochastic runtimes behind deterministic
safety envelopes, STPA hazard modeling, and programmatic boundary enforcement.
Footprint stays sovereign (no build step, no JS added, no trackers, fonts
self-hosted); all new CSS is page-unique in the `index.html` `<head>` block per
CLAUDE.md, so `style.css` is untouched.

Every technical claim was verified against the in-workspace repositories before
landing. Where the source brief proposed copy that the repos contradict or do
not yet support, the claim was rewritten to the verified mechanism rather than
shipped as written — continuing the batch-6 norm of refusing fabrication on a
profile that a code-reading audience will check.

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Retitled positioning across `<title>`, description, OG/Twitter, hero `.hero-sub`/`.hero-tagline`, and JSON-LD `jobTitle`/`description` to "High-Assurance Infrastructure Architecture & Systems Validation" | Req 1 structural position realignment |
| 2 | Added a config-style `.hero-meta` key/value strip (locale / register / thesis / methods) under the tagline | Replaces whitespace with scannable technical metadata (style directive) |
| 3 | Rewrote About to the deterministic-envelope thesis (contracts, tiered authority, action budgets, fail-closed, append-only evidence, STPA-before-mechanism, EU mandate mapping) | Req 1 intro pivot; verified against agents + relay-shell + STPA repos |
| 4 | Added "Regulatory Trust Boundaries" section: framework → enforced-mechanism rows (NIS2/ISO 27001, EU AI Act/CRA, AI Act high-risk/Machinery, DORA, GDPR) | Req 2 compliance-as-trust-boundaries, config-style grid |
| 5 | Added "Observability & Verification" section: metrics/traces (OTel→VictoriaMetrics), JS-divergence drift, append-only evidence + run-provenance gate, property/fuzz regression, Wazuh SIEM | Req 4 telemetry/verification showcase |
| 6 | Open-Source list reworked: added `nous`, reordered, rewrote platform-blueprint / agents / relay-shell / mission-assurance descriptions to high-assurance mechanics | Req 3 project-corpus refactor |
| 7 | Technologies: added `ISO 42001`, `STPA`, `Boundary Contracts` tags | Reflect the high-assurance positioning; all accurate |
| 8 | Page-unique CSS added in `<head>`: `.hero-meta`, `.boundaries`/`.boundary` (responsive framework→mechanism grid), inline `code`; extended fade-up `nth-child` delays to cover the two new sections | Denser, config-style layout (style directive); promote to `style.css` if reused on another page |

## Accuracy corrections — brief copy NOT shipped as written

| Brief copy | Why not shipped verbatim | Shipped instead |
|---|---|---|
| relay-shell "system-level process sandboxing" | Contradicts ADR 0002 (Accepted): relay-shell is **unsandboxed by design**; service account is the trust boundary. ADR 0006 seccomp-notify is **audit-only** and only *Proposed* | "Unsandboxed by design — the service account is the trust boundary"; compensating controls listed |
| AI isolation "via systemd scopes, cgroups tracking, and seccomp notification filters" | Not the implemented mechanism. agents ships subprocess + `rlimit`; container/seccomp/namespace is an explicit **out-of-tree extension point**. Real inference isolation is ai-stack k8s PSA (restricted, `seccompProfile: RuntimeDefault`, default-deny NetworkPolicy) | k8s Pod Security + bounded subprocess/`rlimit`; capability/namespace isolation noted as extension point |
| "cryptographically signed forensic ledger" | relay-shell audit is SHA-256 **hashed** append-only, not signed. QES signing exists only in the `isms` document layer (`verify_qes.py`) | Output-hashed append-only ledger for the runtime; QES verification attributed to ISMS records |
| platform-blueprint "Canonical GitOps reference overlays" | Repo states it is **documentation, not deployable code**; ships no kustomize/overlays | "Reference architectures, design patterns, and EU compliance mappings … documentation, not deployable code" |
| "operator-resilience" repo | No such repo exists | Mapped to `mission-assurance` operator/cyber-physical domain (STPA UCA) + `nous` |
| "real-time latency distribution tracking (inference jitter vs. deterministic gate overhead)" | No latency-histogram/jitter instrumentation found in repos | OTel→VictoriaMetrics timing + action-budget wall-clock bounds, framed as separating gate overhead from inference time |

## Validation (req 3 / execution directives)

- Link targets verified against in-workspace repos: platform-blueprint, agents, relay-shell, nous, mission-assurance, automation → `github.com/rmednitzer/<repo>`; sentinel → published `/sentinel/` project pages (unchanged).
- `html-validate index.html`: my additions are clean (all `&` encoded as `&amp;`). The 3 reported errors (lowercase `<!doctype>`, >70-char title, raw `&` in the pre-existing `/legal` footer link) predate this batch and are left untouched per scope.
- Tag balance verified; local serve returns HTTP 200; no build/static-gen config exists (raw static HTML/CSS), no external scripts/analytics/font CDNs added.

---

# Site Patch Changelog -- 2026-05-28 (batch 6: Invariant Matrix + engineering-first de-warm)

Refactor toward a peer-engineer register (user direction). Adds a static
Invariant Matrix and strips portfolio warmth; scope confirmed via questions
(matrix = agents + relay-shell, static not live, moderate de-warm, relay-shell
description rewritten). nous and mission-assurance were intentionally left
untouched: neither is in the workspace/scope, so their high-assurance invariants
could not be verified without fabrication. Favicon and all visual tokens are
unchanged. Footprint stays sovereign (no build step, no JS added, no trackers).

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Added an "Invariant Matrix" section (static, no JS) after About: per-repo spec cards for agents and relay-shell with Boundary / Control / Isolation / Audit rows | Replaces abstraction summaries with at-a-glance verified constraints (req 2). STPA omitted: neither repo tracks hazards via STPA, so claiming it would be fabrication |
| 2 | Removed the "Domains" section (4 capability cards) | Superseded by the Invariant Matrix per user direction |
| 3 | Removed the "Organizations" (IEEE/OCG) and "Current Focus" blocks | Moderate de-warm: drop resume/corporate filler. `memberOf` retained in JSON-LD as accurate structured data |
| 4 | Rewrote relay-shell description to primitives; sharpened agents | Peer-engineer register (req 1), verified against each repo |
| 5 | Un-truncated `.repo-meta` (removed nowrap/ellipsis) | Constraints in descriptions must be readable, not clipped |
| 6 | Tersed the About paragraphs | Engineering-first density (req 2) |
| 7 | Swapped dead `.domains/.domain`, `.org-list`, `.bottom-grid` CSS for the `.matrix/.spec` component; no new fonts/JS | Component for the matrix; shared `style.css` left untouched except dead-rule removal |

## `style.css`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Removed `.focus-asof` (dead after the Current Focus block was removed) | Cleanup |

## Validation (req 3)

- No build/static-gen config exists; raw static HTML/CSS served from repo root. That is the lightweight, sovereign footprint.
- No external scripts, analytics, trackers, or font CDNs; only an inline footer-year updater + inline JSON-LD; fonts self-hosted.
- All GitHub cross-links resolve (platform-blueprint, mission-assurance, agents, relay-shell, automation; sentinel local). Matrix links to agents and relay-shell verified in-workspace.

---

# Site Patch Changelog -- 2026-05-28 (batch 5: multi-provider AI tags)

Makes the "stack-agnostic over an API" point concrete per user note (uses
Gemini, OpenAI/ChatGPT, and Claude via web and API, alongside local models).

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | About para 2: extended the stack-agnostic clause to name the stack (local models on own hardware plus the Claude, OpenAI, and Gemini APIs) | Grounds the existing claim in the actual multi-provider usage |
| 2 | Technologies: added `Claude`, `OpenAI`, `Gemini` tags, unaccented | Reflect real multi-provider AI use; accenting stays reserved for the open-source identity since these are proprietary |
| 3 | JSON-LD knowsAbout: added Anthropic Claude, OpenAI, Google Gemini | Consistency with the new tags |

---

# Site Patch Changelog -- 2026-05-28 (batch 4: rework + optimize — separate Homelab from Open-Source)

Structural rework and cleanup. Per user direction the homelab and GitHub are now
presented as separate things, and dead CSS left over from the removed article
pages is dropped. The favicon and all its files/URLs are untouched (reused by
other services, e.g. vertex.blackphoenix.org); visual design tokens (colours,
fonts, accent, dark/light, grid background), the hero, title, and meta are
unchanged.

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Split the combined "Homelab & Open-Source" section into two sections: **Homelab** (the self-run fleet, two short paragraphs, no repo links) and **Open-Source** (the pinned GitHub repos with a lead-in). Dropped the "pinned repositories below are the artifacts" tie-in | User direction: GitHub and the homelab should be seen as separate. Homelab = what I run; Open-Source = what I publish |
| 2 | Renamed the legacy `.writing-*` classes (left from the deleted Writing section) to semantic `.repo-list` / `.repo-item` / `.repo-name` / `.repo-meta` in the page `<style>` block and markup | Clarity: the list holds repos, not writing. No visual change |
| 3 | Domains card 4: "AI Assurance (Homelab R&D)" → "AI Assurance (R&D)" | Avoids "Homelab" doubling now that there is a dedicated Homelab section; body already says "self-run track" |
| 4 | Removed the trailing ` /` self-close on the `google-site-verification` `<meta>` | Consistency with the other void `<meta>` elements; clears the html-validate `void-style` error |

## `style.css`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Removed dead rules left from the deleted article pages: `.article-tags`, `.article-meta`, and the entire `.article-related*` block | Unused by both `index.html` and `legal.html` (verified). Smaller stylesheet |
| 2 | Renamed `.writing-list li + li` → `.repo-list li + li` | Matches the renamed repo list |

Kept (still used by `legal.html`): `.page--article`, `.article-nav`, `.article-header`, `.article-body` and children.

## `legal.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Removed the trailing ` /` self-close on the `google-site-verification` `<meta>` | Same as index; consistency + validator |

---

# Site Patch Changelog -- 2026-05-28 (batch 3: realign to actual fleet + open-source preference)

Realigns the site to what is actually run day-to-day, verified against the
operator's own running fleet. That fleet is all open source and mostly Ubuntu,
and the technologies below are the ones the public site now names: local LLM
inference (llama.cpp/llama-swap on NVIDIA, Ollama on AMD ROCm), a self-built MCP
gateway with PydanticAI agents, and a single-node Talos K8s cluster running
VictoriaMetrics + OpenTelemetry + Grafana observability and a Wazuh SIEM. Per
user direction, closed-source tools that only appear in the regulated day job
(VMware, Veeam, SEP sesam, Checkmk, Azure, Windows Server, Tanzu) are
de-emphasised; the day job stays acknowledged honestly but is no longer the
site's identity. No design/CSS-file changes.

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | About para 2: added a sentence stating the preference (open source over closed, mostly Ubuntu and Red Hat, stack-agnostic wherever AI integration is viable over an API) | User direction: "just because I have to work with something professionally doesn't mean I enjoy it." Encodes the stated preference verbatim in intent |
| 2 | Homelab note: rewrote to the verified fleet (all-open-source, mostly-Ubuntu; llama.cpp/llama-swap on NVIDIA + Ollama on AMD ROCm; MCP gateway fronting PydanticAI agents and OSINT/CVE/EU-regulatory intel; Talos K8s with VictoriaMetrics/OTel/Wazuh; ZFS+Sanoid; Tailscale mesh). Replaced "WireGuard" with "Tailscale" (the actual tool) | Accuracy: matches the operator's own verified fleet state. Foregrounds the open-source/local-AI reality |
| 3 | Domains card 1 (Infrastructure & Reliability): replaced "virtualisation (VMware, KVM)" with "Production Linux (Ubuntu, Red Hat), KVM and libvirt virtualisation, ZFS with Sanoid snapshots" | VMware is day-job only; the fleet uses KVM/libvirt + ZFS/Sanoid (open source) |
| 4 | Domains card 2 (Platform Engineering): replaced "Argo CD … Terraform/OpenTofu" with "Kubernetes (Talos), Helm, OpenTofu and Ansible … container and local-inference pipelines" | Matches the fleet (Talos/Helm/OpenTofu/Ansible). Dropped Terraform (now BSL/source-available) in favour of OpenTofu (open source) |
| 5 | Domains card 4 (AI Assurance): grounded the prongs in the real stack (self-hosted models behind a governed MCP gateway, PydanticAI agents under runtime control points) | Concrete artifacts over abstractions; matches relay-shell and agents |
| 6 | Current Focus: rewrote as an honest two-part split — "by day" the regulated enterprise estate (generic: virtualisation, backup/DR, monitoring, change management under ISO 27001/NIS2), "by preference and after hours" the all-open-source mostly-Ubuntu AI fleet | User direction: acknowledge the day job without making the tolerated closed stack the identity. Removed the specific closed-product names (VMware vSphere, Veeam, SEP sesam, Checkmk, Tanzu) |
| 7 | Technologies: removed closed day-job-only tags (Windows Server, VMware, Veeam, Azure, Checkmk) and Terraform (BSL); added open-source/AI-fleet tags (Ubuntu, Open Source, Talos, MCP, PydanticAI, llama.cpp, Ollama, SearXNG, CUDA, ROCm, VictoriaMetrics, Tailscale); re-tiered accents to identity (Linux, Ubuntu, Open Source, Kubernetes, MCP, PydanticAI, ISO 27001, NIS2). Dropped Argo CD/Backup-DR/GitOps accents | Tags read as the toolkit/identity he leads with; align with actual practice + stated open-source preference |
| 8 | JSON-LD knowsAbout: removed the closed-product brand names (VMware, Veeam, Microsoft Azure, Checkmk); added Ubuntu, Open Source Software, Talos Linux, VictoriaMetrics, llama.cpp, Ollama, PydanticAI, Model Context Protocol, Retrieval-Augmented Generation, Local Large Language Models, Tailscale | Keep structured data consistent with the realigned identity; generic capabilities (Virtualization, Backup and Recovery, Windows Server) retained as honest knowledge |

---

# Site Patch Changelog -- 2026-05-28 (batch 2: ops-first alignment + homelab framing)

Realigns site copy with the proven strengths in the provided CV/profile PDFs
(ops-first) and frames the AI-assurance work as homelab R&D. The pinned-repo
list is unchanged (already mirrors the 6 GitHub pins). No design/CSS-file
changes; the homelab note reuses `.section p` plus one page-local spacing rule.

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | About para 2: replaced the "seam between platform operations and systems assurance / policy-enforced delivery / runtime control points" framing with a grounded line (evidence chains and controls mapped to ISO 27001 / NIS2, ISMS/BCM work, ISO 27001 auditor qualification), then explicitly labels the agentic-AI/observability work as self-run homelab exploration | User direction: ops-first, grounded. AI-assurance is a clearly-labeled forward/R&D track, not established practice. ISMS/BCM and the ISO 27001 Manager & Auditor qualification are proven in the CV |
| 2 | Open-Source Work: renamed heading to "Homelab & Open-Source" and added one intro paragraph describing the real homelab (single-node Talos K8s with VictoriaMetrics/OpenTelemetry/Wazuh, NVIDIA RTX local-LLM compute, ZFS + Sanoid, WireGuard, self-hosted MCP gateway on Hetzner). Repo list unchanged | User direction: "pinned repos are my main homelab work"; add a short homelab note. Content sourced from the CV free-text |
| 3 | Added page-local rule `.section p + .writing-list { margin-top: .85rem; }` to the index `<style>` block | Spacing between the new intro paragraph and the repo list; kept page-unique layout out of shared `style.css` per conventions |
| 4 | Domains card 4: retitled "Assurance & AI Governance" → "AI Assurance (Homelab R&D)" and reworded to read as exploratory work ("a self-run track exploring…", "early work, not a service line"); kept supply-chain fundamentals (SBOM/SLSA/Sigstore) | User direction: ops-first. The card previously read as a claimed service line; the PDFs support this only as forward/homelab work |
| 5 | Technologies: added proven CV tools (`Red Hat`, `CI/CD`, `GitLab`, `Checkmk`, `ZFS`, `Veeam`, `Azure`); accented `Backup/DR`; de-accented `Prometheus` | Align tags with the CV "Kenntnisse" list and the current-role stack (Checkmk/Veeam are current monitoring/backup). Prometheus is not in the German CV (Checkmk/Zabbix/Grafana are the day-job monitors), so it stays as a plain tag |
| 6 | Current Focus: named the current-role stack (Windows Server + Linux SLES/Rocky, VMware vSphere, Veeam/SEP sesam, Checkmk, Tanzu Kubernetes + Argo CD GitOps) | More accurate to what is actually done day-to-day per the CV; kept employer unnamed per existing site style |
| 7 | JSON-LD: added `ZFS`, `Red Hat Enterprise Linux`, `CI/CD`, `GitLab`, `Microsoft Azure`, `Checkmk`, `Veeam`, `ISMS` to `knowsAbout`; bumped `dateModified` to 2026-05-28 | Keep structured data consistent with the new tags; existing AI/assurance entries remain valid "knows about" claims |

## `sitemap.xml`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Bumped `/` `lastmod` to 2026-05-28 | Index content changed substantively |

---

# Site Patch Changelog -- 2026-05-28 (batch 1: open-source list mirrors pinned repos)

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Open-Source Work: replaced the 5-entry list (`platform-blueprint`, `isms`, `agents`, `sentinel`, `core-graph`) with the 6 pinned GitHub repos, ordered platform/EU-assurance flagships first: `platform-blueprint`, `mission-assurance`, `agents`, `relay-shell`, `sentinel`, `automation`. Added `mission-assurance`, `relay-shell`, `automation`; dropped `isms`, `core-graph` | User direction: site should reflect the highest-value (pinned) repos. Descriptions and Apache-2.0 licenses verified against each repo's GitHub About text; `sentinel` keeps its local `/sentinel/` Pages dashboard link |

---

# Site Patch Changelog -- 2026-05-17 (batch 1: open-source list)

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Open-Source Work: replaced the `ai-stack` entry with `agents` (`https://github.com/rmednitzer/agents`, meta "Agentic workloads, skills, harness, and memory infrastructure · Apache 2.0") and reordered the list to `platform-blueprint`, `isms`, `agents`, `sentinel`, `core-graph` | User direction: swap `ai-stack` for the `agents` repo and order entries by professional relevance (platform/EU-assurance flagships first) |

---

# Site Patch Changelog -- 2026-05-14 (batch 6: copy refresh)

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Rewrote About paragraphs: split em-dash sentences into two; reworded second paragraph so AI Act and CRA are referred to as "obligations approaching" rather than "emerging expectations" | AI Act (Reg 2024/1689) and CRA (Reg 2024/2847) are already in force with staggered application; "expectations" is inaccurate |
| 2 | Audit-Facing Operations card: replaced em-dash with comma | No em-dashes in prose |
| 3 | Current Focus card: replaced "Driving Kubernetes and Argo CD adoption" framing with steady-state platform-operations description (Linux/Windows Server, VMware/KVM, backup/DR, monitoring, change management aligned to ISO 27001 and NIS2) | Drop consultancy verb; remove "expectations come into force" wording |

## `legal.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | § 5 ECG line: replaced em-dash inside the parenthesised gloss with a comma | No em-dashes in prose |
| 2 | Fonts line: split em-dash sentence into two sentences | No em-dashes in prose |

---

# Site Patch Changelog -- 2026-05-14 (batch 5: review fixes for PR #31)

## `legal.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Removed `<link rel="alternate" type="application/atom+xml">` pointing at the deleted `feed.xml` | Codex review on PR #31: discoverable URL now 404s after feed removal |

## Removed directory

| Path | Rationale |
|------|-----------|
| `scripts/` (`generate-og-images.js`, `package.json`) | Copilot review on PR #31: script hard-codes the four removed article slugs. Site is now single-page; the only OG image needed is the profile portrait, so the generator and its `scripts/` housing are dead code |

## `CLAUDE.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Removed all `scripts/`-related notes (Stack bullet, Layout entry, OG-image guidance, "Things to avoid" `scripts/node_modules/` mention) and simplified the OG guidance to "site OG image is the profile portrait" | Reflects deletion of `scripts/` |

---

# Site Patch Changelog -- 2026-05-14 (batch 4: site simplification)

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Removed Writing section entirely | User direction: simplify site to a single-page profile |
| 2 | Reduced Open-Source list from 10 to 5 entries: `platform-blueprint`, `isms`, `sentinel`, `ai-stack`, `core-graph` | User direction: cap repo list at 5; refocus on the most representative artifacts |
| 3 | Rewrote Current Focus paragraph; removed "Windows Server" mention | User direction |
| 4 | Tightened hero tagline, meta/OG/Twitter descriptions, About, and all four Domain card bodies | User direction: rework site text to be more focused |
| 5 | Removed `<link rel="alternate" type="application/atom+xml">` and `hasPart` array from ProfilePage JSON-LD | No articles remain to syndicate |

## Removed files

| File | Rationale |
|------|-----------|
| `behavioral-contracts-human-autonomy-teaming.html` | Writing block removed |
| `agentic-ai-regulated-infrastructure.html` | Writing block removed |
| `it-operations-architecture.html` | Writing block removed |
| `enforceable-boundary-contracts.html` | Writing block removed |
| `og-behavioral-contracts-human-autonomy-teaming.png` | Article OG card no longer used |
| `og-agentic-ai-regulated-infrastructure.png` | Article OG card no longer used |
| `og-it-operations-architecture.png` | Article OG card no longer used |
| `og-enforceable-boundary-contracts.png` | Article OG card no longer used |
| `feed.xml` | Atom feed had only the four removed articles |

## `sitemap.xml`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Removed the four article entries; site now lists `/` and `/legal` only | Articles deleted |

## `README.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Reduced Pages table to Profile + Legal; updated tagline to match new hero | Site is now single-page |

## `CLAUDE.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Removed article-pages table, feed.xml references, per-article OG image conventions, "Atom alternate link" requirement, article-page-only markup notes, and Writing-section discoverability step | Reflect simplified single-page layout |

## `.github/copilot-instructions.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Replaced article filenames in Key files list with `legal.html` | Reflect simplified single-page layout |

---

# Site Patch Changelog -- 2026-05-14 (batch 3: trim batch-2 positioning back to conservative restore)

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Reverted `<title>` / `og:title` / `twitter:title` to "Roman Mednitzer \| Senior Platform & Infrastructure Engineer · Linux · Kubernetes · GitOps" | User direction (Conservative restore only): drop the " · EU Assurance" extension that batch-2 added to the headline |
| 2 | Reverted `hero-sub` to "Vienna, AT · Senior Platform & Infrastructure Engineer · Linux · Kubernetes · GitOps" | Same — drop the " · Audit-Defensible Platform Ops · EU Assurance" extension |
| 3 | Reverted meta/OG/Twitter description and JSON-LD `description` to batch-1 form | Drop the "Governance-as-code via platform-blueprint; live HAT failure-mode corpus via sentinel" sentence; do not promote centerpieces in description text |
| 4 | Reverted JSON-LD `jobTitle` to "Senior Platform & Infrastructure Engineer" | Drop the " · Audit-Defensible Platform Ops · EU Assurance" extension |
| 5 | Reverted About paragraph 2 and Current Focus to batch-1 form | Drop the "Two active centerpieces — platform-blueprint and sentinel" prose; centerpieces stay in the Open-Source list rather than being promoted in body text |
| 6 | Reverted Open-Source list to batch-1 order: `platform-blueprint`, `platform-assurance`, `isms`, `ansible-ops`, `infra-ops`, `cps-assurance`, `autonomous-platform-assurance`, `operator-resilience`, `sentinel` | Sentinel back to its batch-1 position at the end; descriptions returned to short batch-1 form |
| 7 | Added new Open-Source entry: `6dof-ascent-sim` (Apache 2.0) | User direction: list it — high-fidelity 6DOF orbital launch vehicle simulation, ignition through LEO insertion |
| 8 | Trimmed Domain card 4 body text: removed inline `<code>platform-blueprint</code>` / `<code>sentinel</code>` references; kept the "Assurance & AI Governance" heading and the four-prong scope (governance-as-code mapping, agentic-AI guardrails + HAT, supply-chain, boundary contracts) | Voice-consistent with the reverted About / Current Focus prose; specific artifacts cross-referenced via Writing + Open-Source Work above |
| 9 | Trimmed Technologies tags: removed `Talos`, `VictoriaMetrics`, `Governance-as-Code` (accent), `Boundary Contracts` (accent), `Human-Autonomy Teaming`, `STPA`, `MCP`, `pgvector`, `Apache AGE` that batch-2 added | Conservative restore: re-add only what batch-1 removed (`Wazuh`, `MLOps`, `LLMOps`, `AI Governance` — all kept), not new positioning tags. Accent demoted on `AI Governance` to non-accent for matching tone |
| 10 | Trimmed JSON-LD `knowsAbout`: removed `Talos Linux`, `VictoriaMetrics`, `Governance-as-Code`, `Model Context Protocol`, `Graph Databases`, `pgvector`, `Apache AGE` that batch-2 added | Same rationale as the tag trim. Kept the originally-removed scope entries (`MLOps`, `LLMOps`, `AI Governance`, `Human-Autonomy Teaming`, `Behavioral Contracts`, `Cyber-Physical Systems`, `STPA`, `Boundary Contracts`) — these are what the user asked to put back |

Net result: batch-1 form everywhere except for (a) Apache 2.0 license suffixes on `ansible-ops` / `infra-ops` (Copilot review #2 fix, retained), (b) Domain card 4 "Assurance & AI Governance" rename with broader scope text (per user instruction to "put back Domain text I removed"), (c) `knowsAbout` and Technologies tag restorations of the AI/HAT/governance entries that batch-1 removed (per user instruction), and (d) new `6dof-ascent-sim` Open-Source entry.

---

# Site Patch Changelog -- 2026-05-14 (batch 2: rebalance + Copilot review fixes)

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Extended `<title>` / `og:title` / `twitter:title` to "Senior Platform & Infrastructure Engineer · Linux · Kubernetes · GitOps · EU Assurance" | Copilot review (PR #30): previous social-preview titles still surfaced the deprecated "Linux Infrastructure, Platform Operations, Systems Assurance" wording inconsistent with new descriptions and hero-sub |
| 2 | Extended `hero-sub` to include "Audit-Defensible Platform Ops · EU Assurance" | Restores the right half of the LinkedIn headline that batch-1 truncated |
| 3 | Reorganised Open-Source list to lead with `platform-blueprint` and `sentinel` as the two centerpieces | User direction: focus the narrative on the two active centerpieces; other governance-as-code repos remain as supporting context |
| 4 | Tightened repo descriptions for `platform-blueprint` and `sentinel`; promoted `sentinel` from last to second position | Centerpieces deserve descriptive lines, not just slug + license |
| 5 | Added `· Apache 2.0` suffix to `ansible-ops` and `infra-ops` entries | Copilot review (PR #30): license metadata omitted vs. surrounding entries; verified both repos are Apache-2.0 via repo landing page |
| 6 | Renamed Domain card 4 "Assurance & Supply-Chain" → "Assurance & AI Governance"; rewrote body to name `platform-blueprint`, `sentinel`, and supply-chain fundamentals as the four prongs | Batch-1 narrowed this card to supply-chain only; that undersold the governance-as-code + agent-runtime work that the public portfolio actually contains |
| 7 | Restored AI/HAT/governance tags to Technologies: `Governance-as-Code` (accent), `AI Governance` (accent), `Boundary Contracts` (accent), `Human-Autonomy Teaming`, `STPA`, `MLOps`, `LLMOps`, `MCP`, `pgvector`, `Apache AGE`, `Talos`, `VictoriaMetrics`, `Wazuh` | Each tag corresponds to a public artifact: platform-blueprint (governance-as-code, AI governance), operator-resilience + sentinel (HAT, behavioral contracts, STPA), ai-stack + sentinel (MLOps/LLMOps), isms-mcp + vertex (MCP), core-graph (pgvector/AGE), fleet host axiom (Talos, VictoriaMetrics, Wazuh) |
| 8 | Restored `knowsAbout` entries that batch-1 removed: `MLOps`, `LLMOps`, `AI Governance`, `Human-Autonomy Teaming`, `Behavioral Contracts`, `Cyber-Physical Systems`, `STPA`, `Boundary Contracts`, `Model Context Protocol`, `Graph Databases`, `pgvector`, `Apache AGE`, `Governance-as-Code`, `Talos Linux`, `VictoriaMetrics`, `Wazuh`, `Machinery Regulation` | These map 1:1 to public repos or fleet hosts; batch-1 trimmed them as "writing topics" but the artifacts make them legitimate `knowsAbout` claims |
| 9 | Extended JSON-LD `jobTitle` to "Senior Platform & Infrastructure Engineer · Audit-Defensible Platform Ops · EU Assurance" | Mirrors LinkedIn headline; consistent with extended page title and hero-sub |
| 10 | Updated meta/OG/Twitter descriptions and JSON-LD `description` to name the two centerpieces explicitly | Single description string across all surfaces; centers the narrative on `platform-blueprint` + `sentinel` |
| 11 | Rewrote About paragraph 2 and Current Focus to name `platform-blueprint` and `sentinel` by slug | Concrete artifacts beat abstract framing; reader can click through directly |

## `README.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Updated tagline to byte-identically mirror the new `index.html` `.hero-tagline` paragraph | Copilot review (PR #30): README and hero tagline had drifted; align as single source of truth |

## `CHANGELOG.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Restored heading + `## README.md` table header for the orphaned 2026-05-06 batch-2 rows below | Copilot review (PR #30): markdown rendered as broken/ambiguous after the new 2026-05-14 entry was prepended; dated header verified via `list_commits` against `c5131b8` (PR #29, 2026-05-06 10:23 UTC) |

---

# Site Patch Changelog -- 2026-05-14 (batch 1)

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Rewrote hero tagline, About, and Current Focus to align with profile (PDF) | Previous wording oversold "design" and "compliance evidence as byproduct" beyond what the operator-level role supports; now leads with what is actually done day-to-day |
| 2 | Updated `hero-sub` to "Senior Platform & Infrastructure Engineer · Linux · Kubernetes · GitOps" | Matches profile headline rather than three abstract focus areas |
| 3 | Re-tiered Technologies tags; removed Keycloak, Wazuh, Checkmk, Proxmox, Zarf, MLOps, LLMOps, AI Governance | None of these appear in profile experience; removing avoids implying hands-on use |
| 4 | Added Windows Server, KVM, Argo CD, OpenTofu, Zabbix, Sigstore, Backup/DR; accented Argo CD, Ansible, Prometheus, NIS2 | Reflects actual stack from profile (EBCONT/Kwizda/medPhoton) |
| 5 | Rewrote Domains "Governance & Compliance" → "Audit-Facing Operations" and "Assurance & AI Integration" → "Assurance & Supply-Chain" | Drops claims of "observability for AI/ML workloads" and "policy-as-code controls"; keeps what is supported by profile (SBOM/SLSA/Sigstore fundamentals, ISO 27001/NIS2 alignment) |
| 6 | Expanded Open-Source list with `platform-blueprint`, `ansible-ops`, `infra-ops`; removed `isms` placeholder note since repo is live | Surfaces operational/IaC repos alongside governance-as-code repos so the mix reflects the actual day job, not only research |
| 7 | Trimmed `knowsAbout` in ProfilePage JSON-LD; removed MLOps, LLMOps, AI Security, AI Governance, Human-Autonomy Teaming, Behavioral Contracts, Cyber-Physical Systems, STPA, Boundary Contracts | These are writing topics, not operational expertise — moved out of the "knows about" claim list |
| 8 | Added `knowsLanguage: ["de", "en"]` to JSON-LD | Profile is bilingual; previously omitted |
| 9 | Updated `jobTitle` from "Linux Infrastructure, Platform Operations, Systems Assurance" to "Senior Platform & Infrastructure Engineer" | Matches profile headline |
| 10 | Updated meta/OG/Twitter descriptions and JSON-LD `description` | Same rationale as 1 — replaced marketing line with profile-accurate one |
| 11 | Bumped `dateModified` to 2026-05-14 | Index content changed substantively |

## `README.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Updated public tagline to match new index tagline | Single source of truth |

## `sitemap.xml`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Bumped `lastmod` on `/` to 2026-05-14 | Index content changed substantively |

---

# Site Patch Changelog -- 2026-05-06 (batch 2: accuracy pass, PR #29)

## `README.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | (row content lost from upstream merge; rows 2 and 3 below are preserved as-committed) | — |
| 2 | Reordered article table reverse-chronologically | Most recent article first matches the index.html Writing list order |
| 3 | Updated tagline | Site-wide tagline alignment |

## `CLAUDE.md`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Updated `Topic` line | Site-wide tagline alignment |

---

# Site Patch Changelog -- 2026-05-06 (batch 1: sentinel cross-reference, PR #28)

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Added new `Live Work` section between Writing and Domains | Surface shipped empirical work alongside theoretical writing. Mirrors `.writing-list` styling. Single entry: link to `/sentinel/`, the continuous HAT failure-mode classification corpus |

## `behavioral-contracts-human-autonomy-teaming.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Added one paragraph after the seventh structural-gap paragraph (field study gap) | Cross-references `/sentinel/` as a small counter-example operating in deployed conditions, with explicit acknowledgement of N=1 and LLM-derived classification limits |

---

# Site Patch Changelog -- 2026-03-28 (batch 2)

## `style.css`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Added `.page--article` shared layout class | Extracted from duplicated `<style>` blocks across article pages |
| 2 | Added `.writing-list li + li` spacing rule | Replaced inline `style="margin-top: .5rem;"` on index.html |
| 3 | Added `.article-related` component styles | Replaced inline styles on related article nav blocks across all article pages |

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Moved Writing section above Domains | Writing is the strongest differentiator and should be seen first |
| 2 | Rewrote About to lead with thesis, not timeline | The differentiating value prop was buried behind a CV opening line |
| 3 | Rewrote Current Focus to be specific and non-overlapping with About | Previous text restated the About thesis |
| 4 | Changed `<div class="page" role="main">` to `<main class="page">` | Semantic HTML |
| 5 | Removed inline `margin-top` styles from writing list items | Moved to style.css per project conventions |
| 6 | Updated animation-delay sequence for new section order | Maintains stagger after reorder |

## `enforceable-boundary-contracts.html`, `it-operations-architecture.html`, `agentic-ai-regulated-infrastructure.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Added `page--article` class to `.page` div | Uses shared layout from style.css |
| 2 | Removed duplicated `.page` / animation CSS from `<style>` blocks | Now in style.css |
| 3 | Replaced inline styles on `.article-related` with classes | Moved to style.css per project conventions |

## `.well-known/security.txt`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Changed Policy URL from `/` to `/legal` | Points to dedicated legal notice page |

---

# Site Patch Changelog — 2026-03-28

## New file: `legal.html`
- Dedicated legal notice page: Impressum (§ 5 ECG), Offenlegung (§ 25 MedienG), Datenschutzerklärung (DSGVO), copyright notice, liability disclaimer
- Satisfies "large website" Offenlegungspflicht including grundlegende Richtung
- Linked from footer on all pages

## `index.html`, `enforceable-boundary-contracts.html`, `it-operations-architecture.html`, `agentic-ai-regulated-infrastructure.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Replaced inline impressum text in footer with link to `/legal` | Dedicated legal page is cleaner and satisfies MedienG requirement for clearly labelled, easily accessible legal notice |

## `sitemap.xml`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Added `/legal` entry (priority 0.3, yearly) | New page needs to be discoverable |

---

# Site Patch Changelog — 2026-03-07

All changes are non-breaking. No content was altered. Verify with diff before commit.

## New file: `favicon.svg`
- Extracted inline `data:` URI SVG to standalone file
- Enables browser caching across page navigations
- Both HTML pages now reference `/favicon.svg` instead of the data URI

## `index.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Added `<link rel="manifest" href="/site.webmanifest">` | Manifest existed but was unreferenced |
| 2 | Added `<link rel="sitemap" type="application/xml" href="/sitemap.xml">` | Aids crawler discovery |
| 3 | Changed `<link rel="icon">` from `data:` URI to `/favicon.svg` | Cacheable across navigations |
| 4 | Removed `:hover` styles from `.domain` and `.tag` | Non-interactive elements should not signal interactivity |
| 5 | Linked org names (IEEE, IEEE SMC, IEEE CIS, OCG) to their URLs | Already in JSON-LD but invisible to users |
| 6 | Rewrote "Current Focus" paragraph | Differentiate from "About" — now references specific regulation set and boundary contracts |
| 7 | Added `2026` fallback text inside `<span id="y">` | Renders correctly if JS is blocked |

## `enforceable-boundary-contracts.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Added `<meta name="google-site-verification">` | Present on index, missing here |
| 2 | Added `<meta property="article:modified_time">` | Required for crawlers to detect freshness on revision |
| 3 | Added `<link rel="manifest">` | Consistency with index |
| 4 | Added `<link rel="sitemap">` | Consistency with index |
| 5 | Changed `<link rel="icon">` to `/favicon.svg` | Consistency with index |
| 6 | Added `aria-current="page"` to breadcrumb current item | Accessibility: screen readers identify current page |
| 7 | Added `BreadcrumbList` JSON-LD block | Structured data for rich search results |
| 8 | Added `dateModified` to Article JSON-LD | Matches new `article:modified_time` meta |
| 9 | Added `2026` fallback text inside `<span id="y">` | JS-off resilience |

## `sitemap.xml`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Index priority `0.8` → `1.0` | Landing page is canonical entry point |
| 2 | Article priority `0.9` → `0.8` | Subordinate to index |

## `site.webmanifest`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Removed `maskable` from 512×512 icon purpose | Portrait photo fails maskable safe-zone crop |

## NOT changed (deferred / optional)

- **Shared CSS file**: Both pages duplicate ~4 KB of identical CSS. Extract to `style.css` when adding a third page.
- **`_headers` / cache control**: GitHub Pages defaults are adequate. Revisit if migrating to Cloudflare Pages.
- **`security.txt` expiry**: Expires 2026-12-31. Calendar reminder to renew.

---

# Site Patch Changelog — 2026-03-24

## New directory: `fonts/`

Self-hosted WOFF2 font files replacing Google Fonts dependency.

| File | Weight | Purpose |
|------|--------|---------|
| `outfit-latin-{300,400,500,600}-normal.woff2` | 300–600 | Body text (latin) |
| `outfit-latin-ext-{300,400,500,600}-normal.woff2` | 300–600 | Body text (extended latin) |
| `dm-mono-latin-{400,500}-normal.woff2` | 400–500 | Monospace (latin) |
| `dm-mono-latin-ext-{400,500}-normal.woff2` | 400–500 | Monospace (extended latin) |

## New file: `fonts/fonts.css`

`@font-face` declarations for all self-hosted font files with correct unicode-range subsetting.

## `index.html`, `enforceable-boundary-contracts.html`, `it-operations-architecture.html`

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Removed `dns-prefetch` and `preconnect` hints for `fonts.googleapis.com` and `fonts.gstatic.com` | No longer needed — fonts are served from the same origin |
| 2 | Removed `<link href="https://fonts.googleapis.com/css2?…" rel="stylesheet">` | Replaced by self-hosted fonts |
| 3 | Added `<link rel="preload">` for `outfit-latin-400-normal.woff2` and `outfit-latin-300-normal.woff2` | Hint browser to fetch most-used weights early, improving First Contentful Paint |
| 4 | Added `<link rel="stylesheet" href="/fonts/fonts.css">` | Loads self-hosted font declarations |

## `README.md`

Added site link, page index table, and tech notes for GitHub repository visitors.
