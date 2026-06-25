# Card 007: Start Italian-First Chat Mode

## Purpose

Add a reusable session-start prompt for future `italian-learning-li` conversations. The prompt asks for the current pack and places the chat into Italian-first mode.

## Adds

```text
li/workflow/italian_first_chat_mode_rule.md
li/prompts/start_chat_in_italian_mode_with_pack.md
```

## Principle

The Workbench should be easy to re-enter. A future chat should not have to rediscover the desired language posture.

The default posture is:

```text
Italian-first, not Italian-only.
```

The assistant should:

- ask for the current `italian-learning-li` pack when repo state is not available;
- default to simple Italian as much as possible;
- keep the learner inside first-person conversation;
- allow English for clarity, repo work, source custody, terminal commands, or explanation;
- return to Italian after English support;
- use the `Hear → Imitate → Answer → Repair → Capture` loop.

## Session-start phrase

```text
Ciao Steve. Cominciamo in italiano semplice. Come stai?
```

## Value

This card makes Italian mode a durable WB behavior rather than an ad hoc chat preference. Future conversations can find the prompt and immediately resume the correct posture.
