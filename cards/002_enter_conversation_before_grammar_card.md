# Card 002 — Enter Conversation Before Studying Grammar

## Intent

Add the second Italian Learning LI card: the learner enters conversation before studying grammar.

## Problem

A beginning learner can get blocked if Italian starts as grammar explanation. The Workbench needs a stable rule that keeps the learner in a small exchange first.

## Decision

The Workbench treats conversation as the first doorway.

The learner should first:

1. hear a useful phrase;
2. imitate it aloud;
3. answer with a short first-person response;
4. repair misunderstanding;
5. capture the useful phrase in a personal corpus.

The required loop is:

```text
Hear → Imitate → Answer → Repair → Capture
```

Grammar may be used afterward to clarify a pattern already encountered in speech.

## New LI

```text
li/domain/conversation_before_grammar_rule.md
li/practice/hear_imitate_answer_repair_loop.md
li/prompts/enter_conversation_before_grammar.md
li/prompts/repair_misunderstanding_in_italian.md
li/prompts/capture_personal_corpus_entry.md
```

## Required repair phrases

```text
Non capisco.
Puoi ripetere?
Più lentamente, per favore.
Che significa?
Come si dice in italiano?
```

## Example micro-exchanges

```text
A: Ciao. Come ti chiami?
B: Mi chiamo Steve.
```

```text
A: Come si chiama questo?
B: Si chiama libro.
```

```text
A: Vuoi un caffè?
B: Sì, voglio un caffè.
```

```text
A: Capisci?
B: Non capisco. Puoi ripetere lentamente?
```

## Verification

`make verify` should confirm the new card, rule, practice loop, prompts, map references, spine references, and required Italian repair phrases.
