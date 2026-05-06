# Producer-Consumer Problem Simulation

## Project Overview
This project simulates the classic Producer-Consumer problem using Python threads. It demonstrates how producers and consumers can safely share a bounded buffer by using synchronization primitives.

## Features
- Fixed-size buffer using a queue
- Producer thread(s) adding items to the buffer
- Consumer thread(s) removing items from the buffer
- Synchronization using mutex and semaphores
- Console output showing produced and consumed items and buffer status

## Requirements
- Python 3.7 or later

## How to Run
1. Open a terminal in the project folder.
2. Run the simulation:

```bash
python producer_consumer.py
```

## Project Concepts
- `mutex`: ensures only one thread updates the buffer at a time
- `empty_slots`: semaphore that tracks available buffer capacity
- `filled_slots`: semaphore that tracks items ready to be consumed

## Expected Outcome
The simulation should produce and consume items in a synchronized way without buffer overflow or race conditions.

## Notes
The current implementation uses:
- buffer size: 5
- total items: 20
- one producer thread
- one consumer thread

You can extend the simulation by adding more producer or consumer threads and changing the buffer size.
