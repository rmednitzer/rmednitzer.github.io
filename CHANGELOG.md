# Site Patch Changelog -- 2026-09-10 (batch 48: Open source cards checked against their repositories)

The three Open source cards were read against the README, LICENSE,
tiered-authority ADR, and policy module of the repositories they
describe. The facts held; the wording did not, in five places.

relay-shell: "work a real shell and SSH over hosts" did not parse, and
now reads "a real shell, on the local host and over SSH on the hosts I
administer". "Authority is tiered (open, guarded, and read-only modes
over a global deny-list)" conflated the per-call tier classification
with the policy mode; the card now states the three mechanisms in the
order the code applies them: tier classification, policy mode, deny-list
checked first in every mode. "Every call is recorded as a SHA-256 hash
rather than a raw body" hashed the wrong thing; the call is logged and
its output is what is stored as a hash. The closing analogy about a new
colleague is replaced by a plain statement of the design goal.

infra: the module list now names two modules in parallel form instead
of a product and a module.

automation: "hardening baseline covering ... kernel and systemd
hardening" said hardening twice and is now a flat list of what the
baseline covers. Out-of-band management is labelled as proposed, which
is how the repository itself labels it (no BMC hardware in the fleet).

Copy only; no markup, style, structured data, or CSP hash changed. The
local gate passes.

# Site Patch Changelog -- 2026-09-10 (batch 47: validation pass against WCAG 2.2 and the Google profile-page schema)

A validation pass over `index.html` with html-validate (recommended, a11y,
and document presets), axe-core 4.10 at 1280px and 360px in both colour
schemes, Lighthouse 12 (desktop 100/100/100 for performance,
accessibility, and best practices), and hand measurement of the sticky
navigation. Four changes come out of it.

The section navigation is pinned only from the page's 640px breakpoint
upward. Below that width the five entries wrap to two rows (three at
320px), and a pinned bar of that height covered the heading a nav link
had just jumped to: at 320px the heading landed at 88px while the bar
ended at 113px. Narrower than 640px the bar now stays in flow. The scroll
offset moves from `scroll-margin-top` on each section to
`scroll-padding-top` on the root inside the same media query, which is
the WCAG 2.2 SC 2.4.11 (Focus Not Obscured) technique C43 and also
applies when a keyboard-focused link is scrolled into view, not only to
fragment navigation. Measured after the change: headings sit 36px below
the bar at 640px and 1280px, and directly at the section padding on
phones.

The portrait loses its hover ring. It is not interactive, and the
convention since 2026-03 is that non-interactive elements do not signal
interactivity (the same reason `.tag` lost its hover).

The Person entry in the JSON-LD gains `alternateName` ("rmednitzer", the
handle that the `sameAs` profiles use, which the Google profile-page
guidance recommends) and `worksFor` (Cubicure GmbH, which the hero
already states). Nothing in the structured data is new information.

In `style.css`, the breadcrumb link on `legal.html` gains the same
hairline underline as in-paragraph links. axe flagged it as
distinguishable by colour alone (WCAG 1.4.1); it is the one violation
either page produced.

Not changed, with the reasons: Lighthouse's "robots.txt is not valid" is
its in-page fetch being blocked by the meta CSP (no `connect-src`); the
file itself answers 200 locally and on GitHub Pages. Cache lifetime
(`max-age=600`) and compression are set by GitHub Pages, not by the repo.
The 400px Open Graph portrait is below the 1200px that large link
previews prefer; generating a wider card is a separate asset change.
Inline-style CSP hash recomputed; the local gate passes.

# Site Patch Changelog -- 2026-09-10 (batch 46: a teaser, not a dossier)

Batch 45 leaned too far into biography. The page is meant to be a teaser
for someone who finds it and an accurate portrait for search engines,
not enough material to profile a person. About is back to three short
paragraphs: who and where, what I am curious about, and one sentence of
life away from the keyboard followed by the memberships. Sports, the
character sentence, and the Salzburg origin are gone from About, the
hero, and the `Interests` row. The Person JSON-LD gains "Systems
Engineering", "Cybernetics", and "AI Assurance" in `knowsAbout` so the
machine-readable portrait carries the interests the prose no longer
spells out. No markup, style, or CSP hash changed. The local gate passes.

# Site Patch Changelog -- 2026-09-10 (batch 45: plainer, and a person)

