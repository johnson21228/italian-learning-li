# Flashcard Category Filter Rule

The Italian flashcard site should not force each flashcard into one rigid tab such as Nouns, Verbs, or Other.

Each flashcard must carry enough metadata to support filtering, speaking, curation, and instruction.

## Required flashcard metadata

Each flashcard should include:

```text
id
italian
english
speak
image
imageAlt
partOfSpeech
categories
curated
```

`italian` is the visible word or phrase. `speak` is the exact Italian text to send to speech synthesis. `image` is the flashcard image path. `curated` records whether the image has been accepted as a curated learning image. `categories` places the flashcard into multiple language-instruction categories.

## Controlled starting categories

Use a small controlled category vocabulary first, then add only when a real instructional need appears:

```text
class-1
noun
verb
phrase
question
greeting
response
conversation-primitive
name-exchange
status-check
repair
formal
informal
essere
stare
chiamarsi
time
person
people
place
place-name
object
animal
language
school
grammar-word
speaking-practice
listening-practice
pronunciation-practice
image-supported
curated
needs-image
needs-review
```

## UI rule

The site should render a filter surface generated from flashcard metadata.

- `All` shows every flashcard.
- Category filters show cards whose `categories` include the selected category.
- Tabs are not the source of truth.
- A phrase can be a question, a conversation primitive, a name-exchange item, a speaking practice item, and curated at the same time.

## Learning reason

Language learning does not fit one folder per word. A learner needs to practice by situation, function, grammar pattern, speech action, and curation state. Categories let the same flashcard participate in several learning paths without duplicating the card.
