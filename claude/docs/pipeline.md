# Claude Skill Pipeline

This document describes how the 7 pre-built skills work together as a coordinated team, inspired by the Hermes Agents Forge workflow.

## Pipeline Overview

```
[Idea] → market-scout → idea-challenger → decision-bot → product-manager → product-architect → mvp-builder → qa-engineer → [Demo]
```

## Stage 1: Discovery & Research

### market-scout
**Purpose**: Market research and competitive analysis
**Input**: An idea, market, or technology area
**Output**: Market report with size, competitors, opportunities, recommendation
**Handoff to**: idea-challenger (with market data)

### idea-challenger
**Purpose**: Challenge assumptions and validate ideas
**Input**: Raw idea + market research from market-scout
**Output**: Challenge report with risk-ranked assumptions, evidence gaps, recommendation
**Handoff to**: decision-bot (with assumptions + risks)

## Stage 2: Decision & Planning

### decision-bot
**Purpose**: Facilitate structured decision-making
**Input**: Options, criteria, context from research/validation stages
**Output**: Decision recommendation with scoring, confidence levels, contingency plans
**Handoff to**: product-manager (with approved direction + constraints)

### product-manager
**Purpose**: Create product specifications and roadmaps
**Input**: Validated idea + constraints from decision-bot
**Output**: Product Requirements Document with user stories, roadmap, success metrics
**Handoff to**: product-architect (with PRD + requirements)

## Stage 3: Architecture & Build

### product-architect
**Purpose**: Design technical architecture and implementation approach
**Input**: PRD from product-manager
**Output**: Architecture design with stack choices, component diagrams, implementation guidance
**Handoff to**: mvp-builder (with architecture + guidance)

### mvp-builder
**Purpose**: Build minimum viable product through iterations
**Input**: Architecture from product-architect
**Output**: Built MVP with working code, tests, file paths documented
**Handoff to**: qa-engineer (with built MVP + test scenarios)

## Stage 4: Validation

### qa-engineer
**Purpose**: Validate quality through systematic testing
**Input**: Built features from mvp-builder
**Output**: QA report with test results, bugs found, readiness verdict
**Handoff to**: mvp-builder (with bugs to fix) or back to product-manager (if major issues)

## Usage Example

Start a conversation in Claude Desktop and try:

```
/market-scout "AI tools for personal fitness coaching"

[After receiving market report]

/idea-challenger "Based on the market research, we found a $5B market growing at 25% CAGR. Key risks: user retention and content personalization. Should we build this?"
```

Then continue the chain through each skill.

## Agent Instructions

For Claude (or any LLM) to run this pipeline autonomously:

1. **Start at any point** — Each skill can accept raw input or handoff from another skill
2. **Chain calls** — Pass outputs between skills in sequence
3. **Iterate** — If qa-engineer finds issues, hand back to mvp-builder
4. **Document decisions** — decision-bot's confidence levels guide whether to continue or pivot

## Package Names

| Skill | File | Persona |
|-------|------|----------|
| market-scout | market-scout.zip | Market Scout (Researcher) |
| idea-challenger | idea-challenger.zip | Idea Challenger (Analyst) |
| decision-bot | decision-bot.zip | Decision Bot (Gatekeeper) |
| product-manager | product-manager.zip | Product Manager (Coordinator) |
| product-architect | product-architect.zip | Product Architect (Specialist) |
| mvp-builder | mvp-builder.zip | MVP Builder (Builder) |
| qa-engineer | qa-engineer.zip | QA Engineer (Gatekeeper) |