The copy had accumulated aphorisms ("the place where I think", "practise
what I preach", "rent it and hope", "which teaches you to write things
down"). This batch strips them and writes plainly. About gains a paragraph
about life away from the keyboard: swimming and freediving, industrial and
EBM, building hardware, 3D printing, radio reception and environmental
sensors, hard science fiction and space. The hero tagline and the
`Interests` row say the same in fewer words. Experience, Open source, and
The lab lose their flourishes and keep their facts. Nothing private was
added: no age, no politics, no employers considered, no pay, no host
names, no relationships. No markup, style, or CSP hash changed. The local
gate passes.

# Site Patch Changelog -- 2026-09-10 (batch 44: breadth before biography)

The second About paragraph made the apprenticeship the origin of
everything and reduced the owner to it. It now leads with self-taught
breadth across disciplines, from hardware and operating systems through
systems theory and control to the rules that govern machines and the
trustworthiness of models and agents, with production described as the
source of a temperament rather than of the knowledge. The apprenticeship
stays on the Experience timeline as a dated fact and is no longer
mentioned in About. The membership paragraph is reordered so the
societies come first and the reading follows. No fact, date, membership,
or technology changed; no markup, style, or CSP hash changed. The local
gate passes.

# Site Patch Changelog -- 2026-09-10 (batch 43: About is about a person)

The About section opened with a job title and a list of employers, which
is what the Experience section is for. It now reads as a description of a
person: what I enjoy, how I learned, what I care about, and what I do for
fun, with the working history left to the timeline below. The Cubicure
entry drops "The newest chapter, and my first in an industrial company."
No fact, date, membership, or technology changed; no markup, style, or
CSP hash changed. The local gate passes.

# Site Patch Changelog -- 2026-09-10 (batch 42: a personal page, not a CV)

Batch 41 tightened the copy into the register of a corporate CV: "focused
on dependable infrastructure for the systems the company relies on",
"Owned backup and recovery, including documented restore evidence",
"Core technologies and operating disciplines". This batch puts the
first-person voice of batch 39 back and keeps the batch 41 structure.
Every date, title, organisation, technology, and membership is unchanged.

- **Hero.** The tagline says what I do and why the lab exists, and that
  the backups were restored, not only configured. The `Focus` row is now
  `Interests`, in plain words rather than positioning phrases.
- **About.** Four paragraphs in my own voice: where the ten years went
  and why the whole stack; how I learned the trade and where the habits
  come from; sovereignty, the EU rules that land on platforms, and the
  systems that draw me; and what the two IEEE societies say about what I
  read.
- **Experience.** The lede and every entry are written as a story told by
  the person who was there, not as a responsibilities list. The Cubicure
  entry no longer carries a mission-statement sentence.
- **Capabilities.** The lede says what the list is: the tools I reach for
  without thinking.
- **Social cards.** The Open Graph and Twitter descriptions describe a
  personal site rather than a service offering.

html-validate, the data-file checks, the CSP hashes, the contrast budget,
and the internal-link check all pass.

# Site Patch Changelog -- 2026-09-10 (batch 41: clearer profile structure and copy)

The profile now leads with a concise statement of scope, replaces the broad
interest list with four professional focus areas, and tightens the About and
Experience copy around verifiable responsibilities and operating principles.
The former Stack section is now Capabilities and appears before Open source, so
the page moves from background and experience to capabilities, evidence in
public repositories, and the home lab. Search, social, structured-data,
manifest, and README descriptions use the same positioning. No claims,
technologies, dates, roles, or organisations were added.

# Site Patch Changelog -- 2026-09-10 (batch 40: the current position, without a start date)

The Cubicure entry said "I start in October 2026", which is true for a
few weeks and then wrong for years. It now reads as the current position:
"Since 2026" in the date column, one sentence on what the company makes
and what the job is, no start date. The hero's `Now` row says the same:
IT Systems Engineer at Cubicure, a Vienna maker of industrial 3D printers.
No markup or style changed; the CSP hashes are untouched.

# Site Patch Changelog -- 2026-09-10 (batch 39: a voice)

The copy was accurate and read like a spec sheet. This batch rewrites it
in the first person, with the reasons behind the facts and the interests
the CV states, without adding a claim the CV or the repositories do not
support. No markup structure, style, or token changed; the CSP hashes are
untouched.

- **Hero.** The tagline says why the lab exists ("because I like knowing
  how things actually work") and that the backups were restored, not just
  configured. The `Now` row names what Cubicure makes; the `Into` row adds
  "reading the news through my own pipeline".
- **About.** Four paragraphs instead of three: where the ten years were
  spent and why the whole stack rather than one layer; how the trade was
  learned and where the habits come from; the EU rules and sovereignty,
  and why defence, robotics, space, scientific, medical, and industrial
  systems draw the owner (the machine at the end of the network is real);
  and the two IEEE societies, with what membership since 2013 says about
  what the owner reads.
- **Experience.** Each entry gained a sentence of context: what the
  company does, what the role taught, why it mattered. Titles, dates, and
  organisations are unchanged from batch 38.
- **Open source.** The lede says why the code is public ("the habits are
  the point"); relay-shell says what it was for; automation says what the
  control mapping buys.
- **Stack.** The lede explains the highlighted tags.
- **The lab.** Same facts, told as a story: what it started as and what it
  became, what the pipeline is for, and the habits it practises, ending on
  the fact that it gets broken regularly.

html-validate, the data-file checks, the CSP hashes, the contrast budget,
and the internal-link check all pass.

# Site Patch Changelog -- 2026-09-10 (batch 38: one title per position)

The Experience timeline now carries one short title per entry and no
seniority. "IT Systems Administrator, infrastructure and platform
operations" is "IT Systems Administrator"; "IT Systems Engineer, senior
level" is "IT Systems Engineer"; "IT Technician, then IT Systems
Administrator" is resolved by splitting it the way the CV's education line
does: the apprenticeship is one entry, "IT Technician" at Ledl.net GmbH and
medPhoton GmbH, 2012 to 2016, with the completion year and both halves of
the training in its body; the medPhoton position is "IT Systems
Administrator", 2016 to 2017. "IT Technician, apprenticeship" lost its
qualifier for the same reason.

The lede and the EBCONT entry no longer mention junior or senior. The
apprenticeship note under the timeline is folded into the apprenticeship
entry, and the `.track-note` rules that placed it are gone; the inline
style hash in the meta CSP was recomputed. html-validate, the data-file
checks, the CSP hashes, the contrast budget, and the internal-link check
all pass.

# Site Patch Changelog -- 2026-09-10 (batch 37: a personal site, not a candidate profile)

The owner's direction: the page read like a job application. Three things
were no longer true or never sat right, and the fleet section showed a
network diagram where a person should be.

## Removed

- The `certified` row (ISO/IEC 27001 ISMS Manager and Auditor, 2017, not
  recertified) is gone from the hero and from JSON-LD `hasCredential`. A
  lapsed certificate is not a headline. ISO 27001 and ISMS/BCM stay in the
  Governance stack row, which is what they are: things worked with.
- The availability notice (`seeking` / `available`). The owner starts as
  IT Systems Engineer at Cubicure GmbH, Vienna, in October 2026. That is
  now the `Now` row in the hero and the top entry on the timeline; the
  Kwizda entry closes at 2026.
- "Mostly self-taught". The apprenticeship is on the same page. The About
  text says what was meant: the trade was learned by doing it.
- The fleet section: topology diagram, four role cards, principles row,
  and the `.topo-*` and `.fleet-principles` rules that drew them.

## Rewritten

- **Hero.** The tagline is first person and says what the owner does and
  why the lab exists. Four facts remain: `Now`, `Into` (sovereign systems;
  defence, robotics, and space; scientific, medical, and industrial
  installations; EU platform regulation), `Member of` (with the two IEEE
  societies named), `Languages`.
- **About.** Three first-person paragraphs: the work and where it was
  done; how the trade was learned and why open source and self-hosting;
  what matters beyond the job. Every claim traces to the CV.
- **Experience.** Same timeline, entries trimmed to what a reader of a
  personal site needs, Cubicure on top.
- **Stack** (was Skills): six rows instead of eight. The homelab row is
  gone; the lab has its own section.
- **The lab** replaces the fleet: three paragraphs on what it is, what it
  is for (reading the news through an OSINT pipeline: some 130 feeds,
  220,000+ documents, 38,000+ CVEs, hybrid retrieval, local models, a
  morning briefing), and the habits it practises (the gate and audit log,
  the hardening baseline, tested restores, self-hosted Git), with a
  `Built with` tag row beneath.

## Metadata

The description, Open Graph, Twitter, JSON-LD, manifest, README, and the
`CLAUDE.md` topic line now describe a person with a lab rather than a
candidate. The section nav reads About, Experience, Open source, Stack,
Lab. The inline style hash in the meta CSP was recomputed. html-validate,
the data-file checks, the CSP hashes, the contrast budget, and the
internal-link check all pass; dark and light renders at 1280px and 400px
were inspected.

# Site Patch Changelog -- 2026-09-10 (batch 36: typography, hierarchy, and layout)

A design pass on the profile page. The palette, the two fonts, and every
token are unchanged; what changed is how the type is used, how the page is
divided, and what a reader sees first. No new colour or font literal, no
inline `style=`, no page-specific stylesheet.

## Two voices instead of one

DM Mono had been carrying headings, card titles, dates, tags, and labels
alike, so nothing on the page outranked anything else. It now speaks only
for metadata: dates, organisations, tags, labels, the nav, the footer, and
repository names (which are identifiers). Everything a reader is meant to
read as prose or as a heading is Outfit: the name at up to 2.6rem, the
role beneath it at 500 weight in the accent colour, section titles at
around 1.5rem, card and position titles at 1.08rem and 600 weight. Body
copy moved from 1rem to 1.0625rem on a 1.6 line-height, card copy from
.85rem to .95rem, and measures are capped at 66 to 70ch (76ch for the lead
repository card). Mono numerals are tabular, so dates and counts line up.

## Hero

The role is a line of its own rather than a fragment after the city. The
eight-row key/value strip is split: `seeking` and `available` sit in an
accent-bordered notice directly under the contact buttons, which is the
one thing a recruiter should not have to hunt for, and the remaining six
facts lay out two pairs per row from 720px so the strip is three rows deep
instead of eight. The portrait grew to 132px to match the larger name.

## Section navigation and numbered sections

A section nav (About, Experience, Open source, Skills, Fleet) sits under
the hero and pins to the top of the viewport as the page scrolls; every
section gained an `id` and a scroll margin so the pinned bar never covers
its heading. The outer section cards are gone. Sections are now separated
by whitespace and a numbered heading (`01` to `05`, a CSS counter with the
same silent alt-text form as the old `//` prefix) that runs a hairline out
to the column edge; the inner cards (`.spec`, the topology tiers) carry the
surface colour instead, so the page has one level of boxes rather than two.

## Experience as a timeline

The four stacked cards became a timeline: date in a right-aligned mono
column, a vertical rule with an accent dot per position, title, employer
and body on the right. On narrow screens the date sits above the entry and
the rule stays. The apprenticeship note aligns with the body column.

## Capitalisation

Visible text is sentence case throughout, brand names excepted: the fact
values ("Around ten years", "Open source by default"), the metadata tags
("Cloud VM", "Always-on server", "Since 2025"), the topology labels and
gate steps ("Plan", "Authorize", "Execute"), and the principles tags
("Credential and network separation"). Skill-row labels use an ampersand
consistently ("Containers & GitOps", "Automation & IaC", "Homelab &
learning") instead of a slash. Date ranges use an en dash.

## Shared stylesheet

`style.css`: body type size and line-height as above; `.tag` gained a
line-height, tabular numerals, and slightly more padding; the footer sits
lower with a touch more tracking. `legal.html` picks up the body size and
nothing else.

## Housekeeping

The inline style hash in the meta CSP was recomputed. html-validate, the
data-file checks, the CSP hashes, the contrast budget (40 token pairs
across 5 palettes), and the internal-link check all pass; the page was
rendered in dark and light at 1280px and 400px to check the result.

# Site Patch Changelog -- 2026-09-10 (batch 35: say no more than the CV does)

An accuracy pass against the CV and against live sources, plus the house
style the last batch had let slip. No redesign, no new tokens.

## Claims trimmed to what the CV states

- The About text said "I have implemented the ISO 27001 ISMS that has to
  satisfy the auditor". The CV says ISMS and BCM practice including
  preparation for ISO 27001 audits. The sentence now says that. The
  manifest description and the `CLAUDE.md` topic line carried the same
  "ISMS implementation" claim and were corrected with it.
- The `certified` row now records that the ISO/IEC 27001 ISMS Manager and
  Auditor certificate (TÜV Austria, 2017) has not been recertified, as the
  CV does.
- The Experience lede said "from apprentice to senior engineer" at one
  provider. The apprenticeship was elsewhere; EBCONT was junior to senior,
  and the lede now says so. "Ten years" became "around ten years", the
  CV's own qualifier, in the hero strip and the lede.
- The Kwizda card carries the CV's title in full (infrastructure and
  platform operations) and its Kubernetes and GitOps line as a
  contribution, not an ownership claim.
- JSON-LD `knowsAbout` lost "SUSE Linux Enterprise Server" and "Edge AI":
  neither appears in the CV or the fleet.

## Repository cards checked against their READMEs

`infra` no longer "builds the fleet": its README describes modules for
cloud-init Ubuntu VMs and a Talos cluster, a production environment whose
remote backend is configured but holds no deployed resources, and a CI gate
of format, lint, Trivy, gitleaks, and mock-provider module tests. The card
now says that. `automation` says "Controls map to" rather than "Every
control maps to". `relay-shell` matched its README and is unchanged in
substance.

## Fleet numbers refreshed from the data plane

Read live on 2026-09-10: 221,573 documents with 221,573 embeddings,
38,195 CVEs, 130 enabled feed sources of 138 configured. The Data &
inference card now says over 220,000 documents, some 38,000 CVEs, and some
130 sources (it said "more than 130", which the enabled count does not
support).

## House style and accessibility

Batches 9 and 22 established that the copy carries no em-dashes; batch 34
reintroduced eight. All are gone again, replaced by colons, commas, and
parentheticals. Date ranges on the Experience cards use an en dash, and the
current position reads "since 2025". The arrow in "IT Technician →
IT Systems Administrator" is now the word "then", the "plan → authorize →
execute" phrase in the control-plane card is written out, and the arrow
separators in the topology diagram use the `content: '→' / ''` alt-text
form so screen readers skip them, matching the `//` heading prefix.

## Housekeeping

`dateModified` and the sitemap `lastmod` moved to 2026-09-10; the inline
style hash in the meta CSP was recomputed. html-validate, the data-file
checks, the CSP hashes, the contrast budget (40 token pairs across 5
palettes), and the internal-link check all pass.

# Site Patch Changelog -- 2026-08-14 (batch 34: the site follows the CV)

The CV is the primary document; the site had drifted from it. This batch pulls
the page back onto that base, in English, without redesigning anything.

## Positioning

The title is now **Systems & Platform Engineer**, the headline the CV itself
carries, replacing "Senior Linux & Platform Engineer" across `<title>`, the
description, Open Graph and Twitter cards, the manifest, the JSON-LD
`jobTitle`, and the README. The tagline says what the CV says: broad rather
than specialised, hardware and storage through to observability and verified
recovery.

Two rows were added to the hero strip, because a profile that is looking for a
role should say so: `seeking` (senior systems integration, platform and
infrastructure operations, or systems architecture) and `available` (from
October 2026, Vienna and surroundings, on-site or remote, security clearance
possible). `certified` records the ISO/IEC 27001 ISMS Manager and Auditor
certificate (TÜV Austria, 2017), which the site had only ever implied.

## Experience

New section between About and Open source: four positions, newest first, on
the same `.spec` cards the rest of the page already uses -- Kwizda Holding
(2025 -- now), EBCONT operations (2017 -- 2025), medPhoton (2015 -- 2017),
Ledl.net (2012 -- 2014), with the estate sizes, the scope, and the apprenticeship
line the CV states. Two new rules carry it (`.track`, `.spec .track-org`); the
cards, hairlines, and hover treatment are the existing ones.

Employer names and years only. No address, no phone, no day-level dates --
the repository rule still holds.

## Skills and the fleet

The tag rows were re-cut against the CV's technology inventory: **Storage &
Data** and **Network & Cloud** are new rows, hardening and governance moved
into **Security & Governance**, and the core inventory items the page was
missing are now on it (Debian, Windows Server, Ceph, NetApp, enterprise SAN,
Podman, AAP, Graylog, OpenSearch, Cilium, HAProxy, Azure, Google Cloud,
Hetzner, CIS hardening, CRA).

The fleet cards took the CV's numbers, which are more current than the ones on
the page: ~30 workloads reconciled by Flux, 170,000+ documents with full
embedding coverage, ~25,000 CVEs enriched with KEV and EPSS, hybrid retrieval
with reranking. The Ansible baseline is described as CIS-benchmark-based,
which it is.

## Housekeeping

JSON-LD gained `hasCredential` and the `knowsAbout` entries matching the new
tags; `dateModified` and the sitemap `lastmod` moved to 2026-08-14; the inline
style hash in the meta CSP was recomputed. html-validate, the data-file checks,
the CSP hashes, the contrast budget, and the internal-link check all pass.

# Site Patch Changelog -- 2026-08-13 (batch 33: font licence files, and the repo's missing paperwork)

## The one that actually mattered: OFL compliance

The site self-hosts Outfit and DM Mono as WOFF2 in `fonts/`, deliberately,
so no visitor request ever reaches a font CDN. Self-hosting also makes this
repository a *redistributor* of both families, and SIL Open Font License 1.1
clause 2 permits redistribution only "provided that each copy contains the
above copyright notice and this license".

Eleven `.woff2` files were being redistributed with neither. That is a licence
condition, not a nicety.

Added, verbatim from upstream:

- `fonts/OFL-Outfit.txt`  -- Copyright 2021 The Outfit Project Authors
- `fonts/OFL-DMMono.txt`  -- Copyright 2020 The DM Mono Project Authors

Both licence bodies are the standard OFL 1.1 text and differ only in the
`scripts.sil.org` URL scheme, but each ships whole so that each family's own
copyright line travels with its own licence. Neither family declares a Reserved
Font Name, so clause 3 imposes no naming restriction here.

`fonts/README.md` now records what is in the directory, why the licence files
are there, and the rule for adding a family. `CLAUDE.md` and
`.github/copilot-instructions.md` carry the same rule, so the next weight added
does not quietly reintroduce the gap.

## Repository paperwork

`NOTICE` now states the split the LICENSE file alone left to inference: the
markup, stylesheet, and CI scripts are Apache-2.0, while the prose, biography,
portraits, and site marks are personal content and rights reserved. Anyone who
wants the layout can take the code and bring their own content, and now the
repository says so plainly.

`CONTRIBUTING.md` sets expectations honestly for a personal site: bug reports
and accessibility findings are very welcome, content rewrites and redesigns are
not, and the no-build-step and no-CDN rules are standing constraints rather than
things nobody got around to. It also documents the four-command local gate.

Also added: `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1, reporting via
private advisory), `.github/CODEOWNERS`, a pull request template that mirrors
the CI gate, and issue forms for bugs and accessibility. The accessibility form
is separate on purpose: contrast is already machine-checked, so the reports
worth soliciting are the ones a script cannot produce.

No HTML, CSS, or inline script changed. The CSP hashes are untouched.
html-validate, the CSP hashes, the contrast budget (40 token pairs across 5
palettes), and the internal-link check all pass.

# Site Patch Changelog -- 2026-08-05 (batch 32: the More at note is just the link)

The note now reads "More at github.com/rmednitzer" and nothing else.

The teaser list -- "an AIOps MCP, a self-hosted AI stack as one Helm
chart, a knowledge platform on PostgreSQL" -- described three
repositories the page had already decided not to feature. Three cards
above it make the case in detail; a partial second list underneath
competes with them for attention and adds nothing a reader cannot get
by following the link, which is what the note is for.

This also finishes what batches 29 and 30 started. The note has been
edited three times running: batch 28 re-picked which repositories it
named, batch 29 cut their descriptions down, batch 30 removed the
"earlier-stage" ranking. Each pass kept the list and trimmed it. The
list itself was the thing that did not belong.

No CSS changed, so the CSP style hash is untouched. html-validate, the
CSP hashes, the contrast budget, and the internal-link check all pass.

# Site Patch Changelog -- 2026-08-05 (batch 31: draw the fleet topology)

The fleet section opens by calling itself "a strict control-plane /
data-plane split" and then describes that split in four prose cards. The
split is the organizing idea of the whole section and it was the one
thing the section never showed. This batch draws it.

**A topology figure above the cards.** Two tiers, each a bordered box
with a hairline label matching the section headings. The control plane
holds the MCP gateway as the single entry point -- accent-bordered,
because it is the only way in -- with `plan -> authorize -> execute` as
three `.tag` pills joined by accent arrows. A short run connects the
tiers, labelled "every mutation, hash-chained". The data plane holds the
three host roles. The figure is a map; the four cards below remain the
detail, and the node names match the card names so the two read
together.

**Drawn in HTML, not SVG.** This was the load-bearing decision. SVG text
scales with the viewBox rather than reflowing, so a diagram laid out for
this 820px column renders its labels at roughly 5px on a 320px phone --
the width range is 2.4x and there is no `preserveAspectRatio` trick that
keeps type legible at both ends. HTML boxes reflow instead: the three
data-plane nodes are a 3-up grid above 640px and stack below it, the
gate pills wrap, and every label stays real selectable text at its real
size, honouring user font settings and scaling with them. It also means
no new colour or font literals -- the figure is built entirely from
existing tokens, so both palettes, both `prefers-contrast: more`
variants, and print all follow for free.

Verified at 320, 360, 560, 640, and 900px: no horizontal overflow at any
width, in either theme.

**Reused rather than reinvented.** The gate steps are the shared `.tag`
pill. The tier labels use the same `flex` + hairline `::after` as
`.section h2`. Node hover matches `.spec:hover`. The only genuinely new
shapes are the connector rule and its CSS chevron.

The inline `<style>` block changed, so the CSP style hash was
regenerated. html-validate, the CSP hashes, the contrast budget, and the
internal-link check all pass.

Deliberately not done: the figure restates parts of the `Control plane`
card (the gate sequence, the hash-chained audit). Map-then-detail makes
that repetition defensible and the card carries specifics the figure
does not -- the single-use confirmation digest, the typed interface, no
provider credential in the network-facing process. Worth revisiting as
an editorial question, not folded into a batch that was asked to add a
diagram.

# Site Patch Changelog -- 2026-08-05 (batch 30: remove the portfolio commentary from the Open source section)

Batch 29 fixed a proportion problem by adding maturity commentary. That
was the wrong instrument. Ranking your own repositories in the copy is
something a reader does not need and a professional profile should not
do: it talks *about* the portfolio instead of presenting the work, and it
tells the reader how to read the page. Four passages went, all of the
same kind.

**The self-ranking.** The `relay-shell` card's second paragraph -- "The
furthest along of my repositories, and the one to read first: released,
documented, and carrying the most CI" -- is gone. So is the `most
developed` fragment appended to its tag, which had broken the tag
pattern: every other tag slot on the page carries licence and
technology, not a self-assessment.

The card keeps its primacy without claiming it. It still leads at full
width above the grid, and position plus width is the whole signal --
that is what the layout is for. The freed sentence went back into
substance: interactive PTY sessions, which the card had omitted and
which are a real part of the tool surface.

**The disclaimers.** The `automation` card's "Pre-1.0: the gaps that
remain are written down in the repository rather than left implied" and
the note's "Most of it is earlier-stage than the three above" are gone
for the same reason, inverted -- pre-emptive self-deprecation is still
commentary about the portfolio, and on a professional profile it reads
as anxious rather than candid. Anyone assessing the repositories will
open them; the repositories are honest about their own state, which is
where that belongs.

`automation` got its substance back instead: the roles it actually ships
(SSH, auditd, firewalling, kernel and systemd hardening) and the three
playbooks batch 29 had cut (SRE toolchain, local inference, out-of-band
management), all verified against the repository.

The principle the section now follows: **primacy through position,
honesty through specificity.** Say precisely what each thing is and let
the ordering carry the ranking. Maturity claims and maturity disclaimers
are both commentary, and neither belongs in the copy.

`legal.html` was reviewed in the same pass and left unchanged -- it is
standard Impressum, DSGVO, and MedienG boilerplate, and the editorial
direction it declares still matches the site.

No CSS changed, so the CSP style hash is untouched. html-validate, the
CSP hashes, the contrast budget, and the internal-link check all pass.

# Site Patch Changelog -- 2026-08-05 (batch 29: rank the repos honestly, shorten the Open source section)

A proportion pass over the Open source section, plus two small honesty
edits elsewhere. Nothing on the page was false -- batch 26 verified every
claim and batch 28 re-checked the three featured cards -- but the section
presented three repositories as peers when they are not, and spent its
length on CI tool inventories rather than on what each repository is.

**`relay-shell` leads.** It is the furthest along by every available
signal: a tagged release and a `release.yml`, nine CI workflows
(CodeQL, dependency-review, pip-audit, gitleaks, SBOM, nightly fuzzing),
a published docs site, and an `audit/` directory. `infra` has one CI
workflow plus a Renovate validator and no release pipeline; `automation`
has two, and its own `LIMITATIONS.md` records "L7 -- Pre-1.0, no release
tags". Presenting all three at equal weight understated the first and
overstated the other two.

So `relay-shell` now sits above the grid as a full-width lead card,
tagged `most developed`, with a second short paragraph saying plainly
that it is the one to read first. `infra` and `automation` follow as a
2-up row. Keeping the lead card *outside* `.matrix` leaves the grid an
even two cards, so nothing takes the `:last-child:nth-child(odd)`
full-width branch -- the alternative, a third card in the grid, would
have promoted whichever repo landed last instead of the one that earned
it. The only new CSS is `.spec--lead { margin-top: 1rem; }`.

**Shorter, and about the repositories rather than their CI.** The card
bodies drop the tool inventories -- "fmt, validate, TFLint, Trivy,
gitleaks, and module tests", "ansible-lint and schema checks" -- which
listed the same class of thing three times and told a reader nothing
about the systems. `infra` and `automation` are two sentences each now.
`automation` gained the one fact that matters for calibration: it is
pre-1.0, and its gaps are written down rather than left implied. The
"More at" note loses its per-repository descriptions and gains the same
calibration: most of the rest is earlier-stage than the featured three.
The section lede flips order to match the new card order.

**Two edits outside the section.** The About paragraph loses "The range
is the point", which announced the reader's conclusion instead of
letting the sentence make it. The fleet lede's "run the way I run
production" claimed an equivalence a personal fleet does not have --
now "run with the habits I bring to production", which is the true
claim and the more useful one.

The inline `<style>` block changed, so the CSP style hash was
regenerated. html-validate, the CSP hashes, the contrast budget, and the
internal-link check all pass.

# Site Patch Changelog -- 2026-08-05 (batch 28: trim the fleet section, re-pick the featured repos)

A subtractive pass. Batch 26 refreshed every factual claim against the
live fleet, and in doing so pushed the fleet section into territory that
is more inventory than engineering. This batch pulls it back and fixes
one link that oversold what it points at.

**The fleet section no longer describes a house.** The `Edge & mesh`
card is gone entirely: it enumerated the personal devices on the
operator side -- an SDR desktop, a roaming laptop, a Windows management
surface -- and placed the subnet router and exit node "at home". On a
page that already carries a full name, a portrait, and Vienna, that
combination is a physical inventory, and it demonstrated nothing the
architecture cards do not. The mesh survives as one word in the lede,
which is all it needed.

For the same reason the `Data & inference` card drops its spec sheet
(Core i9, 128 GB ECC, RTX 4500 Ada) for "a single workstation-class
host", and the storage card drops the NAS as a named box -- encrypted
Restic backups going off-host is the control; where they land is not a
credential. The software-scale claims stay: 130+ OSINT sources, the
four-hour cycle, six analysis agents, PostgreSQL 18. Those describe a
system, not a room.

The lede also loses the host count, which invited the inventory reading,
and "I designed and run myself", which restated the "self-run" three
clauses earlier.

Net effect on layout: five cards become four, so the fleet grid is now
an even 2x2 and no card takes the full-width `:last-child:nth-child(odd)`
branch. `relay-shell` remains the only full-width card on the page.

**Featured repos re-picked against what the repos actually are.** The
"More at" note advertised "a code-managed ISO 27001 ISMS", linking work
that its own README marks as a *Skeleton* with content population
incomplete. ISO 27001 is the strongest governance credential on this
page; pointing it at an empty framework was the one link that could cost
more than it earned. Dropped.

Also dropped: the governed agentic runtime (`agents`), which retold the
story the featured `relay-shell` card already tells in more detail.

The note now names three, chosen for maturity and for covering three
different kinds of system rather than three versions of one:

- `aiops-mcp` -- bitemporal fleet state, drift detection, and a tiered
  actuator that gates changes behind approval. Nine invariants proven in
  CI, STPA analysis, AI Act/NIS2/CRA mapping.
- `ai-stack` -- 15+ components as one Helm chart, with SBOM validation,
  CVE scanning, and conformance testing in CI.
- `core-graph` -- eight ontology layers on PostgreSQL with Apache AGE
  and pgvector, MCP/REST/TAXII interfaces.

Not featured but worth knowing about, if the note is ever revisited:
`mission-assurance` (governance-as-code, operational, no draft marker)
is the honest replacement for the `isms` link, and `platform-blueprint`
is a 122-document corpus whose content is still uniformly draft.

**Also.** The Open source lede opened with "Open source by default",
which is verbatim the hero `approach` line eight elements above it.
Reworded to lead with the arc instead.

No CSS changed, so the CSP style hash is untouched. html-validate, the
CSP hashes, the contrast budget, and the internal-link check all pass.

# Site Patch Changelog -- 2026-08-05 (batch 27: contrast fix, layout repairs, CI budgets)

A design and setup pass driven by rendering the page rather than reading
it. Three things were wrong once looked at.

**Contrast.** `--muted` sat at 4.25:1 against `--bg-surface` in dark mode
(4.42:1 against `--bg`), below the WCAG AA small-text floor of 4.5:1, and
it carries most of the page's secondary text: every skill and principle
tag, every section lede, the footer, the hero subtitle, the repo tags.
Light mode passed, which is presumably how it survived review. Dark
`--muted` moves to `#788699` (5.03:1 / 5.22:1) and light `--muted` to
`#666d7a` for margin. A `prefers-contrast: more` palette was added on top,
overriding the same tokens so every existing rule follows without change.

**Measure.** `.spec p` had `max-width: none`, which is invisible in the
two-column cards but let the full-width ones (`relay-shell`, and the new
fleet storage card) run past 100 characters per line. Capped at 74ch,
which only ever binds on a full-width card.

**Skills alignment.** The label column was a fixed 9.5rem, so
"Linux & Virtualization" wrapped to two lines while shorter labels did
not. Widening the fixed value just moved the problem to the tags. Instead
the rows now collapse into one shared grid (`.tag-row { display: contents }`
above 640px), so every label sits in a single `max-content` track: aligned,
one line each, and no magic number to re-tune when a label changes.

Also: section headings gained a hairline that runs out to the card edge,
which gives the five stacked cards some rhythm; cards respond to
`:focus-within` as well as `:hover`, so keyboard users get the same
affordance as mouse users; the hero meta labels went from .66rem to .7rem;
section spacing 1.25rem to 1.5rem; and print gained `break-inside: avoid`
so a card is not split across sheets.

**Setup.** Two dependency-free CI checks in the pattern ADR 0007
established, plus the ADR recording them:

- `check_contrast.py` asserts the 4.5:1 floor for `--fg`, `--fg-strong`,
  `--muted`, and `--accent` against both surfaces, across all five
  palettes, layering media-block overrides the way the cascade does. It
  was verified to fail on the exact palette this batch replaced.
- `check_links.py` resolves internal links, assets, in-page anchors, CSS
  `url()` targets, and every sitemap `<loc>` against the files on disk,
  using Pages' own resolution order so `/legal` is checked as served. It
  also fails any external reference in the stylesheets, making ADR 0003's
  no-third-party-requests rule executable. `--external` runs weekly from a
  separate workflow rather than gating pull requests, because a
  rate-limited host is not a reason to block a merge.

| File | Change |
|------|--------|
| `style.css` | Dark `--muted` `#6b7a8d` to `#788699`, light `#6b7280` to `#666d7a` (WCAG AA); new `prefers-contrast: more` palettes for dark and light; print gains `break-inside`/`break-after` guards |
| `index.html` | `.spec p` max-width `none` to `74ch`; `.taglist` becomes the shared grid with `.tag-row { display: contents }` above 640px; `.section h2` flex layout with trailing hairline rule; `.spec:focus-within` matches `:hover`; hero `dt` .66rem to .7rem; section margin 1.25rem to 1.5rem; inline-style CSP hash recomputed |
| `.github/scripts/check_contrast.py` | New: palette contrast budget |
| `.github/scripts/check_links.py` | New: internal link/asset/anchor/sitemap resolution, plus `--external` mode |
| `.github/workflows/validate.yml` | Two new gating steps: contrast budget, internal links |
| `.github/workflows/links.yml` | New: weekly off-site link-rot check, not gating |
| `.editorconfig` | New: UTF-8, LF, final newline, 2-space (4 for Python) |
| `docs/adr/0010-...md`, `docs/adr/README.md` | ADR 0010 recording both checks and what they deliberately do not cover |
| `CLAUDE.md`, `.github/copilot-instructions.md` | Contrast budget documented; local validation section now lists the full gate |
| `CHANGELOG.md` | This entry |

# Site Patch Changelog -- 2026-08-05 (batch 26: refresh every factual claim against the live fleet and repos)

Accuracy pass over everything the page asserts about the owner, checked
against the live fleet inventory and the current GitHub repositories
rather than against the previous copy. The fleet has grown since the last
update: a Git/services server and a NAS backup target joined it, so the
lede count went from five hosts to eight and a fifth role card was added.
The control plane is no longer the only externally reachable surface now
that a public relay host exists, so that claim was reworded to what is
still true (it is where automated action enters the fleet). The data-plane
card's "sixteen scheduled OSINT and analysis pipelines" was wrong after the
2026-07 migration that moved scheduling to the compute host; it is now
130-plus sources on a four-hour cycle and six scheduled agents. The
observability cluster reconciles with Flux, not generic GitOps. Repo cards
picked up CI surfaces that have since been added (SBOM publishing, nightly
fuzzing, module tests), and the repos-note now names what is actually in
the account instead of "edge-AI experiments". Body-only; inline style and
CSP hashes unchanged, no em-dashes.

| File | Change |
|------|--------|
| `index.html` | Fleet lede five to eight hosts; control-plane card reworded off the "only externally reachable surface" claim; data/inference card corrected to 130-plus OSINT sources, four-hour cycle, six scheduled agents; observability card gains vmalert/Alertmanager and Wazuh agent coverage, "GitOps-reconciled" to "Flux-reconciled"; "Edge & mesh" trimmed to the operator side with a new "Git, services & storage" card (Forgejo, Ansible job automation, notifications, encrypted Restic backups, ZFS/Sanoid); principles gain "encrypted off-host backups"; `infra` card gains module tests, `relay-shell` card gains SBOM and nightly fuzzing; repos-note rewritten to the current portfolio; Skills gain Flux, Restic, pgvector; JSON-LD `knowsAbout` gains Flux, pgvector, Apache AGE, Forgejo, Restic, Cyber Resilience Act, GDPR; `dateModified` to 2026-08-05 |
| `sitemap.xml` | Home `lastmod` to 2026-08-05 |
| `README.md` | Summary reframed to match the site's positioning (works with open-source software, not builds open-source tooling) |
| `CHANGELOG.md` | This entry |

# Site Patch Changelog -- 2026-07-16 (batch 25: hero positioning, work with open source not build tools)

Two positioning fixes to the intro copy. First, dropped the closing
"Mostly self-taught. Open source by default." from the hero tagline: those
two sentences repeated the `approach` meta chip ("open source by default ·
mostly self-taught") two lines below, verbatim, so the hero duplicated
itself. Second, per the owner, reframed the copy away from building tools
and toward working with open-source software: the tagline's "build
open-source tools and platforms for the same problems" and the meta
description's "open-source tooling for the same problems" mis-positioned
him as a tool builder. The fleet line was adjusted from "control plane I
built myself" to "designed and run myself" to credit his architect and
operator role (he works out the specs; the systems stay his) without
implying from-scratch coding. Body-only; inline style and CSP hash
unchanged, no em-dashes.

| File | Change |
|------|--------|
| `index.html` | Hero tagline trimmed and reframed to "working with open-source software throughout"; meta description reframed to "built entirely on open-source software"; fleet lede "control plane I built myself" to "designed and run myself" |
| `CHANGELOG.md` | This entry |

# Site Patch Changelog -- 2026-07-16 (batch 24: sharper About section)

Rewrote the About paragraph. The previous copy restated the hero-meta
`experience` and `focus` lines and re-listed the same stack that the
Skills tags already carry, so it duplicated the page instead of adding to
it. The replacement drops the tool enumeration, leads with the value
(keeping business-critical systems dependable where downtime and audit
findings both cost), and makes the differentiator explicit: running the
infrastructure and implementing the ISO 27001 ISMS together, engineering
and governance built rather than bolted on. Body-only; inline style and
CSP hash unchanged, no em-dashes.

| File | Change |
|------|--------|
| `index.html` | About paragraph rewritten from a stack enumeration to a narrative that does not duplicate the hero-meta or Skills |
| `CHANGELOG.md` | This entry |

# Site Patch Changelog -- 2026-07-16 (batch 23: feature relay-shell over isms)

Swapped the third featured repo in the Open source section from `isms` to
`relay-shell`, giving the three cards a build, harden, operate arc (infra,
automation, relay-shell) that ties into the fleet's governed MCP control
plane. The ISMS work stays discoverable through the GitHub note. Body-only
change; inline style and CSP hash unchanged.

| File | Change |
|------|--------|
| `index.html` | Open source: `isms` card replaced by a `relay-shell` card (governed MCP shell/SSH server; tag `Apache-2.0 · MCP`). Section lede reworded from "a code-managed ISMS for the compliance side" to "the governed control plane that operates it"; repos-note now points to the ISO 27001 ISMS and edge-AI experiments instead of relay-shell |
| `CHANGELOG.md` | This entry |

# Site Patch Changelog -- 2026-07-16 (batch 22: fleet showcase polish + em-dash removal)

Formatting and layout pass on the home page to make the fleet read as a
real showcase, plus a house-style change: no em-dashes anywhere in the
prose. The fleet section gains a one-line topology summary and a scannable
`principles` chip row under the role cards (credential/network separation,
typed gated mutation, localhost-only, hash-chained audit, ZFS snapshots,
reversible by default); every card title is now a real `<h3>`, and cards
lift on hover. Copy across the fleet and open-source sections was tightened
and every em-dash replaced with a colon, comma, or parenthetical. Verified
in Chromium at desktop and mobile widths in both colour schemes.

| File | Change |
|------|--------|
| `index.html` | Section order is now About, Open source, Skills, then The fleet (professional signal first; the homelab fleet closes the page). Fleet section: topology lede plus a `principles` tag row beneath the cards; role/repo card titles promoted to `<h3 class="spec-name">` (repo names wrap an `<a>`); `.spec` gains a hover lift (border + tint). Shared `.skills`/`.skill-row` classes renamed to `.taglist`/`.tag-row` (now used by both principles and skills); `.section-lede` muted-lede helper added. All em-dashes removed from copy and the meta description. Meta CSP `style-src` hash recomputed (`sha256-DOa4...`); year-script hash unchanged. No inline `style=` attributes; no new colour or font tokens |
| `CHANGELOG.md` | This entry |

# Site Patch Changelog -- 2026-07-16 (batch 21: site rework + remove /projects sub-site)

Reworked the single-page site around the homelab fleet and removed the
`/projects` sub-site. The former standalone `projects.html` write-up page
is gone; the home page now leads with a public-safe showcase of the
self-run fleet — a control-plane / data-plane split described by role, not
by hostname (no hostnames, IPs, domains, or provider IDs) — followed by a
trimmed open-source section and the existing skills grid. The old
"Homelab" one-paragraph section is replaced by four role cards (control
plane, data & inference, observability & SIEM, edge & mesh). CI, the
sitemap, and the docs mirrors were updated to drop the retired page.

| File | Change |
|------|--------|
| `projects.html` | Removed. The `/projects` sub-site is retired; its content is not migrated (the deeper per-repo write-ups are dropped in favour of the fleet showcase and the compact home-page cards) |
| `index.html` | New `The fleet` section: intro plus four role cards showcasing the control plane, data & inference plane, Talos observability/SIEM cluster, and edge/mesh nodes, all described by role with no hostnames, IPs, domains, or provider IDs. Former `Open-source projects` section renamed `Open source`, trimmed to three cards, and delinked from the removed `/projects` page (repos-note now points only to GitHub). Inline `<style>` adds `.spec-name` for non-link card titles; the `.matrix` comment generalised from "featured-project cards" to the shared card grid. Meta/OG/Twitter descriptions and the JSON-LD `Person.description` mention the fleet; `knowsAbout` adds PostgreSQL, Tailscale, WireGuard; `dateModified` to 2026-07-16. Meta CSP `style-src` hash recomputed for the new inline style (`sha256-WSg7...`); year-script hash unchanged |
| `sitemap.xml` | `/projects` URL removed; `/` `lastmod` to 2026-07-16 |
| `.github/workflows/validate.yml` | `html-validate` and the JSON-LD parse step no longer include `projects.html` |
| `.github/scripts/check_csp_hashes.py` | `PAGES` no longer includes `projects.html` |
| `.github/copilot-instructions.md`, `CLAUDE.md` | Key-files list and layout map drop the retired `projects.html` |

# Site Patch Changelog -- 2026-06-21 (batch 20: in-depth projects page + card accuracy refresh)

A new `/projects` page gives each featured open-source project a deeper
write-up than the home-page card, grounded in the current state of each
repository. Refreshing the cards against the repos surfaced two factual
drifts in the existing copy, both corrected here and flagged for the owner:
relay-shell has three policy modes plus a global deny-list overlay (not four
modes; deny is not a mode, per relay-shell ADR 0003), and aiops-mcp is no
longer stdio-only (an opt-in HTTP transport shipped, aiops ADR 0041/0042).
The new page reuses the existing `page--article` layout and adds no inline
styles; CI (html-validate, JSON-LD parse, CSP-hash check) now covers it.

| File | Change |
|------|--------|
| `projects.html` | New page at `/projects`: in-depth write-ups of the six featured projects (infra, automation, isms, relay-shell, aiops-mcp, nous), each grounded in its repository, with a jump-link table of contents. Reuses `page--article` / `article-body`; carries a `BreadcrumbList` plus a `CollectionPage` whose `mainEntity` is an `ItemList` of six `SoftwareSourceCode` nodes (each `author`-linked to the existing `#person`). Same meta CSP as `legal.html`; reuses the existing year-script hash, no inline `<style>` block |
| `index.html` | Projects section `repos-note` now links the new `/projects` page; two card corrections from the repo refresh (relay-shell "four authority modes (... and deny)" to "three policy modes (...) plus a global deny-list"; aiops-mcp "v0 is stdio-only" to "v0 defaults to stdio with an opt-in HTTP transport"); JSON-LD `dateModified` to 2026-06-21 |
| `style.css` | Projects-page layout block (`.work-lede`, `.work-toc`, `.work-project`, `.work-meta`) added beside the existing article-layout rules; no new colour or font tokens, no inline styles |
| `sitemap.xml` | `/projects` URL added (priority 0.8, monthly, lastmod 2026-06-21) |
| `.github/workflows/validate.yml` | `html-validate` and the JSON-LD parse step now include `projects.html` |
| `.github/scripts/check_csp_hashes.py` | `PAGES` now includes `projects.html` |
| `.github/copilot-instructions.md`, `CLAUDE.md` | Key-files list and layout map note the new `projects.html` page |

# Site Patch Changelog -- 2026-06-12 (batch 19: backlog close-out B-06, B-07, B-08, B-09)

Owner decisions collected and applied. The audit backlog is now down to
a single item, B-02 (repository-settings verification and the
security.txt renewal), which needs owner access to GitHub Settings.

| File | Change |
|------|--------|
| `legal.html` | Privacy section: restored the GDPR Art. 77 sentence naming the Austrian DPA (Österreichische Datenschutzbehörde, public authority address and dsb@dsb.gv.at), as carried by the pre-2026-04 revision; og:locale en_AT to en_US |
| `index.html` | og:locale en_AT to en_US (absent from consumer locale lists; Austria stays signalled in copy and JSON-LD address) |
| `.claude/settings.json` | Removed `Bash(hugo:*)` and `Bash(jekyll:*)` allowances to match the no-build convention |
| `BACKLOG.md` | B-06/B-07/B-08 resolved; B-09 closed without creating CONTRIBUTING.md (deliberate: personal site, no contributions solicited); resolution log added; only B-02 remains |
| `audit/02-security-findings.md` | Post-audit addenda on findings Q-13, Q-15, Q-17 |

# Site Patch Changelog -- 2026-06-12 (batch 18: backlog burn-down B-05, B-03, B-01)

Owner-approved implementation of three audit backlog items in dependency
order: CI validation first, then asset pruning, then the meta CSP whose
hash maintenance the new CI guards. ADRs 0007, 0008, and 0009 flip from
proposed to accepted.

| File | Change |
|------|--------|
| `.github/workflows/validate.yml` | New, the repo's first workflow: html-validate@11.5.3 on both pages, sitemap XML parse, manifest/settings JSON parse, JSON-LD parse, and the CSP hash check; `permissions: contents: read`, checkout pinned by digest (v6.0.3) |
| `.github/scripts/check_csp_hashes.py` | New: recomputes every bare inline script/style hash and fails CI when the page's meta CSP no longer lists it |
| `index.html`, `legal.html` | Hash-based meta Content-Security-Policy (default-src 'none'; self-only images, styles, fonts, manifest; hashed inline year script and index style block; placed before all subresources) |
| `profile_roman-mednitzer.webp`, `fonts/outfit-latin-300-normal.woff2`, `fonts/outfit-latin-ext-300-normal.woff2` | Deleted: the "full size" WebP was byte-identical to the 400px file and the 300-weight pair was referenced by no rule (both re-verified before deletion); their two @font-face blocks removed; the 800px PNG master stays |
| `CLAUDE.md` | Layout map gains the workflow; local-validation section now points at CI; portrait notes match the pruned inventory |
| `docs/adr/`, `BACKLOG.md`, `audit/02-security-findings.md` | ADRs 0007/0008/0009 accepted and index updated; B-01/B-03/B-05 removed from the backlog; post-audit addenda recorded on findings S-01, Q-07, Q-08, Q-16 |

# Site Patch Changelog -- 2026-06-12 (batch 17: rebalance highlighted projects)

Owner-approved rebalance of the open-source cards from a 5-of-6 AI/agent
list to a 3 + 3 split: the platform-engineering pillar (the actual job
title) was previously absent. In: `infra` (OpenTofu KVM/Talos IaC),
`automation` (Ansible hardening mapped to NIS2/CRA/GDPR/ISO 27001), and
`isms` (code-managed ISMS, marked early-stage; it substantiates the
hero's "ISO 27001 ISMS implementation" claim). Out (still on GitHub via
the profile link): `agents`, `core-graph`, `sentinel`. Card copy,
licenses, and maturity verified against each repo README on 2026-06-12;
all three are Apache-2.0.

| File | Change |
|------|--------|
| `index.html` | Project grid reordered and recomposed to infra, automation, isms, relay-shell, aiops-mcp, nous; section intro updated to describe the span ("from the code that runs and hardens my own fleet to governed-agent and edge-AI research"); relay-shell, aiops-mcp, and nous cards unchanged |

# Site Patch Changelog -- 2026-06-12 (batch 16: layout and design refinement)

Visual, typographic, and interaction polish; no copy changes, favicon
unchanged per owner direction. All colour work stays inside the existing
token system: the new print palette re-maps the same custom properties the
dark and light palettes already use. Closes backlog item B-04 (audit
finding Q-12).

| File | Change |
|------|--------|
| `style.css` | `color-scheme: dark light` on `:root`; body font-size 16px to 1rem so user browser defaults are respected; background grid fades toward the page bottom via `mask-image`; in-paragraph links underlined (1px, offset, border-accent colour) so links no longer rely on colour alone; global `:focus-visible` outline in accent; `::selection` in accent; `text-wrap: balance` for headings and `text-wrap: pretty` for paragraphs; skip link now becomes visible while keyboard-focused; print block with ink-safe token re-map, grid hidden, links underlined |
| `index.html` | Paired light/dark `theme-color` metas; DM Mono 400 preload (mono renders above the fold); `fetchpriority="high"` on the avatar (LCP); terminal-style `// ` prefix on section headings via `::before` with alt-text syntax (silent for screen readers, fails safe to no prefix where unsupported) |
| `legal.html` | Paired light/dark `theme-color` metas; DM Mono 400 preload |
| `BACKLOG.md` | B-04 (light theme-color meta) removed: implemented in this batch |

# Site Patch Changelog -- 2026-06-12 (batch 15: correct ISO 27001 role wording)

Owner correction: he is not an ISO 27001 auditor; he is a systems engineer
who writes ISMS documentation and implements ISMS requirements. The
"auditor" wording predated batch 14 (it shipped in site.webmanifest and
CLAUDE.md) and batch 14 surfaced it into the visible hero; all three
places now read "ISO 27001 ISMS implementation". The JSON-LD description
("hands-on ISMS/BCM and audit-prep work") already matched the corrected
description and is unchanged. Historical changelog entries stay as
written (append-only log).

| File | Change |
|------|--------|
| `index.html` | Hero experience row: "ISO 27001 auditor" corrected to "ISO 27001 ISMS implementation" |
| `site.webmanifest` | Description: "ISO 27001 auditor" corrected to "ISO 27001 ISMS implementation" |
| `CLAUDE.md` | Topic line: "ISO 27001 auditor" corrected to "ISO 27001 ISMS implementation" |

# Site Patch Changelog -- 2026-06-12 (batch 14: surface verifiable credentials and the nous project)

Owner direction: the profile must stay honest, no overstatements. Every
addition in this batch surfaces facts already published elsewhere by the
owner: languages and memberships come from the page's own JSON-LD, "ISO
27001 auditor" already ships in site.webmanifest's description, the
Hardening tag is backed by the public `automation` repo (Ansible fleet
hardening aligned to NIS2, CRA, GDPR, ISO/IEC 27001), and the new `nous`
card states explicitly that the project is simulation only. Deliberately
not added: anything about clearances, citizenship, professional air-gapped
operations, or a CV (owner-only facts).

| File | Change |
|------|--------|
| `index.html` | Meta description extended with the regulated-environments phrase already used in og:description plus "open-source work on governed automation and edge AI"; hero experience row now reads "ISO 27001 auditor" (matches the manifest); new hero-meta rows "languages: German · English" and "member of: IEEE · Austrian Computer Society (OCG)" (both from the page's JSON-LD); sixth project card `nous` (Apache-2.0, pre-1.0, simulation-based digital twin of an edge-AI appliance with CoT/TAK, STANAG 4774/4778, MISB KLV, NMEA 0183, SensorThings interop; "Simulation throughout; no fielded hardware"); Resilience/Security skill row moved from fifth to second and gains a Hardening tag; JSON-LD knowsAbout gains "Edge AI"; ampersands in description/og:description/twitter:description attribute values encoded as `&amp;` for consistency with the escaped titles (review suggestion; raw `&` + space is valid HTML5, change is cosmetic) |
| `legal.html` | Same escaping consistency pass: og:title and twitter:title now use `&amp;` |

# Site Patch Changelog -- 2026-06-12 (batch 13: feature aiops-mcp in projects)

Swapped the fifth open-source project card at the owner's direction:
`platform-blueprint` (documentation-only engineering blueprint) out,
`aiops-mcp` in. Rationale: highlight deployable code in the site's core
domain; the regulatory/ISO themes platform-blueprint covered stay
represented in the Skills section. Description, license, and maturity
verified against the repo README on 2026-06-12 (Apache-2.0, v0, stdio-only
MCP server combining bitemporal fleet state, a drift engine, and a gated
actuator).

| File | Change |
|------|--------|
| `index.html` | Fifth project card now `aiops-mcp` (was `platform-blueprint`); sitemap lastmod and JSON-LD `dateModified` already read 2026-06-12 from batch 12, so no date changes needed |

# Site Patch Changelog -- 2026-06-12 (batch 12: full audit pass)

Full repository audit: validation baseline, security and quality findings
register, small validation-driven fixes, documentation sync, ADR backfill,
and a prioritized backlog. Reports live under `audit/`, decisions under
`docs/adr/`, deferred work in `BACKLOG.md`. Registry note: the 2026-05-28
PRs #43 (open-source projects expanded from 2 to 5 cards) and #44 (hero
wording and skills casing) shipped without changelog batches at the time;
recorded here, history not rewritten.

| File | Change |
|------|--------|
| `index.html` | Encoded the raw `&` in "MITRE ATT&CK" (restores a clean `html-validate` run); dropped redundant `role="contentinfo"` from the footer (parity with batch 11 on the legal page); added `aria-hidden="true"` to the three decorative contact-button SVGs; after review, moved the footer out of `<main>` (sibling inside the `.page` wrapper) so it maps natively to the contentinfo landmark; JSON-LD `dateModified` bumped to 2026-06-12 |
| `legal.html` | Footer moved out of `<main>` into the `.page` wrapper (same landmark fix as `index.html`; batch 11 had left this page without a contentinfo landmark too) |
| `style.css` | Moved `scroll-behavior: smooth` behind the `prefers-reduced-motion` gate; removed the dead `.repo-list` rule (its article pages were deleted 2026-05-14); corrected the article-layout comment |
| `sitemap.xml` | `/legal` lastmod refreshed 2026-04-29 to 2026-05-28 to match the file's last change; both entries then bumped to 2026-06-12 with this batch's page changes |
| `.well-known/security.txt` | Added GitHub private vulnerability reporting as the first `Contact:` entry (aligns with SECURITY.md) |
| `CLAUDE.md` | Layout map now lists all tracked repo files; local-validation note added for the `/legal` extensionless quirk |
| `README.md` | Added license and security-policy pointers |
| `docs/adr/`, `audit/`, `BACKLOG.md` | New: six accepted ADRs (0001 plus five backfills), three proposed ADRs (meta CSP, asset pruning, CI validation), audit phase reports, prioritized backlog |

# Site Patch Changelog -- 2026-05-28 (batch 11: legal page validation cleanup)

Resolved the remaining `html-validate` errors on the legal page without changing
its content. The fixes are semantic-only: uppercase doctype, native landmark
usage, and removal of a redundant ARIA role.

| File | Change |
|------|--------|
| `legal.html` | Uppercased `<!DOCTYPE html>`, changed the page wrapper from `<div>` to `<main>`, removed redundant `role="main"` from `<article>`, and removed redundant `role="contentinfo"` from `<footer>` |

# Site Patch Changelog -- 2026-05-28 (batch 10: copy tighten + text fixes)

Refined the public profile copy for clarity and flow without changing the site's
structure. The homepage and repository summary now use tighter wording, align on
the same positioning, and remove a few awkward phrases. Also uppercased the
`<!DOCTYPE html>` in `index.html` while touching the page.

| File | Change |
|------|--------|
| `index.html` | Tightened meta descriptions, hero tagline, About, project blurbs, Homelab copy, and JSON-LD description; uppercased `<!DOCTYPE html>` |
| `README.md` | Aligned the repo summary with the refreshed homepage wording |

# Site Patch Changelog -- 2026-05-28 (batch 9: drop em-dashes from site copy)

Removed em-dashes from the public copy per the owner's standing preference
(continuing the earlier "drop em-dashes" pass). Replaced them with commas,
colons, or full stops; no wording or meaning changed. Historical changelog
entries and internal instruction files were left as-is.

| File | Change |
|------|--------|
| `index.html` | 6 em-dashes removed across About, Open-source projects, and Homelab copy |
| `README.md` | 3 em-dashes removed (heading + two tech-note bullets) |
| `CLAUDE.md` | Topic line reworded to avoid the one em-dash added in batch 8 |

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
