# Community Profile — Writing Guide

A community profile is a markdown file that gets loaded as the system prompt
for a Community Analyst agent. Each profile encodes how one community thinks
about decisions in this domain — their mental model, typical concerns, voice,
and the blind-spots they themselves have.

## Why this matters

The Community Analyst agent is a generic implementation. What makes it
specialize as a "founder-engineer-blogger analyst" vs a "reddit-tech-collective
analyst" is the profile loaded as its system prompt. Profiles are
**knowledge artifacts** — they sit alongside source-views as the project's moat.

A good profile lets the analyst:
- Frame the situation the way this community would.
- Surface concerns this community would surface (not generic ones).
- Use language and reference points this community uses.
- Acknowledge what this community typically misses (their own blind spots).

## File location

`community_profiles/<community-tag>.md` where `<community-tag>` matches the
`community_tag` field used in `data/source_registry.yaml`.

## Required sections

Each profile MUST contain these four sections, in this order. The Community
Analyst loader expects this structure.

```markdown
# <Community Name>

## Voice
Two to four sentences describing how this community talks. Tone, level of
formality, typical sentence rhythm, characteristic vocabulary, names of
representative writers/posters.

## Mental model
Three to six bullet points describing how this community sees the world in
this domain. What do they take for granted? What do they consider obvious?
What axioms do they reason from?

## Typical concerns
Three to six bullet points naming the specific risks, mechanics, or angles
this community focuses on. Be concrete — name actual concepts, dollar
amounts, specific traps. Not "be careful about equity" but "the spread tax
on ISOs at exercise if FMV has appreciated significantly above strike".

## Known blind spots OF this community
Three to five bullet points naming what this community itself tends to
miss. What perspectives are underrepresented here? What systematic biases?
This is critical — the Risk Officer uses these to cross-check.
```

## Optional sections

```markdown
## Representative voices
A short list of named writers, posters, or accounts that exemplify this
community. Used by the Community Analyst as concrete style anchors.

## Anti-pattern responses
Two to three examples of how this community would NOT respond — what
generic LLM advice this community would find unhelpful or wrong.
This is anti-training: it sharpens the contrast.
```

## Length

Aim for 250–500 words total. Too short = thin specialization. Too long =
diluted signal. If a section is overflowing, ask whether you're capturing
*this* community specifically or just generic domain knowledge.

## Updating

When the refinement routine (or you, manually) identifies a systematic
failure mode in a community analyst's output, the fix usually goes here.
Update the relevant section, commit, the next turn picks it up.

## Naming convention

`community_tag` slug → filename. Use lowercase, hyphens, no spaces:
- `founder-engineer-bloggers` → `community_profiles/founder-engineer-bloggers.md`
- `reddit-tech-collective` → `community_profiles/reddit-tech-collective.md`
