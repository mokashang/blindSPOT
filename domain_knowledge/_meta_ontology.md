# Blindspot Meta-Ontology — Life-Decision Domains

## Purpose

This file names the top-level taxonomy of life-decision domains the
Blindspot project covers. It sits as **Layer 0** above the 4-layer
knowledge model in [docs/specs/ROADMAP.md §3](../docs/specs/ROADMAP.md):
each domain named here gets a folder under `domain_knowledge/<slug>/`
with the four layers (decisions, framings, blindspots, sources) the
runtime consumes. Authoring this file is the V2 entry-gate condition
(ROADMAP §4); V2 builds out the 10 domains below under this ontology.

## The 10 V2 domains

Each entry below gives slug, scope, maturity, high-stakes flag (per
ROADMAP §5 Mechanism E), and 3–5 sample decisions.

### 1. tech-career

- **slug**: `tech-career`
- **scope**: US knowledge-worker comp, equity, offer negotiation,
  perf reviews, layoff response, intra-industry job changes. Excludes
  cross-industry pivots (`career-pivots`) and status-dependent moves
  (`immigration`).
- **maturity**: `in-migration` — V1 built this as monolithic
  `data/source_registry.yaml` + `community_profiles/`; V2 migrates
  it into this folder.
- **high_stakes**: `false` — material but recoverable; a bad comp
  negotiation costs money, not health or legal status.
- **sample decisions**:
  - Accept offer A (RSU-heavy) vs offer B (cash-heavy) for a 4-year horizon
  - Exercise ISOs early (paying AMT) vs wait-and-pay-ordinary at IPO
  - Counter-offer strategy after a layoff with severance in hand
  - Stay through cliff vs leave with partial vest

### 2. immigration

- **slug**: `immigration`
- **scope**: US visa categories, status transitions, employer-sponsored
  vs self-petitioned paths, green-card timing, dependent visas. US
  inbound only; outbound emigration deferred to V3+.
- **maturity**: `planned`
- **high_stakes**: `true` — missed filing windows or status lapses
  cause out-of-status, deportation risk, multi-year bans. Mechanism E
  gating applies (Editor "decision-support, not legal advice";
  Critic stricter grounding).
- **sample decisions**:
  - H-1B to O-1 transition timing while I-140 is pending
  - Marry-for-status timing when partner's own GC priority date is current
  - Concurrent I-140/I-485 vs sequential under known retrogression
  - Stay on H-1B vs switch employer mid-PERM
  - Apply for advance parole before international travel during AOS

### 3. housing

- **slug**: `housing`
- **scope**: Rent vs buy, lease terms, mortgage selection (rate type,
  term, down payment trade-offs), location choice within a metro
  (commute, schools, climate risk), primary-residence vs investment-
  property framing. Excludes commercial real estate.
- **maturity**: `planned`
- **high_stakes**: `false` — large dollars but reversible (sell,
  refinance, sublet). Borderline; flagged false because the user
  typically also engages an agent and lender.
- **sample decisions**:
  - Rent vs buy in HCOL metro with 5-year time horizon
  - 30-year fixed vs 7/1 ARM given employer-stability and rate outlook
  - Put 20% down to avoid PMI vs invest the difference in index funds
  - Commute-distance vs school-district trade-off for a family of four
  - Sell current home before buying next vs bridge loan vs contingency

### 4. health-insurance

- **slug**: `health-insurance`
- **scope**: US health coverage decisions — plan selection at open
  enrollment (HDHP / PPO / HMO), HSA/FSA optimization, COBRA vs
  marketplace at job change, Medicare timing, dependent coverage.
  Excludes diagnosis or treatment (see "Out-of-scope").
- **maturity**: `planned`
- **high_stakes**: `true` — wrong choice during the 12-month lock-in
  causes uncapped OOP exposure; Medicare late-enrollment penalties
  are permanent. Mechanism E gating applies.
- **sample decisions**:
  - HDHP + HSA vs PPO for a 32-year-old with no chronic conditions
  - Cover spouse on your plan vs each on respective employer plan
  - COBRA for 18 months vs jump to marketplace immediately after layoff
  - Delay Medicare Part B while on employer plan past 65 vs enroll on time
  - Switch from Marketplace silver to bronze given subsidy cliff

