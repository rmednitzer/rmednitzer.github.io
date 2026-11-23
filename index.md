# Roman Mednitzer

Senior Systems & Platform Engineer · Vienna, Austria

I like understanding how things work, especially where technologies and disciplines meet.

## Professional work

I have around ten years of production infrastructure experience across managed services, enterprise infrastructure and a regulated medical-device environment.

I work between development, operations and security: I turn requirements into changes that run in production and stay with them until they run reliably.

### Platforms and integration

I connect infrastructure layers, services and applications into systems that can be operated and maintained. Most problems live at the interfaces, so that is where I focus: how components, dependencies and failure modes interact.

### Operations and recovery

I troubleshoot production systems and run changes and backups. A backup is not done until a restore test has proved it, and every change I plan has a way back.

### Automation and documentation

I automate repetitive infrastructure work and write the documentation that lets others operate, maintain and take over the systems I build.

## How I work

These habits shape how I build systems. My public projects show them in practice, so each one links to the evidence.

### Decisions in writing

I record significant design decisions before building them: the context, the alternatives considered and the consequences, so the reasoning survives the person who made it.

[relay-shell decision records](https://github.com/rmednitzer/relay-shell/blob/main/docs/adr/README.md).

### Failure analysis first

Before a system acts on its own or holds sensitive data, I work out which losses are unacceptable and how they could happen, using STPA alongside threat modelling at trust boundaries.

[osint-workbench STPA analysis](https://github.com/rmednitzer/osint-workbench/blob/main/docs/assurance/stpa.md).

### Records you can trust

Actions should leave evidence. relay-shell writes an audit record for every call and chains the records by hash, so later tampering is detectable.

[Audit hash-chain decision](https://github.com/rmednitzer/relay-shell/blob/main/docs/adr/0007-audit-hash-chain.md).

### Recovery is proved

A backup counts once it has been restored. osint-workbench checkpoints restore into an isolated database and are checked against an integrity receipt.

[Checkpoint and recovery procedure](https://github.com/rmednitzer/osint-workbench/blob/main/docs/recovery.md).

### Honest status

Each project separates what is implemented, what has been verified and what is still open, so nobody has to guess what works.

[osint-workbench status](https://github.com/rmednitzer/osint-workbench/blob/main/STATUS.md).

### Control stays local

I prefer open, self-hostable technology. osint-workbench runs locally by default; cloud AI needs an explicit, approved route and denies everything otherwise.

[Governed cloud routes](https://github.com/rmednitzer/osint-workbench/blob/main/docs/cloud-routes.md).

## Selected projects

These are personal, AI-assisted projects I build outside work. I set the requirements and design, make the integration decisions, and review, validate and operate the result; AI does much of the implementation, testing and documentation.

### [relay-shell](https://github.com/rmednitzer/relay-shell)

A Model Context Protocol (MCP) server that gives AI clients the full reach of a shell: local commands, interactive sessions, SSH fleet operation, file transfer and port forwarding, with a per-call audit record and risk classification for every action. Built as operator infrastructure for hosts you own: open by default, with opt-in refusal modes and no sandbox.

[Documentation and limits](https://github.com/rmednitzer/relay-shell/blob/main/README.md).

### [osint-workbench](https://github.com/rmednitzer/osint-workbench)

A self-hostable workbench that collects open-source information, preserves it as immutable evidence and makes it searchable, with optional local or governed cloud AI and read-only access for AI assistants.

Collection, evidence, search and recovery paths work today; the full platform is still in development.

[Implementation status](https://github.com/rmednitzer/osint-workbench/blob/main/STATUS.md).

### Personal experimentation

My private lab is where I try ideas before I trust them: I run AI infrastructure and automation, test integrations, and rehearse migrations and recovery. I also study how AI agents behave in real operations: whether they act on command results correctly and stay consistent over long tasks.

## Interests

I tend to follow a question across disciplines rather than stop where one field ends. AI, robotics and cybernetics interest me because they connect engineering with questions about intelligence, identity and how people might live. Human augmentation and space exploration appeal to the same curiosity: what could we become capable of, and what would it take to get there?

Open systems and digital sovereignty matter to me because I want to understand, adapt and retain control of the technology I use.

Hard science fiction gives me another way to explore those possibilities and their consequences. My musical tastes lean towards industrial, electronic body music (EBM) and dark ambient.

## Contact

- [LinkedIn](https://www.linkedin.com/in/rmednitzer)
- [GitHub](https://github.com/rmednitzer)
- Email: r.mednitzer@ieee.org

Canonical public profile: https://rmednitzer.github.io/
Profile reviewed: 2026-11-23.
