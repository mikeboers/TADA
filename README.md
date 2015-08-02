TADA
====

A `todo.txt` processing framework.

Tada is designed to parse plaintext todo lists, provide an API and simple tools
to process them, and rewrite them with minimal formatting changes. Your `todo.txt`
is still yours, but tada is a helpful assitant.


Schema of a Task
----------------

Tasks generally consist of:

- a status indicator, e.g.: `√` for complete, `-` for incomplete, etc.
- a headline containing a series of key-value tokens, e.g.:

    - `@context Do a thing`
    - `Do a thing for +project`
    - `Do a thing with explicit key:value`

- any number of inter-woven sub-task and body text lines


### Status

The status of a task is indicated via a set of symbols, defaulting to:

- `-` incomplete
- `√` complete
- `x` cancelled
- `~` delegated or deferred.

There are two method of specifying this status:

- implicit start: as the first character in the task, e.g.: `√ Do a thing`
- explicit start: within square brackets at the start, e.g.: `- [x] Abandon a task`

The explicit start is required for sub-tasks, as I tend to have lists as
task content that start with hyphens.


### Key-Value Tokens

There are a series of characters that start a key-value token within the
headline of a task. They are typically:

    !PRIORITY
    @CONTEXT
    #TAG
    _GOAL
    -PROJECT
    .SUPER_TASK
    +PROJECT_GROUP
    /CATEGORY
    =DURATION
    ^DUE
    %REPEAT


