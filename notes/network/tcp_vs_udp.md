# TCP vs UDP

- What it is: TCP provides ordered, reliable delivery; UDP provides connectionless datagrams with minimal overhead.
- Why it matters: This is a common starting point for networking interviews and protocol tradeoff questions.
- Interview answer: Choose TCP when correctness and ordering matter; choose UDP when latency and simplicity matter more than guaranteed delivery.
- Common confusion: UDP is not inherently faster in every real system; application-level retries and packet loss can erase that advantage.
