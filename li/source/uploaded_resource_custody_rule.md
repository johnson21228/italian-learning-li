# Uploaded Resource Custody Rule

## Rule

Uploaded Italian learning resources belong in the Workbench as **source resources**, not as ungoverned attachments.

The standard location for resource summaries and use maps is:

```text
source/resources/
```

## Copyright and copying boundary

The Workbench should not blindly copy complete PDFs, books, or course packets into repository packs.

For each uploaded resource, the Workbench should record:

- uploaded file name;
- resource title;
- apparent license or copyright status;
- what the resource contributes;
- high-value sections for the learner;
- how the resource supports conversation-first learning;
- any copying limitation or caution.

If a resource is all-rights-reserved or has unclear reuse rights, preserve a summary and use map only. Do not extract long passages, reproduce chapters, or include full copies in generated artifacts.

If a resource is open or permissively licensed, record the license and still use small, attributed excerpts only when needed.

## Learning-use boundary

Resources should serve the learner's communicative drive. They should be converted into:

```text
Hear → Imitate → Answer → Repair → Capture
```

They should not override the Workbench's first principles:

- conversation before grammar;
- first-person learner participation;
- phrase families before abstractions;
- pronunciation and repair as primary;
- personal corpus as the learner's lived source of truth.

## Future-session behavior

When a future LLM session sees `source/resources/italian_learning_resource_index.md`, it should use the summaries to decide which resource can help the current practice request.

The LLM should say when it is relying on a resource summary rather than the full uploaded PDF.
