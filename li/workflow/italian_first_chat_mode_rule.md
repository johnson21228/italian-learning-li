# Italian-First Chat Mode Rule

## Rule

When an Italian Learning LI session starts, the chat should default to Italian-first interaction.

Italian-first does not mean Italian-only. In short: Italian-first, not Italian-only. It means:

- begin in simple Italian whenever possible;
- keep the learner inside conversation as much as possible;
- use short, clear Italian before explanation;
- allow English for safety, clarity, repo work, source custody, terminal commands, copyright boundaries, or when the learner asks;
- after English support, return to Italian as soon as practical;
- prefer one small question or exchange at a time;
- preserve the `Hear → Imitate → Answer → Repair → Capture` loop;
- ask for the current Workbench pack when the session needs repo-grounded LI continuity.

## Pack requirement

A new or resumed Workbench chat should ask for the current `italian-learning-li` pack when the assistant cannot already see the current repo state.

The current pack lets the assistant read:

```text
MAP.md
SPINE.md
README.md
outputs/history/repo_history_for_llm.md
source/resources/italian_learning_resource_index.md
li/prompts/
li/practice/
li/corpus/
```

The pack request should be friendly and short:

```text
Please upload the current `italian-learning-li` pack so I can use the latest WB state. After I read it, I will run this chat in Italian-first mode.
```

## Italian-first behavior

The assistant should use Italian as the default language for the learning exchange:

```text
Ciao. Cominciamo in italiano semplice.
```

The assistant may use English to explain what is happening:

```text
Brief English support: I will keep asking one small Italian question at a time.
```

Then return to Italian:

```text
Adesso: Come stai?
```

## Boundary

Do not force Italian when English is necessary for the learner to understand the workflow, source limits, commands, or repo changes. The goal is to maximize Italian use while keeping the learner oriented.
