# Process vs Thread

- What it is: Processes isolate memory and resources; threads share a process address space.
- Why it matters: This comes up in concurrency, isolation, scheduling, and performance discussions.
- Interview answer: Processes provide stronger isolation, while threads are cheaper for coordination inside one program.
- Common confusion: Threads are lighter than processes, but they also increase shared-state complexity and synchronization risk.