### 5. personal-finance

- **slug**: `personal-finance`
- **scope**: Retirement-account contribution ordering, tax-advantaged
  account strategy (401k, IRA, HSA, 529), brokerage asset allocation,
  debt-payoff vs invest prioritization, tax-loss harvesting. Dollar-
  specific investment guidance is gated.
- **maturity**: `planned`
- **high_stakes**: `true` — dollar-specific investment guidance is
  exactly what Mechanism E was written to gate (Editor "decision-
  support, not financial advice").
- **sample decisions**:
  - Order: 401k match → HSA → Roth IRA → 401k cap → taxable
  - Mega backdoor Roth vs after-tax brokerage given tax-rate trajectory
  - Pay down 6.5% student loans vs invest in S&P 500 index
  - Open 529 in home state vs out-of-state with no tax benefit
  - Tax-loss harvest across taxable + IRA without triggering wash sale

### 6. entrepreneurship

- **slug**: `entrepreneurship`
- **scope**: Founding, co-founder selection, fundraising vs
  bootstrapping, side-business vs full-time leap, freelance/
  consulting structure (sole prop / LLC / S-corp). Excludes deep
  entity-tax optimization (overlaps `personal-finance`).
- **maturity**: `planned`
- **high_stakes**: `false` — failure is the modal outcome and is
  generally survivable; not Mechanism-E-gated despite large dollar
  swings.
- **sample decisions**:
  - 50/50 equity split with co-founder vs vesting-asymmetric split
  - Bootstrap to $1M ARR vs raise seed to compress time-to-PMF
  - Quit day job vs nights-and-weekends until $X MRR
  - LLC pass-through vs S-corp election once net income crosses $80k
  - SAFE post-money valuation cap vs priced seed given dilution math

### 7. education-funding

- **slug**: `education-funding`
- **scope**: Higher-education funding — student-loan type and refi
  timing, grad-school ROI given career stage, 529 / Coverdell /
  taxable savings for children's college, repayment-plan choice.
- **maturity**: `planned`
- **high_stakes**: `false` — slow-clocked and reversible (refinance,
  switch repayment plan, defer enrollment).
- **sample decisions**:
  - Refi federal loans to private vs preserve IDR / PSLF optionality
  - MBA at top-15 with $200k debt vs continue current trajectory
  - Front-load 529 with 5-year-election lump sum vs annual contributions
  - IDR + tax-bomb savings vs 10-year standard
  - In-state public vs out-of-state private with merit aid

### 8. family-planning

- **slug**: `family-planning`
- **scope**: Marriage / partnership financial-legal structuring,
  kids timing and financial readiness, eldercare for aging parents,
  divorce financial separation. Religious and cultural framings
  handled with care (ROADMAP §4 per-domain note).
- **maturity**: `planned`
- **high_stakes**: `true` — child welfare, irreversible legal-status
  changes (marriage, divorce, custody), eldercare medical decisions.
  Mechanism E gating applies most strictly here.
- **sample decisions**:
  - Prenup vs no prenup given asymmetric pre-marital assets
  - First child at 30 vs 35 given career trajectory and biology
  - In-home care vs assisted-living for parent with early-stage dementia
  - Joint vs separate finances after marriage with income gap
  - Mediated vs litigated divorce given custody complexity

### 9. legal-disputes

- **slug**: `legal-disputes`
- **scope**: Contract disputes (vendor, employment, lease), small-
  claims filing, employment-law (wrongful termination, wage,
  discrimination), pre-litigation negotiation. domain_pack.md Editor
  labels output "decision-support, not legal advice" (ROADMAP §4).
- **maturity**: `planned`
- **high_stakes**: `true` — statutes of limitation create hard
  deadlines; admissions / recorded statements are not retrievable.
  Mechanism E gating applies.
- **sample decisions**:
  - Sign separation agreement with non-compete vs negotiate carve-outs
  - File EEOC charge before suing vs proceed directly to state court
  - Demand letter from a lawyer vs pro-se small-claims filing
  - Settle vendor dispute at 60% vs litigate for full breach damages
  - Withdraw resignation after retaliatory environment vs document and exit

### 10. career-pivots

- **slug**: `career-pivots`
- **scope**: Cross-domain professional moves — engineer-to-PM,
  IC-to-management, tech-to-finance, industry switches, return-to-
  school, early-retirement transitions. **Meta-domain** by design
  (see Cross-domain notes).
- **maturity**: `planned`
- **high_stakes**: `false` — large career swings but recoverable on
  multi-year horizons; typical regret is opportunity-cost, not harm.
- **sample decisions**:
  - Pivot from staff engineer to PM at same company vs new company
  - Leave big-tech IC role for early-stage founding-engineer slot
  - Grad school full-time vs part-time vs employer tuition reimbursement
  - FAANG to public-sector / nonprofit given comp delta
  - Coast-FIRE at 45 with bridge-job vs full-FIRE at 50

## Selection criteria

The 10 domains above were chosen per ROADMAP §4 "Choosing the 10
domains" priority order:

- **High personal stakes for a typical US-resident knowledge-worker** —
  V1's user; V3 expands outward.
- **Blind spots known to be costly** — domains where "I didn't know I
  needed to ask" is a common regret in published post-mortems.
- **Reachable source-views** — active English-language communities,
  RSS-able blogs, or static corpora the source-adapter layer can
  ingest. Domains where real expertise lives in private channels are
  deferred (see §10 Honest limits).
- **Coverage diversity** — no two domains collapse to the same
  underlying decision class. RSU comp and ISO comp are one domain
  (`tech-career`); rent-vs-buy and mortgage-type are one domain
  (`housing`); etc.

## Out-of-scope / deferred

Life areas explicitly NOT named as V2 domains:

- **medical-diagnosis** — handled by Mechanism E gating rather than
  as its own domain; Blindspot does not propose diagnoses or
  treatments.
- **specific-legal-advice** — `legal-disputes` covers framings;
  specific advice is referred to counsel via Editor gating.
- **mental-health-treatment** — overlaps medical-diagnosis gating;
  revisit in V3 if a careful source-view set emerges.
- **substance-recovery** — too high-stakes for public source-views;
  bad framing causes severe harm.
- **child-custody-specifics** — `family-planning` covers framings;
  jurisdiction-specific custody outcomes are gated.
- **politics / voting** — out of north-star scope.

`career-pivots` IS a meta-domain — intentional (ROADMAP §4 lines
201–203). Its presence sharpens the 4-layer model because cross-
domain edges are the V4 frame-breaking surface.

## Cross-domain notes

V4 (frame-breaking) leans on the cross-domain edges these 10 domains
imply. The most load-bearing edges:

- **`career-pivots` ↔ everything** — the meta-domain. Almost any
  career-pivot situation also intersects `personal-finance`,
  `housing`, sometimes `immigration` and `family-planning`.
- **`immigration` ↔ `tech-career`** — visa status couples tightly to
  employer choice, comp negotiation, layoff response.
- **`personal-finance` ↔ `tech-career`** — equity comp, RSU vesting,
  ISO exercise math, concentration-risk live on the boundary.
- **`family-planning` ↔ all financial domains** — major transitions
  (marriage, kids, divorce, eldercare) cascade into
  `personal-finance`, `housing`, `health-insurance`, `education-funding`.
- **`legal-disputes` ↔ `housing` and `tech-career`** — landlord-tenant
  and employment-law disputes are where most knowledge-workers first
  encounter the legal system.

These edges are documentation, not runtime data. Triage Officer's
two-pass design (ROADMAP §4 "Architecture changes") multi-labels a
situation across these edges; the notes here help human authors of
per-domain `framings.md` files name the adjacent domains they exclude.

## Update policy

This file is editable by future refine runs:

- **Editing scope is allowed** — sharpen scope statements, add sample
  decisions, refine high-stakes rationale, extend cross-domain notes
  as eval results expose edges.
- **V3-grown domains get appended** — when V3's Mechanism A promotes
  a domain to manually-authored quality, append it here with
  `maturity: planned` and the same field set.
- **Do NOT remove an existing domain without explicit human review.**
  Removal breaks per-domain folder layouts (`domain_knowledge/<slug>/`),
  invalidates fixtures, and confuses `roadmap_progress` logging.
- **Renames are also human-review** — a slug rename ripples through
  fixtures paths, sources.yaml entries, and Triage pass-1 labels.
  Slugs are load-bearing once a domain leaves `maturity: planned`.
